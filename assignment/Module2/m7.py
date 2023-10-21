s= input("Enter a string: ")

if len(s) < 2:
    ans = "Empty string"
else:
    ans=s[:2] + s[-2:]

print("Result:",ans)
