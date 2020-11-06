# import math_funs
# import math_funs as mf
import sys
# Add new folder to module search path
sys.path.insert(0, r'c:\classroom\oct13\demo\mylib')
print(sys.path)

from math_funs import iseven
# from math_funs import *

import str_funs as st

print(iseven(10))
# print(largest(10,20))

print(st.extract_upper("PyThon"))
