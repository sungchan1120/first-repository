import re 

data = """
park 010-9988-9999
"""

pat = re.compile("(\d{3})[-](\d{4})[-](\d{4})")
print(pat.sub("\g<3>-####", data))