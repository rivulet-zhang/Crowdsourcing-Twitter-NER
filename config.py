#!/usr/local/bin/python2.7
# vim: set fileencoding=utf8 noexpandtab tabstop=4 shiftwidth=4:   # boilerplate
from __future__ import division as _, unicode_literals as _; del _ # boilerplate

import os, sys

PATH_BASE = os.path.abspath(sys.path[0])
PATH_DATABASE = "data/db.sqlite"

del os, sys  # keep namespace clean
