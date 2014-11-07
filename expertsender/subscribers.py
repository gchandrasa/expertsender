import urllib
import requests

from django.conf import settings

from .utils import generate_subscribe_xml

xsi = 'http://www.w3.org/2001/XMLSchema-instance'

API_SERVER = getattr(settings, 'EXPERTSENDER_API_SERVER', 'https://api2.esv2.com')

SUBSCRIBE_ADD_AND_UPDATE = 'AddAndUpdate'
SUBSCRIBE_ADD_AND_REPLACE = 'AddAndReplace'
SUBSCRIBE_ADD_AND_IGNORE = 'AddAndIgnore'
SUBSCRIBE_IGNORE_AND_UPDATE = 'IgnoreAndUpdate'
SUBSCRIBE_IGNORE_AND_REPLACE = 'IgnoreAndReplace'


def subscribe(api_key, email, list_id, fields, extra_fields=None, mode=SUBSCRIBE_ADD_AND_UPDATE):
    xml = generate_subscribe_xml(api_key, email, list_id, extra_fields, mode)
    headers = {'Content-Type': 'application/xml'}
    return requests.post('%s/Api/Subscribers/' % API_SERVER, data=xml, headers=headers)


def unsubscribe(api_key, email, list_id=None):
    params_list = ['apiKey=%s' % api_key, 'email=%s' % urllib.quote(email)]
    if list_id:
        params_list.append('listId=%s' % list_id)
    params = '&'.join(params_list)
    return requests.delete('%s/Api/Subscribers?%s' % (API_SERVER, params))
