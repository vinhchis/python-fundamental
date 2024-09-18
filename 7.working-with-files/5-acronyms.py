absolute_path = "/home/vinhchis/Documents/fpt-aptech/Semester/Seme-III/3.PYTHON/sourse/7.working-with-files/acronymsa.txt"


def add():
    acronym = input('What acronyms do you want to add?\n')
    definition = input('What is definition?\n')

    with open(absolute_path, 'a') as f:
        f.write(acronym + ' - ' + definition + '\n')


def lookup():
    look_up = input('What is acronym would you like to look up?\n')
    found = False

    try:
        with open(absolute_path, 'r', encoding="utf-8") as f:
            for line in f:
                if look_up in line:
                    print(line)
                    found = True
                    break
    except FileNotFoundError as e:
        print('Find Not Found')
        return

    if not found:
        print('It not existed!!')


def main():
    choice = ''
    while (choice != 'F' and choice != 'A'):
        choice = input('Do you want to find(F) or add (A) a acronym?\n')
        if choice == 'F':
            lookup()
        elif choice == 'A':
            add()
        else:
            print('Please choice again!!!')


main()
