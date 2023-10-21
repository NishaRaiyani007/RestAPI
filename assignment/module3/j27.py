d1={"name":"ram" , "age":23}
d2={"city": "baroda", "gender": "female"}
d3={"mark":450}
d4 = {}
for d in (d1, d2, d3): d4.update(d)
print(d4)
