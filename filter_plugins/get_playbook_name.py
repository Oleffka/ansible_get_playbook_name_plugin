from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import re


def run(message):
    pattern_filter = '[a-zA-Z0-9_-]*[.]ya?ml'
    find = re.search(pattern_filter, message)

    return find.group()


class FilterModule(object):
    def filters(self):
        return { 'get_playbook_name': run }
