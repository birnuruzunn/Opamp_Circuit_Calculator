# -*- coding: utf-8 -*-

def toplayici():
    """ I1 = (V1-Vx)/R1
        I2 = (V2-Vx)/R2
        I3 = (V3-Vx)/R3
        I3 = (Vx-Vout)/R3 ve buradaki Vx = 0 olduğu için;

        I1 = V1/R1
        I2 = V2/R2
        I3 = V3/R3
        I3 = -(Vout/R3) diyebiliriz. Bu durumda KCL den If = -(I1 + I2 + I3) olacağına göre;

        -(Vout/R3) = V1/R1 + V2/R2 + V3/R3 ve buradan da

        Vout = -((Rf/R1)*V1 + (Rf/R2)*V2 + (Rf/R3)*V3) bulunur. """

    Vi1 = int(input("vi1 değeri giriniz:"))
    Vi2 = int(input("vi2 değeri giriniz:"))
    Vi3 = int(input("vi3 değeri giriniz:"))

    Ri = [4000, 2000, 1000]
    Rf = 16000

    Vout = -((Rf/Ri[0])*Vi1 + (Rf/Ri[1])*Vi2 + (Rf/Ri[2])*Vi3)

    I1 = Vi1 / Ri[0]
    I2 = Vi2 / Ri[1]
    I3 = Vi3 / Ri[2]

    If = -(Vout / Rf)

    print("""Vi1:{} Vi2:{} Vi3:{} Vout:{}\n
          I1:{} I2:{} I3:{} If:{}""".format(Vi1,Vi2,Vi3,Vout,I1,I2,I3,If))

toplayici()