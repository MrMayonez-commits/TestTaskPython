import numpy as np

center1 =0                       # float(input())
center2 =0                       # float(input())
center3 =0                      # float(input())
radius  =10                   #float(input())
line1x  =-100                      #float(input())
line1y  =-100                       #float(input())
line1z  =0                      #float(input())
line2x  =100                     #float(input())
line2y  =100             #float(input())
line2z  =0               #float(input())
a = 0
diapmax = max(radius,line1x,line1y,line1z,line2x,line2y,line2z)
diapmin = min(radius,line1x,line1y,line1z,line2x,line2y,line2z)
for x in np.arange(diapmin, diapmax , 0.1):
    #print(x)
    Y = ((((( x - line1x ) / ( line2x - line1x ))) * ( line2y - line1y)) + line1y)
    #print(x,Y)
    Z =  (( x - line1x ) / ( line2x - line1x )) * ( line2z - line1z) + line1z
    znach = ( x * x + Y * Y + Z * Z ) ** ( 1 / 2 )
    radmin = radius * 0.99
    radmax = radius * 1.01
    #print(x, Y, Z)
    #if znach == radius:
    if (znach < radmax) and (znach > radmin):
        print(x,Y,Z)
        a = 1
if a != 1:
    print("Коллизий не найдено")