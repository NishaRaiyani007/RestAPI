def line_count():
    file = open("tops.txt","r")
    count=0
    for line in file:
        if line[0] not in 'p':
            count+= 1
    file.close()
    print("lines not starting with 'p'=",count)

line_count()
