import os
path = "F:/QUAX/Days"
folders = os.listdir(path)

for folder in folders:
    day,month,year = folder.split(".")
    nFolder = year+"."+month+"."+day
    print(nFolder)
    os.rename(path+"/"+folder,path+"/"+nFolder)