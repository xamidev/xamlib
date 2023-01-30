from maths.constants import pi

#pi = (factorial.factorial(6*k)*(13591409+545140134*k))/(factorial.factorial(3*k)*(factorial.factorial(k)**3)*(-640320)**(3*k))

print("Approximating Pi...")

n=1000000000
k=1
s=0
for i in range(n):
    if i % 2 == 0: s += 4/k
    else: s -= 4/k
    k += 2

    if i % 100000 == 0:
        accuracy = round(abs(s/pi)*100, 12)
        print(f"pi={round(s,12)} accuracy={accuracy}% iteration={round(i,12)}", end='\r')
print(f"pi={s} accuracy={accuracy}% iteration={i}")