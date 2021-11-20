import cmath
import json
data = {}
data['point'] = []
# reading PN Points or Nenner - Zähler Parameter
for i in range (4):
    type_PN= input(str(i) + "PN typ: ")
    if type_PN == "e": break
    PNre= input("re: ")
    PNim= input("im: ")
    data['point'].append({
    'type': type_PN,
    're': PNre,
    'im': PNim
    })
with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)

# reading_Control

with open('data.txt') as json_file:
    data = json.load(json_file)
    print(json.dumps(data, sort_keys=True, indent=4))
    #print(json.dumps(data))

    for p in data['point']:
        print('type: ' + p['type'])
        print('re: ' + str(p['re']))
        print('im: ' + str(p['im']))
        print('')
# complex array generator
import numpy as np
point_zero = [ complex(0, i) for i in range(4) ]
print (point_zero)
point_pole = [ complex(0, i) for i in range(4) ]
print (point_pole)

for i in range (4):
    point_pole [i] = complex (10,0)
    point_zero [i] = complex (10,0)

print (point_pole)
print (point_zero)
zpt_test = 0.0
i = 0
k =0
for p in data['point']:
    if p['type'] == "p":
        zpt_test = float(p['re'])
        if zpt_test <= 10: 
            point_pole [i] = complex (float(p['re']),float(p['im'] ))
            i=i+1
 
for p in data['point']:
    if p['type'] == "z":
        zpt_test = float(p['re'])
        if zpt_test <= 10:
            point_zero [k] = complex (float(p['re']),float(p['im'] ))
            k=k+1

#for p in data['point']:
#    if p['type'] == "p":
#        point_pole [i] = complex (float(p['re']),float(p['im'] ))
#       print ("complex pole " + str (i) + str (point_pole[i]))
#        i =i + 1

#    if p['type'] == "z":
#        point_zero [k] = complex (float(p['re']),float(p['im'] ))
#        k=k+1
print ("zero number : " + str(k) +" -- pole number : " + str(i) )
print (point_pole)
print (point_zero)


         