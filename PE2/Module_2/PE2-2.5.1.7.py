text = input("Enter your text: ")
new_text = ""
for char in text:
    if char == " ":
        continue
    else:
        new_text += char
new_text = new_text.lower()
new_list = list(new_text)
n = len(new_list)
N = n//2
a = ''
b = ''

for i in range(N):
    a += new_list[i]
for j in range(N):
    b += new_list[-(1+j)] 

if new_text.isalpha() and a == b:
    print("It's a palindrome")
else:
    print("It's not a palindrome")
