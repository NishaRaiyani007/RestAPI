a=[]
n= int(input("Enter the number of elements in list:"))

for i in range(0,n):
   element=input("Enter element" + str(i+1) + ":")
a.append(element)
max1=len(a[0])
temp=a[0]
for j in a:
  if(len(j)>max1):
      max1=len(j)
temp=j
print("The word with the longest length is:")
print(temp)
