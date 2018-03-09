import logging
import re
from bson import json_util


LOG = logging.getLogger(__name__)


class EJSONReader():

    OPTIONS_MAP = {
        'i': re.IGNORECASE,
        'm': re.MULTILINE
    }

    @staticmethod
    def loads(ejson_str):
        ejson_value = json_util.loads(ejson_str)
        ejson_value = EJSONReader._transform_regex(ejson_value)
        return ejson_value

    @staticmethod
    def _transform_regex(value):
        """
        Do:
        - for something like:
            {"$regex":"example\\\\.","$options":"im"}
            in the regex's value replace two backslashes with one
        - for something like: 
            {"$type":"RegExp","$value":{"regex":"example","options":"i"}}
            return re.compile('example', flags=re.IGNORECASE)
        """

        if isinstance(value, (list, tuple)):
            new_items = []
            for item in value:
                new_items.append(EJSONReader._transform_regex(item))
            return new_items

        if not isinstance(value, dict):
            return value

        _dict = value
        for k, v in _dict.items():
            if k == '$regex' and '$options' in _dict:
                # "example\\\\." -> "example\\."
                _dict[k] = v.replace('\\\\', '\\')
                continue
            elif k == '$type' and v == 'RegExp':
                return EJSONReader._get_ejson_RegExp_replacement(_dict)

            _dict[k] = EJSONReader._transform_regex(v)

        return _dict

    @staticmethod
    def _get_ejson_RegExp_replacement(reg_exp_dict):
        """ If <reg_exp_dict> is:
        {"$type":"RegExp","$value":{"regex":"mogka","options":"i"}}
        will return
        re.compile('mogka', flags=re.IGNORECASE)
        """
        if reg_exp_dict['$type'] != 'RegExp':
            raise Exception('Method used incorrectly')

        value = reg_exp_dict['$value']
        flags = 0  # no flags
        for option in value.get('options') or '':
            option_number = EJSONReader.OPTIONS_MAP.get(option)
            if not option_number:
                LOG.warning('Unsupported regex option: %s', option)
                continue
            flags = flags | option_number

        regex = value['regex'].replace('\\\\', '\\')
        # this is how dot is escaped in qExports mongo collection ($regex):
        # "example\\\\."
        return re.compile(regex, flags=flags)
