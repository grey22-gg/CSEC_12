from fractions import Fraction
y, w = map(int, input().split())
z = []
if y > w:
    for i in range(y, 7):
        z.append(i)
elif w > y:
    for i in range(w, 7):
        z.append(i)
else:  
    for i in range(w, 7):
        z.append(i)
a = len(z)
k = Fraction(a, 6)
if k == 0:
 print("0/1")
elif k == 1:
 print("1/1")
else:
 print(k)
