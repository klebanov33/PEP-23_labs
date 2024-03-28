blocks = int(input("Enter the number of blocks: "))
height = 0
used_bloks_on_level = 0
sum_of_bloks = 0
remain_bloks = 0
while blocks - sum_of_bloks > 0:
    height = height + 1
    used_bloks_on_level = used_bloks_on_level + 1
    sum_of_bloks = sum_of_bloks + used_bloks_on_level
    remain_bloks = blocks - sum_of_bloks
    if remain_bloks < used_bloks_on_level + 1:
        break
print("The height of the pyramid:", height)