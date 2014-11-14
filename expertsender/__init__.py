from lxml import etree
import requests

from django.conf import settings

from .subscribers import subscribe, unsubscribe
from .subscribers import (SUBSCRIBE_ADD_AND_UPDATE, SUBSCRIBE_ADD_AND_REPLACE,
                    SUBSCRIBE_ADD_AND_IGNORE, SUBSCRIBE_IGNORE_AND_UPDATE,
                    SUBSCRIBE_IGNORE_AND_REPLACE)

xsi = 'http://www.w3.org/2001/XMLSchema-instance'

API_SERVER = getattr(settings, 'EXPERTSENDER_API_SERVER', 'https://api2.esv2.com')
TIMEOUT = getattr(settings, 'EXPERTSENDER_TIMEOUT', 5)


def send_email(api_key, email, transactional_id, list_id=None, options=None):
    doc = etree.Element('ApiRequest', nsmap={'xsi':'http://www.w3.org/2001/XMLSchema-instance', 'xs': 'http://www.w3.org/2001/XMLSchema'})
    etree.SubElement(doc, 'ApiKey').text = api_key
    data = etree.SubElement(doc, 'Data')
    # receiver
    receiver = etree.SubElement(data, 'Receiver')
    etree.SubElement(receiver, 'Email').text = email
    if list_id:
        etree.SubElement(receiver, 'ListId').text = unicode(list_id)

    # snippets
    if options and 'snippets' in options:
        snippets = etree.SubElement(data, 'Snippets')
        for snippet in options['snippets']:
            snippet_tree = etree.SubElement(snippets)
            etree.SubElement(snippet_tree, 'Name').text = snippet['name']
            etree.SubElement(snippet_tree, 'Value').text = snippet['value']
    xml = etree.tostring(doc)
    headers = {'Content-Type': 'application/xml'}
    response = requests.post('%s/Api/Transactionals/%s' % (API_SERVER, transactional_id), data=xml, headers=headers, timeout=TIMEOUT)

    return response
