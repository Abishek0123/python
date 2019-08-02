p=int(input(""))
if p > 1:
    for i in range(2, p):
        if (p % i) == 0:
            print("no")
            break
    else:
        print("yes")
else:
    print("no")
