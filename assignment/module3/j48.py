num = int(input("enter the num :"))
d= [1]
for i in range(2, num):
	if (num % i)==0:
		d.append(i)
print("sum of all divisor:",sum(d))
