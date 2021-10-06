import os

path = "C:/Users/ASUS/Documents/GitHub/my-portfolio/friends_assets"

file_list = os.listdir(path)

for index, file in enumerate(file_list):
    os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(index+1), '.jpg'])))