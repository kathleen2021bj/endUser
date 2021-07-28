import matplotlib.pyplot as plt
from matplotlib import font_manager as fm, rcParams
import os
import math


fig, ax = plt.subplots()
l = []
p = 0
for i in range(0, 1000):
    c = p + 0.01
    p = c
    l.append(c)


# λ1 > 0, λ2 > 0 ;  λ1 = λcS- λr, λ2 = λw - λm
## λ1 > λ2 Vmin > 0
λ1G = 20   #λcS = 30 , λr = 10
λ2G = 10   #λw = 24 , λm = 14
comG = 20
lable1 = 'Vmin > 0'
Vmin = λ1G / math.sqrt(λ1G/λ2G) + λ2G*math.sqrt(λ1G/λ2G) - comG
print("1--λ1 > λ2   Vmin = {}".format(Vmin))
v1 = []
a = λ1G
b = λ2G
c = comG
for t in range(0, 1000):
    vtmp = (a/l[t])+b*l[t]-c
    v1.append(vtmp)

plt.plot(l, v1, label="{}".format(lable1))
## λ1 > λ2 Vmin < 0, λ1 + λ2 - com > 0
λ1G = 24   #λcS = 36 , λr = 12
λ2G = 11   #λw = 21 , λm = 10
comG = 33
lable2 = 'Vmin < 0, λ1 + λ2 - com > 0'
Vmin = λ1G / math.sqrt(λ1G/λ2G) + λ2G*math.sqrt(λ1G/λ2G) - comG
conditionOne = λ1G + λ2G - comG
conditionTwo = comG*comG - 4*λ1G*λ2G
if conditionOne > 0 and conditionTwo >= 0 :
    l1 = (comG - math.sqrt(comG*comG-4*λ1G*λ2G))/(2*λ2G)
    l2 = (comG + math.sqrt(comG*comG-4*λ1G*λ2G))/(2*λ2G)
    print("1--λ1 > λ2 Vmin = {},  l1 = {},  l2 = {}".format(Vmin,l1,l2))
    v2 = []
    a = λ1G
    b = λ2G
    c = comG
    for t in range(0, 1000):
        vtmp = (a/l[t])+b*l[t]-c
        v2.append(vtmp)
    plt.plot(l, v2, label="{}".format(lable2))
else :
    print("Vmin = {} ,conditionOne = {}, conditionTwo = {},should not be here".format(Vmin,conditionOne,conditionTwo))


## λ1 > λ2 Vmin < 0, λ1 + λ2 - com = 0
λ1G = 22   #λcS = 48 , λr = 26
λ2G = 11   #λw = 21 , λm = 10
comG = 33
lable4 = 'Vmin < 0, λ1 + λ2 - com = 0'
Vmin = λ1G / math.sqrt(λ1G/λ2G) + λ2G*math.sqrt(λ1G/λ2G) - comG
conditionOne = λ1G + λ2G - comG
conditionTwo = comG*comG - 4*λ1G*λ2G
if conditionOne == 0 and conditionTwo >= 0 :
    l1 = (comG - math.sqrt(comG*comG-4*λ1G*λ2G))/(2*λ2G)
    l2 = (comG + math.sqrt(comG*comG-4*λ1G*λ2G))/(2*λ2G)
    print("1--λ1 > λ2 Vmin = {},  l1 = {},  l2 = {}".format(Vmin,l1,l2))
    v4 = []
    a = λ1G
    b = λ2G
    c = comG
    for t in range(0, 1000):
        vtmp = (a/l[t])+b*l[t]-c
        v4.append(vtmp)
    plt.plot(l, v4, label="{}".format(lable4))
else :
    print("Vmin = {} ,conditionOne = {}, conditionTwo = {},should not be here".format(Vmin,conditionOne,conditionTwo))



## λ1 > λ2 Vmin < 0, λ1 + λ2 - com < 0
λ1G = 20  #λcS = 36 , λr = 16
λ2G = 11  #λw = 21 , λm = 10
comG = 33
lable3 = 'Vmin < 0, λ1 + λ2 - com < 0'
Vmin = λ1G / math.sqrt(λ1G/λ2G) + λ2G*math.sqrt(λ1G/λ2G) - comG
conditionOne = λ1G + λ2G - comG
conditionTwo = comG*comG - 4*λ1G*λ2G
if conditionOne < 0 and conditionTwo >= 0 :
    l1 = (comG - math.sqrt(comG*comG-4*λ1G*λ2G))/(2*λ2G)
    l2 = (comG + math.sqrt(comG*comG-4*λ1G*λ2G))/(2*λ2G)
    print("1--λ1 > λ2  Vmin = {},  l1 = {},  l2 = {}".format(Vmin,l1,l2))
    v3 = []
    a = λ1G
    b = λ2G
    c = comG
    for t in range(0, 1000):
        vtmp = (a/l[t])+b*l[t]-c
        v3.append(vtmp)
    plt.plot(l, v3, label="{}".format(lable3))
