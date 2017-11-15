def set_update_clause(update_clause, key, val, is_array=False):
    if not val:
        return

    if is_array:
        if not isinstance(val, (tuple, list)):
            raise Exception('Value %s for key %s must be array' %
                            (val, key))
        add_to_set = update_clause.setdefault('$addToSet', {})
        add_to_set[key] = {'$each': val}
    else:
        set_clause = update_clause.setdefault('$set', {})
        set_clause[key] = val
        
update_clause = {}
set_update_clause(update_clause, 'info.name', 'Amon Ra')
set_update_clause(update_clause, 'related.bananas', ['crazy banana'], 
                  is_array=True)
print(update_clause)