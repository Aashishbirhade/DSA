
for i in range(int(input())):
    a = input()
    v =a.split()
    s = []
    
    for i in range(len(v)):
        if v[i] == v[i].upper():
            s.append(v[i])
        else:
           s.append(v[i].title())
    print(" ".join(s))
#Input
# hello world
# this is a CODECHEF problem
# WELCOME to the JUNGLE
# the quick BROWN fOx
# programming in PYTHON
#output
# Hello World
# This Is A CODECHEF Problem
# WELCOME To The JUNGLE
# The Quick BROWN Fox
# Programming In PYTHON