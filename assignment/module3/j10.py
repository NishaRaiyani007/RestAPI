num = [ 2,4,56,78,4,34,5,8,9]
duplicate = set()
uniq = []
for l in num:
  if l not in duplicate:
    uniq.append(l)
    duplicate.add(l)
uniq.sort()    
print(  uniq[1]   )
