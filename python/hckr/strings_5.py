import re
s = raw_input()

if re.findall("[A-Za-z0-9]", s):
    print "True"
else:
    print "False"

if re.findall("[A-Za-z]", s):
    print "True"
else:
    print "False"

if re.findall("[0-9]", s):
    print "True"
else:
    print "False"

if re.findall("[a-z]", s):
    print "True"
else:
    print "False"

if re.findall("[A-Z]", s):
    print "True"
else:
    print "False"
