import shutil
import os

n=int(input("Folder you want to create: "))
l = list(range(n))
list_string = map(str, l)
# path where you want to create folders
parent_dir = r"C:\Users\Krishna\Downloads\folder_split\\"
for i in list_string:
    path = os.path.join(parent_dir, i)
    os.makedirs(path)
    print(f"Folder {i} created")

# path of folder containing files
dir_path = r'C:\Users\Krishna\Downloads\folder_split\new\\'
files = os.listdir(dir_path)
count = 0

for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        count += 1
print('Total Files:', count)


for k in l:
    for f in files[count//n*k:count//n*(k+1)]:
        shutil.move(dir_path + f, parent_dir+ f"{k}")

