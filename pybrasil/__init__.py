# -*- coding: utf-8 -*-

from __future__ import (division, print_function, unicode_literals,
                        absolute_import)

import sys
if sys.version >= '3':
    unicode = str

from . import (base, data, ibge, inscricao, ncm, telefone, valor, template,
               febraban)
from .python_pt_BR import python_pt_BR
