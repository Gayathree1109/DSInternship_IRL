a = 'M{0,3}'
b = '(C[MD]|D?C{0,3})'
c = '(X[CL]|L?X{0,3})'
d = '(I[VX]|V?I{0,3})'
regex_pattern = r"%s%s%s%s$" % (a, b, c, d)# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))