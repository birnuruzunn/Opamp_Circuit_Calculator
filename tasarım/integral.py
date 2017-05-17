# -*- coding: utf-8 -*-
from sympy import *
import denemeler as dnm

t = dnm.Ui_mainWindow(object)
t.setupUi()
""" I1 = (Vi1-Vx)/R1 = Vi1/R1 dir.(Vx = 0 olduğu için)
    x noktasındaki akımlar için düğüm denklemini yazacak olursak, KCL den;
    If-I1 = 0 ise If = I1 ve bu durumda If = Vi1/R1 olur.
    Vout = -(1/Cf)*[t-0 aralığında integral(If*dt)] = -(1/Cf)*[t-0 aralığında integral((Vi1/R1)*dt)] olur.
    Bunun sonucu olarak da;

    Vout = -(1/R1*Cf)*[t-0] aralığında integral(Vi1*dt)] bulunur. """

def integral():

   Vin1 = symbols('V1')
   R1 = symbols('R1')
   I1, If = symbols('I1, If')
   Cf = symbols('Cf')

   i1 = (t.setupUi().lineEdit().text())*simplify(Vin1/R1)
   i1.equals(I1)

   if_= (t.setupUi().lineEdit().text())*simplify(Vin1/R1)
   if_.equals(If)

   Vout = expand(-(1/(R1*Cf))*Integral((t.setupUi().lineEdit().text())*Vin1,((t.setupUi().lineEdit().text())*Vin1, 0, 1))) # 0-1 aralığında integral hesabı yaptım

   kazanc = (t.setupUi().lineEdit().text())*simplify(1/(R1*Cf))

   print("Vout = {}\n I1 = {}\n If = {}\n devre kazancı = {}".format(Vout,i1,if_,kazanc))

integral()
