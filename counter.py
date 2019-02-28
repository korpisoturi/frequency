#!/usr/bin/python

try:
  jono=open("cipher.txt", "r").read()
except:
  print "Cannot open cipher.txt file."
  
jono=jono.lower()
aakkoset=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
weight=['0']*52
valmis=['0']*26
palauta=['0']*26
paino=0
apulaskuri=0

for x in aakkoset:
  paino=jono.count(x,0,len(jono))
  weight[(apulaskuri*2)]=x
  weight[((apulaskuri*2)+1)]=paino
  apulaskuri+=1
valmis=str(sorted([weight[i:i+2] for i in range(0,len(weight),2)], key=lambda x:x[1]))
apulaskuri=0
for x in valmis:
  if x in aakkoset:
    palauta[apulaskuri]=x
    apulaskuri+=1
palauta.reverse()
print "Letter's frequency order: "+str(palauta)
