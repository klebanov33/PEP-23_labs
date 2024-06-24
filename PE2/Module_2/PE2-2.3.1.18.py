def mysplit(strng):
    new_list = []
    splited_word = ""
    count_symbol = 0
    for ch in strng:
        count_symbol += 1
        if ch != "" and ch != " ":
            splited_word += ch
        if (count_symbol == len(strng)) and splited_word != "":
            new_list.append(splited_word)
            splited_word = ""
        if (count_symbol == len(strng)) and splited_word == "":    
            break
        if ch == " " and splited_word != "":
            new_list.append(splited_word)
            splited_word = ""
        if ch == " " and splited_word == "":
            continue
    return new_list

### TEST ###

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))

### OUTPUT ###

'''
['To', 'be', 'or', 'not', 'to', 'be,', 'that', 'is', 'the', 'question']
['To', 'be', 'or', 'not', 'to', 'be,that', 'is', 'the', 'question']
[]
['abc']
[]
'''
