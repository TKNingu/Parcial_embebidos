import array
import math
from machine import mem32

N = 0; Xn = 2; a=0;b=0;c=0;d=0;e=0;f=0;g=0;h=0;
print('Ingrese valores de P0,P1,P2 y P3',a,b,c,d,e,f,g,h);

P[0] = array.array('l', [a, b])
dir1 = mem32(P[0])
P[1] = array.array('l', [c, d])
dir2 = mem32(P[0] & 0x4)
P[2] = array.array('l', [e, f])
dir3 = mem32(P[0] & 0x8)
P[3] = array.array('l', [g, h])   # dir4 = mem32(cod4 0x12)
dir4 = mem32(P[0] & 0x12)
LR = [0]*N

def lista_retornada():
    for i in range(N):
        t = i / M
        if (t == 0):
            LR[i] = (1 - t)*(1-t) * P0[0] + LR[i]
        if (t == 1):
            LR[i] = t ** N-1 * 0.3 + LR[i]
    LR[M] = (1 - t) * (3 - t) * t ** 2 * 0.6 * c * t * P[Xn] + LR[i]
    
    if (Xn == 3):
        Xn = 2

    Xa = Xn + 1
    print(LR[M])
