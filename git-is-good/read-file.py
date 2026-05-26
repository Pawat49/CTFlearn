count = 0
zero = 0
one = 0
with open('data.dat','r') as file:
    content = file.read()

    for line in content:
        if line == '\n':

            if zero % 3 == 0 or one % 2 == 0:

                count += 1
                
            zero = 0
            one = 0
        
        if line == '0':
            zero += 1
        elif line == '1':
            one += 1

    print(count)

    file.close()