else :
    print("Vmin = {} ,conditionOne = {}, conditionTwo = {},should not be here".format(Vmin,conditionOne,conditionTwo))
ax.set_title("benefit function of individual")
plt.xlabel("L")
plt.ylabel("V")
plt.xlim((1, 5))
plt.ylim((-5, 20))
plt.legend()
plt.savefig('picOne')
plt.show()

fig, ax = plt.subplots()
## λ1 < λ2, Vmin = λ1 + λ2 - com > 0
λ1G = 10   #λcS = 48 , λr = 37
λ2G = 20   #λw = 25 , λm = 5
comG = 25
lable2 = 'Vmin = λ1 + λ2 - com > 0'
Vmin = λ1G + λ2G - comG
conditionOne = λ1G + λ2G - comG
conditionTwo = comG*comG - 4*λ1G*λ2G
if conditionOne > 0  :
    print("2--λ1 < λ2,   Vmin = {}  ".format(Vmin)) 
    v2 = []
    a = λ1G
    b = λ2G
    c = comG   
    for t in range(0, 1000):
        vtmp = (a/l[t])+b*l[t]-c
        v2.append(vtmp)
    plt.plot(l, v2, label="{}".format(lable2)) 
else :
    print("Vmin = {} ,conditionOne = {}, conditionTwo = {},should not be here".format(Vmin,conditionOne,conditionTwo))
## λ1 < λ2, Vmin = λ1 + λ2 - com < 0
λ1G = 11   #λcS = 48 , λr = 37
λ2G = 15   #λw = 25 , λm = 10
comG = 30
lable1 = 'Vmin = λ1 + λ2 - com < 0'
Vmin = λ1G + λ2G - comG
conditionOne = λ1G + λ2G - comG
conditionTwo = comG*comG - 4*λ1G*λ2G
if conditionOne <= 0 and conditionTwo >= 0 :
    l1 = (comG - math.sqrt(comG*comG-4*λ1G*λ2G))/(2*λ2G)
    l2 = (comG + math.sqrt(comG*comG-4*λ1G*λ2G))/(2*λ2G)
    print("2--λ1 < λ2,  Vmin = {},  l1 = {},  l2 = {}".format(Vmin,l1,l2))
    v1 = []
    a = λ1G
    b = λ2G
    c = comG
    for t in range(0, 1000):
        vtmp = (a/l[t])+b*l[t]-c
        v1.append(vtmp)
    plt.plot(l, v1, label="{}".format(lable1))
else :
    print("Vmin = {} ,conditionOne = {}, conditionTwo = {},should not be here".format(Vmin,conditionOne,conditionTwo))

ax.set_title("benefit function of individual")
plt.xlabel("L")
plt.ylabel("V")
plt.xlim((1, 5))
plt.ylim((-5, 20))
plt.legend()
plt.savefig('picTwo')
plt.show()

fig, ax = plt.subplots()
# λ1 > 0, λ2 < 0 ;  λ1 = λcS- λr, λ2 = λw - λm
##  Vmax = λ1 + λ2 - com > 0
λ1G = 40   #λcS = 48 , λr = 8
λ2G = -10  #λw = 15 , λm = 25
comG = 3
lable1 = 'Vmax = λ1 + λ2 - com > 0'
Vmax = λ1G + λ2G - comG
conditionOne = λ1G + λ2G - comG
conditionTwo = comG*comG - 4*λ1G*λ2G
if conditionOne > 0 and conditionTwo >= 0 :
    l1 = (comG - math.sqrt(comG*comG-4*λ1G*λ2G))/(2*λ2G)
    l2 = (comG + math.sqrt(comG*comG-4*λ1G*λ2G))/(2*λ2G)
    print("3--λ1 > 0, λ2 < 0 ;  Vmax = {},  l1 = {},  l2 = {}".format(Vmax,l1,l2))
    v1 = []
    a = λ1G
    b = λ2G
    c = comG
    for t in range(0, 1000):
        vtmp = (a/l[t])+b*l[t]-c
        v1.append(vtmp)
    plt.plot(l, v1, label="{}".format(lable1))
else :
    print("Vmax = {} ,conditionOne = {}, conditionTwo = {},should not be here".format(Vmax,conditionOne,conditionTwo))
ax.set_title("benefit function of individual")
plt.xlabel("L")
plt.ylabel("V")
plt.xlim((1, 5))
plt.ylim((-5, 20))
plt.legend()
plt.savefig('picThree')
plt.show()

