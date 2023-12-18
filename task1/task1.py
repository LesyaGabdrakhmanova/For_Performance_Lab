import sys
Massiv=[]
A = 1
with open (sys.argv[1]) as file:
    for line in file:
        if line.rstrip('\n').isdigit():
            Massiv.append (int(line.rstrip('\n')))
        else:
            sys.exit()
    if len(Massiv) == 2 and Massiv[0]>0 and Massiv[1]>0:
        while True:
            print(A, end='')
            A = 1 + (A + Massiv[1] - 2) % Massiv[0]
            if A == 1:
                break
    else:
        sys.exit()