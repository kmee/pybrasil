import sys

if sys.version_info.major == 3:
   from .decimal3 import Decimal
elif sys.version_info.major == 2:
   from .decimal2 import Decimal
else:
    raise ('Versão python não suportada')

