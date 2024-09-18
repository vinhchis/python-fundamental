relative_path = "./acronyms.txt"
absolute_path = "/home/vinhchis/Documents/fpt-aptech/Semester/Seme-III/3.PYTHON/sourse/7.working-with-files/acronyms.txt"

look_up = input('What is acronym would you like to look up?\n')
found = False

with open(absolute_path, 'r', encoding="utf-8") as f: 
   for line in f:
       if look_up in line:
            print(line)
            found = True
            break


if not found:
    print('It not existed!!')