from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import sys
import re


def run(message):
    pattern_filter = '[a-zA-Z0-9_-]*[.]ya?ml'
    cmdline = " ".join(sys.argv)

    try:
      find = re.search(pattern_filter, cmdline)
      return find.group()
    except:
      AttributeError

class FilterModule(object):
    def filters(self):
        return { 'get_playbook_name': run }
