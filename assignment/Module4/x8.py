file = open('file.txt', 'r')
r= file.read()
p = r.split()

print('words:', len(p))
