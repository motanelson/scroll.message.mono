import os
import copy
print("\033c\033[47;31m\ngive me file .class: ? \n")
a=input().strip()
rrr=a.replace(".class","")
ttt="/usr/bin/openjdk-asmtools-jdis $1 -w /tmp/".replace("$1",a)
os.system(ttt)
f1=open("/tmp/$2.jasm".replace("$2",rrr),"r")
bodys=f1.read()
f1.close()

b=bodys.split("\n")
line=1
aa=True
cc=False
for bb in b:
    hh=bb.find("public")
    if hh<0:
        hh=bb.find("private")
    if hh>-1:
        print(bb) 
    line=line+1
        