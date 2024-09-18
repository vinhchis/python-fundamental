import os

folder_original = '/home/vinhchis/Documents/arch-linux'
folder_destination = '/home/vinhchis/Documents/fpt-aptech/Semester/Seme-III/3.PYTHON/sourse/7.working-with-files/CleanUP/'

os.mkdir(folder_destination)

for entry in os.scandir(folder_original):
    location_origin = os.path.join(folder_original,entry.name)
    location_destination = os.path.join(folder_destination, entry.name)

    if os.path.isfile(entry):
        os.rename(location_origin, location_destination)