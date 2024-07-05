def readint(prompt, min, max):
    try:
        N = int(input(prompt))
        assert min <= N <= max
    except ValueError:
        print("Error: wrong input")
        N = int(input(prompt))
    except AssertionError:
        print("Error: the value is not within permitted range (" + str(min) + ".." + str(max) + ")")
        N = int(input(prompt))
    return N

v = readint("Enter a number from -10 to 10: ", -10, 20)

print("The number is:", v)