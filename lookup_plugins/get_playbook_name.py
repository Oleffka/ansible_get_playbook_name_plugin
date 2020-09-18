from ansible.plugins.lookup import LookupBase

import sys
import re


class LookupModule(LookupBase):

  def run(self, terms, inject=None, **kwargs):

    pattern_filter = '[a-zA-Z0-9_-]*[.]ya?ml'
    cmdline = " ".join(map(str, sys.argv))

    try:
      find = re.search(pattern_filter, cmdline)
      return [find.group()]
    except:
      AttributeError
