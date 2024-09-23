path = "`acronyms.txt"

look_up = input('What is acronym would you like to look up?\n')
found = False

with open(path, 'r', encoding="utf-8") as f: 
   for line in f:
       if look_up in line:
            print(line)
            found = True
            break


if not found:
    print('It not existed!!')