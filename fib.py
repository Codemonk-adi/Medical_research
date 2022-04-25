from re import X


for i in range(8):
    x,y,z = i>>2,(i%4)>>1,i%2
    print(f"{x},{y},{z},{(x|y)&~z}")