import re


str = '''firstbit solution is an educational institute 
       Firstbit solution address fc @ road 4012207 '''
       
pattern = r'Firstbit'

pattern = re.compile(pattern)

res = re.findall(pattern ,str)
print(res)