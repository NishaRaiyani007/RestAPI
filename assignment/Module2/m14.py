s1 = input("Enter a String : ")

if len(s1) >= 3:
    if s1.endswith("ing"):
        s2 = s1 + "ly"
    else:
        s2 = s1 + "ing"
else:
    s2 = s1

print("Modified String :", s2)
