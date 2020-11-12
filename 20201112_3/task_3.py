while True:
    s = input()
    try:
        n = float(s)
    except:
        print("Try again")
    else:
        break
print(n)

