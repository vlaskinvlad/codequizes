import re
origin = raw_input()
substirng = raw_input()
p = re.compile("(?=(%s))" % substirng)
print(len(re.findall(p, origin)))
