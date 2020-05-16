#The Beginning of Everything

test_case = int(input())

for i in range(test_case):
    s = str(input())
    a = "ldrwolloeh"
    #a = "".join(sorted(a))

    if("".join(sorted(s)) == "".join(sorted(a))):
            print("Yes\n")
    else:
        print("No\n")
