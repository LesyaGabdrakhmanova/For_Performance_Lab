import sys
Massiv_Nums = []
with open (sys.argv[1]) as file:
    for line in file:
        try:
            a = int(line)
            Massiv_Nums.append(int(line.rstrip('\n')))
        except ValueError:
            sys.exit()
if len(Massiv_Nums)>1:
    A = (sorted(Massiv_Nums)[len(Massiv_Nums) // 2])
    print(sum(abs(i - A) for i in Massiv_Nums))
else:
    sys.exit()