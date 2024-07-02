text = input("Enter your message: ")
shift = 0
while not 1 <= shift <= 25:
    shift = int(input("Enter shift number: "))
    if not 1 <= shift <= 25:
        print("Input number is not withing the range from 1 to 25, please try again.")
cipher = ''
for char in text:
        if not char.isalpha():
            cipher += char  
        if 65 <= ord(char) <= 90:
            if (ord(char) + shift) > 90:
                code = ord(char) + shift - 26
                cipher += chr(code)
                code = 0
            if (ord(char) + shift) <= 90:
                code = ord(char) + shift
                cipher += chr(code) 
                code = 0
        if 97 <= ord(char) <= 122:
            if (ord(char) + shift) > 122:
                code = ord(char) + shift - 26
                cipher += chr(code)
                code = 0
            if (ord(char) + shift) <= 122:
                code = ord(char) + shift
                cipher += chr(code)
                code = 0                      
print(cipher)