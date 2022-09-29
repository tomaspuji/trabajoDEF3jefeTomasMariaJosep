#cambio de prueba de maria
print("Enter the Binary Number: ", end="")
bnum = int(input())

h = 0
m = 1
chk = 1
i = 0
hnum = []
while bnum!=0:
    rem = bnum%10
    h = h + (rem*m)
    if chk%4==0:
        if h<10:
            hnum.insert(i, chr(h+48))
        else:
            hnum.insert(i, chr(h+55))
        m = 1
        h = 0
        chk = 1
        i = i+1
    else:
        m = m*2
        chk = chk+1
    bnum = int(bnum/10)

if chk!=1:
    hnum.insert(i, chr(h+48))
if chk==1:
    i = i-1

print("\nEquivalent Hexadecimal Value = ", end="")
while i>=0:
    print(end=hnum[i])
    i = i-1
print()