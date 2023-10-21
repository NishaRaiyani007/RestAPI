d1 = {'item': 'item1', 'amount': 400}

d2 = {'item': 'item2', 'amount':300}
d3 = {'item': 'item1', 'amount': 750}

for i, j in d1.items():

    for x, y in d3.items():

        if i == x:

            d3[i]=(j+y)

print(d3)
