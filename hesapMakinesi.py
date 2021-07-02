def hesaplama(x,y,isl):
    if isl=="+":
        return( str(x) + "+"  + str(y) + "=" +str(x+y))
    
    elif isl =="-":
         return( str(x)+ "-" + str(y) + "=" +str(x-y))

    elif isl=="*":
         return( str(x)+ "*"  + str(y) + "=" +str(x*y))

    elif isl=="/":
         return( str(x) +"/"  + str(y) + "=" +str(x/y))
        
x=int(input("ilk sayıyı gir"))
y=int(input("sonraki sayıyı gir"))

isl =input("islemini sec +-/*")


hesaplama(x,y,isl)

