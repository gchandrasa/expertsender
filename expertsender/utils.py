from lxml import etree


xsi = 'http://www.w3.org/2001/XMLSchema-instance'


def generate_subscribe_xml(api_key, email, list_id, fields, mode, extra_fields=None):
    """
        extra_fields should be list of dictionaries. Example:
        extra_fields = [{'id': 1, 'type': 'string', 'value': 'hello'}]
    """
    doc = etree.Element('ApiRequest', nsmap={'xsi':'http://www.w3.org/2001/XMLSchema-instance', 'xs': 'http://www.w3.org/2001/XMLSchema'})
    etree.SubElement(doc, 'ApiKey').text = api_key
    
    subscriber = etree.SubElement(doc, 'Data', attrib={'{%s}type' % xsi: 'Subscriber'})
    etree.SubElement(subscriber, 'Mode').text = mode
    etree.SubElement(subscriber, 'Force').text = 'true'
    etree.SubElement(subscriber, 'ListId').text = '%s' % list_id
    etree.SubElement(subscriber, 'Email').text = email
    
    for key, value in fields.items():
        etree.SubElement(subscriber, key).text = value

    # Custom fields
    if extra_fields:
        properties = etree.SubElement(subscriber, 'Properties')
        for item in extra_fields:
            property = etree.SubElement(properties, 'Property')
            etree.SubElement(property, 'Id').text = item['id']
            etree.SubElement(property, 'Value', attrib={'{%s}type' % xsi: 'xs:%s' % item['type']}).text = item['value']
    return etree.tostring(doc)
