# -*- coding: utf-8 -*-
from sympy import *
""" I1 = (V1-Vx)/R1
    I2 = (V2-Vx)/R2
    I3 = (V3-Vx)/R3
    I3 = (Vx-Vout)/R3 ve buradaki Vx = 0 olduğu için;

    I1 = V1/R1
    I2 = V2/R2
    I3 = V3/R3
    If = -(Vout/Rf) diyebiliriz. Bu durumda KCL den If = -(I1 + I2 + I3) olacağına göre;

    -(Vout/R3) = V1/R1 + V2/R2 + V3/R3 ve buradan da

    Vout = -((Rf/R1)*V1 + (Rf/R2)*V2 + (Rf/R3)*V3) bulunur. """

def toplayici():
    Vin1, Vin2, Vin3, Vout= symbols('V1, V2, V3, Vout')
    R1, R2, R3, Rf =  symbols('R1, R2, R3, Rf')
    I1, I2, I3, If = symbols('I1, I2, I3, If')

    i1 = simplify(Vin1/R1)
    I1.equals(i1)
    i2 = simplify(Vin2/R2)
    i2.equals(i2)
    i3 = simplify(Vin3/R3)
    i3.equals(i3)
    if_ = simplify(-(Vout/Rf))
    if_.equals(if_)

    Vout = expand(-((Rf/R1)*Vin1 + (Rf/R2)*Vin2 + (Rf/R3)*Vin3))
    print("Vout = {}\n I1 = {}\n I2 = {}\n I3 = {}\n If = {}\n".format(Vout, i1, i2, i3, if_) )

toplayici()