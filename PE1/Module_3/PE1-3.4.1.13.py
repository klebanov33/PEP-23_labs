# step 1
beatles = []
print("Step 1:", beatles)
# step 2
beatles.append("Джон Леннон")
beatles.append("Пол Маккартни")
beatles.append("Джордж Харрисон")
print("Step 2:", beatles)
# step 3
for i in ("Стью Сатклифф","Пит Беста"):
    beatles.append(i)
print("Step 3:", beatles)
# step 4    
del beatles[4]
del beatles[3]
print("Step 4:", beatles)
# step 5
beatles.insert(0,"Ринго Старр")
print("Step 5:", beatles)
# testing list legth
print("\nThe Fab", len(beatles))