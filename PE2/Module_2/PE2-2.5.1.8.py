text_1 = input("Enter your text 1: ")
text_2 = input("Enter your text 2: ")

new_text_1 = ""
for char1 in text_1:
    if char1 == " ":
        continue
    else:
        new_text_1 += char1
new_text_1 = new_text_1.lower()
new_list_1 = list(new_text_1)

new_text_2 = ""
for char2 in text_2:
    if char2 == " ":
        continue
    else:
        new_text_2 += char2
new_text_2 = new_text_2.lower()
new_list_2 = list(new_text_2)


if text_1 != "" and text_2 != "" and sorted(new_list_1) == sorted(new_list_2):
    print("Anagrams")
else:
    print("Not anagrams")
