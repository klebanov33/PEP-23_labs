text_1 = input("Enter your text 1: ")
text_2 = input("Enter your text 2: ")    
new_word = ''
p = 0
for char in text_1:
    a = text_2.find(char, p)
    if a != -1:
        new_word += char
        p = a + 1
if new_word == text_1:
    print("Yes")
else:
    print("No")