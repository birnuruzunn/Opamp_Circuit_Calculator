# -*- coding: utf-8 -*-
from sympy import *

""" I1 = (Vi1-Vx)/R1 = Vi1/R1 dir.(Vx = 0 olduğu için)
    x noktasındaki akımlar için düğüm denklemini yazacak olursak, KCL den;
    If-I1 = 0 ise If = I1 ve bu durumda If = Vi1/R1 olur.
    Vout = -(1/Cf)*[t-0 aralığında integral(If*dt)] = -(1/Cf)*[t-0 aralığında integral((Vi1/R1)*dt)] olur.
    Bunun sonucu olarak da;

    Vout = -(1/R1*Cf)*[t-0] aralığında integral(Vi1*dt)] bulunur. """

def integral():

   V = symbols('V')
   R = symbols('R')
   I, If = symbols('I, If')
   C = symbols('C')

   i =simplify(V/R)
   i.equals(I)

   if_= simplify(V/R)
   if_.equals(If)

   Vout = -(1/(R*C))*Integral((V,(V, 0, 1))) # 0-1 aralığında integral hesabı yaptım

   kazanc = simplify(1/(R*C))

   return kazanc