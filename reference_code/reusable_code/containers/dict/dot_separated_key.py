def equal_arrays(arr1, arr2, none_equals_empty_arr=True):
    """ Check if two lists have the same elements """

    if not arr1 and not arr2:  # None or empty tuple/list
        if none_equals_empty_arr:
            return True
        if ((arr1 is None and arr2 is not None) or
                (arr1 is not None and arr2 is None)):
            return False
        return True

    return Counter(arr1) == Counter(arr2)


def set_dict_val(d, key, val):
    """ Set a value for dot separated key """
    keys = key.split('.')
    for k in keys[:-1]:
        d = d.setdefault(k, {})
    d[keys[-1]] = val


def get_dict_val(doc, key):
    """ Get a value for dot separated key 

    Return field_exists, value
    field_exists - if the key exists in doc
    value - the value for the specified key
    """
    field_exists = True
    val = None
    keys = key.split('.')
    for k in keys[:-1]:
        if k not in doc:
            field_exists = False
            break
        doc = doc[k]

    if field_exists:
        key = keys[-1]
        if key in doc:
            val = doc[key]
        else:
            field_exists = False

    return field_exists, val
    
# doc = {
# }

# doc = {
#     'horde': {}
# }

# doc = {
#     'horde': {
#         'orcs': {}
#     }
# }

doc = {
    'horde': {
        'orcs': {
            'type': 'Melee'
        }
    }
}

set_val(doc, 'horde.orcs.name', 'Mogka')
print(doc)