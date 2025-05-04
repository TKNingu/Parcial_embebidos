import array
import struct
from machine import mem32

print("Ingrese el número de puntos (N):")
N = int(input())  

def float_to_u32(f): return struct.unpack('<I', struct.pack('<f', f))[0]

def u32_to_float(u): return struct.unpack('<f', struct.pack('<I', u))[0]

direcciones = [0x20000000, 0x20000008, 0x20000010, 0x20000018]  
dir_curva = 0x20001000  

print("Ingrese las 4 coordenadas (x y) de los puntos de control:")
P = []  
for i in range(4):
    while True:
        try:
            xs, ys = input(f"P{i} (x y): ").split()
            P.append((float(xs), float(ys)))
            break
        except ValueError:
            print("Error: ingrese dos números separados por espacio.")

for idx, (x, y) in enumerate(P):
    base = direcciones[idx]
    mem32[base]     = float_to_u32(x)
    mem32[base + 4] = float_to_u32(y)

LR = array.array('f', [0.0] * (2 * N))

def lista_retornada():  # Renombrada función de cálculo
    if N <= 0:
        return
    for i in range(N):
        t = i / (N - 1) if N > 1 else 0.0
        u = 1 - t
        xs = [u32_to_float(mem32[d]) for d in direcciones]
        ys = [u32_to_float(mem32[d+4]) for d in direcciones]
        b0, b1, b2, b3 = u**3, 3*u**2*t, 3*u*t**2, t**3
        x = b0*xs[0] + b1*xs[1] + b2*xs[2] + b3*xs[3]
        y = b0*ys[0] + b1*ys[1] + b2*ys[2] + b3*ys[3]
        LR[2*i], LR[2*i+1] = x, y
        b_lr = dir_curva + i*8
        mem32[b_lr]     = float_to_u32(x)
        mem32[b_lr + 4] = float_to_u32(y)


lista_retornada()

print("\nPuntos calculados:")
for i in range(N):
    print(f"P{i}: ({LR[2*i]:.2f}, {LR[2*i+1]:.2f})")




