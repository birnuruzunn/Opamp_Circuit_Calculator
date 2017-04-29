# -*- coding: utf-8 -*-

def integralAlici():

    """I1 = (Vi1-Vx)/R1 = Vi1/R1 dir.(Vx = = olduğu için)
        x noktasındaki akımlar için düğüm denklemini yazacak olursak, KCL den;
        If-I1 = 0 ise If = I1 ve bu durumda If = Vi1/R1 olur.
        Vout = -(1/Cf)*[t-0 aralığında integral(If*dt)] = -(1/Cf)*[t-0 aralığında integral((Vi1/R1)*dt)] olur.
        Bunun sonucu olarak da;
        Vout = -(1/R1*Cf)*[t-0 aralığında integral(Vi1*dt)] bulunur. """

    Vi1= int(input("vi1 değeri giriniz:"))
    t = int(input("bir zaman aralığı giriniz:"))
    R1 = 1000
    Rf = 16000
    Cf = 1/1000

    I1 = Vi1/R1
    If = I1

    i = 0
    toplam = 0.0
    for i in range(0,t):
        toplam = toplam+Vi1*t

    Vout = -(1/(R1*Cf))*toplam

    kazanç = 1/(R1*Cf)

    print("""Vi1:{} , I1:{} , Vout:{} ve devre kazancı:{}""".format(Vi1,I1,Vout,kazanç))

integralAlici()