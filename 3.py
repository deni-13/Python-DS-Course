#stringler
"""

a="merhaba"
print(3*a )

b="ali"
print(b*9)



y="alininyeri"
print(y.split())


#slicing
a="1233456789"

print(a[1:2]) #1den 2 ya kadar say
print(a[::3]) #3er atla
print(a[:3])  #baslangıc slice : ---> bitis slice 3 e kadar say
print(a[3:])  #3.den basla sonuna kadar say 





#list methods

a="matematik"
print(a.upper())


c="fizik,analiz"
b=c.split()
print(c)

""" 
#kosul ifadeleri
"""
if 3<1:
    print("yanlıs")
else:
    print("yanlıs")


"""

#if elif else kontrol yapıları
"""
x=5
y=9


if x>y:
    print("buyuk")
elif x<y:
    print("kucuk")
else:
    print("esit")
"""
#--------------------------------------

"""
a=10
b=20
c=30

if a>b and b>c :
    print("a bden büyük ve b de cden büyük")
elif a<b and b<c :
    print("a bden kucuk b cden kucuk")
else:
    print("diger")


"""
str="istanbul"
if "i" in str:
    print("var")
else:
    print("yok kanka")

    #string te if koontrolu


lis=[1,2,34,5,7,8]

if 65 in lis:
    print("65 vardir")
else:
    print("no")

#--for donguleri--------------------

#ikiye bolunup bolunemdigi

listem=[12,454,57,789]


for i in listem:
    if i%2==0:
        print(i)
    else:
        print("tek sayılar",i)

"""
#break continue

listem=[12,454,57,789]


for i in listem:
    if i%2==0:
        break
    else:
        print("tek")

"""

"""
x= 0
while x<10:
    print("merhaba")
    x+=1
"""

#------------------

#random
from random import randint

a=randint(0,7)
print(a)


#range -->
for i in range(0,90):
    if i%3==0:
        print(i)