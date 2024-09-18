absolute_path = "/home/vinhchis/Documents/fpt-aptech/Semester/Seme-III/3.PYTHON/sourse/7.working-with-files/acronyms.txt"

acronym = input('What acronyms do you want to add?\n')
definition = input('What is definition?\n')

with open(absolute_path, 'a') as f:
    f.write(acronym + ' - ' + definition + '\n')