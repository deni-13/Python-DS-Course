def yeni(*args): #parametre syısı 
    return sum(args)

yeni(642,33)
#lambdayla tek satırda fonk yazmak
carpma= lambda a : a*a
carpma(7)

#stringteki harfin tespiti
def p(string):
    return "a" in string

p("ahmet")


#hata yakalama--------------------

#hata ayıklama
def hesaplama(x,y,isl):
    
    if not isl in "+-/*":
        return "istenenleri gir"
    
    if isl=="+":
        return( str(x) + "+"  + str(y) + "=" +str(x+y))
    
    elif isl =="-":
         return( str(x)+ "-" + str(y) + "=" +str(x-y))

    elif isl=="*":
         return( str(x)+ "*"  + str(y) + "=" +str(x*y))

    elif isl=="/":
         return( str(x) +"/"  + str(y) + "=" +str(x/y))
while True:
    try:

        x=int(input("ilk sayıyı gir---->"))
        y=int(input("sonraki sayıyı gir---->"))

        isl =input("islemini sec +-/*")


        print(hesaplama(x,y,isl))
    except:
        print("sayıları düzgün gir")

        