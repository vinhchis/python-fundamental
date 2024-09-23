import os

folder = "D:/code/github.com/vinhchis\python-fundamental/7.working-with-files"
entries = os.scandir(folder)

# for entry in entries:
#     print(entry.name)


for entry in entries:
    if os.path.isfile(entry):
        print("File:",entry.name)
    if os.path.isdir(entry):
        print("Subdirectory:", entry.name)