def set_val(doc, val, key):
    """ Set a value for dot separated key """
    keys = key.split('.')
    d = doc
    for k in keys[:-1]:
        d = d.setdefault(k, {})
    d[keys[-1]] = val
    
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

set_val(doc, 'Mogka', 'horde.orcs.name')
print(doc)