fig, ax = plt.subplots()
# λ1 < 0, λ2 > 0 ;  λ1 = λcS- λr, λ2 = λw - λm
##  Vmin = λ1 + λ2 - com > 0
λ1G = -10  #λcS = 15 , λr = 25
λ2G = 15   #λw = 35 , λm = 20
comG = 2
lable1 = 'Vmin = λ1 + λ2 - com > 0'
Vmin = λ1G + λ2G - comG
conditionOne = λ1G + λ2G - comG
conditionTwo = comG*comG - 4*λ1G*λ2G
if conditionOne > 0 and conditionTwo >= 0 :
    l1 = (comG - math.sqrt(comG*comG-4*λ1G*λ2G))/(2*λ2G)
    l2 = (comG + math.sqrt(comG*comG-4*λ1G*λ2G))/(2*λ2G)
    print("4--λ1 < 0, λ2 > 0 ; Vmin = {},  l1 = {},  l2 = {}".format(Vmin,l1,l2))
    v1 = []
    a = λ1G
    b = λ2G
    c = comG
    for t in range(0, 1000):
        vtmp = (a/l[t])+b*l[t]-c
        v1.append(vtmp)
    plt.plot(l, v1, label="{}".format(lable1))
else :
    print("Vmin = {} ,conditionOne = {}, conditionTwo = {},should not be here".format(Vmin,conditionOne,conditionTwo))

##  Vmin = λ1 + λ2 - com < 0
λ1G = -10  #λcS = 15 , λr = 25
λ2G = 10   #λw = 25 , λm = 15
comG = 6
lable2 = 'Vmin = λ1 + λ2 - com < 0'
Vmin = λ1G + λ2G - comG
conditionOne = λ1G + λ2G - comG
conditionTwo = comG*comG - 4*λ1G*λ2G
if conditionOne < 0 and conditionTwo >= 0 :
    l1 = (comG - math.sqrt(comG*comG-4*λ1G*λ2G))/(2*λ2G)
    l2 = (comG + math.sqrt(comG*comG-4*λ1G*λ2G))/(2*λ2G)
    print("4--λ1 < 0, λ2 > 0 ; Vmin = {},  l1 = {},  l2 = {}".format(Vmin,l1,l2))
    v2 = []
    a = λ1G
    b = λ2G
    c = comG
    for t in range(0, 1000):
        vtmp = (a/l[t])+b*l[t]-c
        v2.append(vtmp)
    plt.plot(l, v2, label="{}".format(lable2))
else :
    print("Vmin = {} ,conditionOne = {}, conditionTwo = {},should not be here".format(Vmin,conditionOne,conditionTwo))
ax.set_title("benefit function of individual")
plt.xlabel("L")
plt.ylabel("V")
plt.xlim((1, 5))
plt.ylim((-5, 20))
plt.legend()
plt.savefig('picFour')
plt.show()

fig, ax = plt.subplots()
# λ1 = 0 or λ2 = 0 ;  λ1 = λcS- λr, λ2 = λw - λm
##λ1 = 0 , λ2 > 0, Vmin =  λ2 - com > 0
λ1G = 0   #λcS = 15 , λr = 15
λ2G = 13  #λw = 25 , λm = 12
comG = 10
lable1 = 'λ1 = 0 , λ2 > 0, Vmin  =  λ2 - com > 0'
Vmin = λ2G - comG
conditionOne = λ2G - comG
if conditionOne > 0  :
    l2 = comG / λ2G
    print("5--λ1 = 0 , λ2 > 0 ;  Vmin = {},    l2 = {}".format(Vmin, l2))
    v1 = []
    a = λ1G
    b = λ2G
    c = comG
    for t in range(0, 1000):
        vtmp = (a/l[t])+b*l[t]-c
        v1.append(vtmp)
    plt.plot(l, v1, label="{}".format(lable1))
else :
    print(" Vmin = {} ,conditionOne = {},  should not be here".format(Vmin,conditionOne))

##λ1 > 0 , λ2 = 0, Vmax =  λ2 - com > 0
λ1G = 30  #λcS = 48 , λr = 18
λ2G = 0   #λw = 15 , λm = 15
comG = 10
lable2 = 'λ1 > 0 , λ2 = 0, Vmax =  λ1 - com > 0'
Vmax = λ1G - comG
conditionOne = λ1G - comG
if conditionOne > 0  :
    l2 = λ1G / comG
    print("5--λ1 > 0 , λ2 = 0, Vmax =  λ1 - com > 0  Vmax = {},    l2 = {}".format(Vmax, l2))
    v2 = []
    a = λ1G
    b = λ2G
    c = comG
    for t in range(0, 1000):
        vtmp = (a/l[t])+b*l[t]-c
        v2.append(vtmp)
    plt.plot(l, v2, label="{}".format(lable2))
else :
    print("Vmin = {} ,conditionOne = {},  should not be here".format(Vmin,conditionOne))
ax.set_title("benefit function of individual")
plt.xlabel("L")
plt.ylabel("V")
plt.xlim((1, 5))
plt.ylim((-5, 20))
plt.legend()
plt.savefig('picFive')
plt.show()



