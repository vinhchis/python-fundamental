absolute_path = "acronyms.txt"

acronym = input('What acronyms do you want to add?\n')
definition = input('What is definition?\n')

with open(absolute_path, 'a') as f:
    f.write(acronym + ' - ' + definition + '\n')