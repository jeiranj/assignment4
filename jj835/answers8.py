#
# Python answers8.py
#
D = {'first':[2,1],'second':[2,3],'third':[3,4]}
d1=D['first']
d3=D['third']
D['first']=d3
D['third']=d1

d3=D['third']
d3.sort()
D['third']=d3

D['fourth']=D['second']

del D['second']

print D
