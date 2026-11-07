#-------------------------------------------------------------------------------------------------------
# Discriminant
#-------------------------------------------------------------------------------------------------------
import numpy as np

a=float(input("Rentrer la valeur de a: "))
b=float(input("Rentrer la valeur de b: "))
c=float(input("Rentrer la valeur de c: "))
print("a =",a, "b =",b, "c =",c)

#delta : b.carré - 4 ac

Delta=b**2-(4*a*c)
print("Delta =", Delta)

#solutions#

if Delta<0:
    print("Le polynôme n'a pas de solutions réelles")

if Delta==0:
    s=-b/(2*a)
    print("La seule solution est s = ",round(s,4))

if Delta>0:
    s1=(-b-np.sqrt(Delta))/(2*a)
    s2=(-b+np.sqrt(Delta))/(2*a)
    print("s1 = ",round(s1,4))
    print("s2 = ",round(s2,4))

