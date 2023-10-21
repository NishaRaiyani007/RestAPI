s= "welcome to python"
words = s.split()  
short_word = words[0]  
for word in words:
    if len(word) < len(short_word):
        short_word = word
print("Shortest word:", short_word)  
