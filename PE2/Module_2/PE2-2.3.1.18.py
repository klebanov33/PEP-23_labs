def mysplit(strng):
    new_list = []
    a = ""
    for ch in strng:
        if ch != "" and ch != " ":
            a += ch
        if ch == " " and a != "":
            new_list.append(a)
            a = ""
        else:
            continue
    return new_list


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))


### OUTPUT ###

'''
['To', 'be', 'or', 'not', 'to', 'be,', 'that', 'is', 'the']
['To', 'be', 'or', 'not', 'to', 'be,that', 'is', 'the']
[]
['abc']
[]
'''
