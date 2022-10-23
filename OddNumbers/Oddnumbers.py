lower_limit=int(input("Indtast nedre grænse: "))
upper_limit=int(input("Indtast øvre grænse: "))

for i in range(lower_limit, upper_limit + 1):
    if(i % 2 != 0):
        print(i)
