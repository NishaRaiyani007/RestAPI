s=0
l=['abc','jalpa','123','vikas','555']
for i in l:
    if len(i)>1 and i[0]==i[-1]:
        print("given words :",i)
        s=s+1
print("no.of words:",s)

