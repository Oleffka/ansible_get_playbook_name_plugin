from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import re


# pattern_filter = '[a-zA-Z0-9_-]*[.][a-z]*'
#
# message = "/usr/local/bin/python /usr/local/bin/ansible-playbook get-playbook-name.yml"
#
# def run(message):
#     find = re.search(pattern_filter, message)
#     return find.group()
#
# run(message)

def run(message):
    pattern_filter = '[a-zA-Z0-9_-]*[.][a-z]*'
    find = re.search(pattern_filter, message)

    return find.group()


class FilterModule(object):
    def filters(self):
        return { 'get_playbook_name': run }
