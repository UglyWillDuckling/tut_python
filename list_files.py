import re
# import OS module
import os
 
# Get the list of all files and directories
path = input("Give me the path: ") 
dir_list = os.listdir(path)
 
print("Files and directories in'", path, "':")
 
# prints all files
#print(dir_list)

# Rename the files according to regex

for fname in dir_list:
    file_path = path + "/" + fname
    new_name = re.sub("\.?(1080p.*|720p.*)", "", fname)
    new_path = path + "/" + new_name
    print(new_path)
    os.rename(file_path, new_path)
