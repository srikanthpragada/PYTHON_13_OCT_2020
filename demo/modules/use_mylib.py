import sys
print(sys.path)

from mylib import math_funs
from mylib.str_funs import extract_upper

print(extract_upper('AbcAbc'))
print(math_funs.iseven(10))
