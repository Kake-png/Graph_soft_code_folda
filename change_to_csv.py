import os

def chenge_to_csv(filename, file_path, newfile_path):
    os.chdir(file_path)
    changedfile = replace_colon(filename)
    os.chdir(newfile_path)
    newfilename = write_to_csv(filename, changedfile)
    return newfilename

def replace_colon(filename):
    changedfile = []
    with open (filename) as file:
        for line in file:
            newline = line.replace(":",",")
            changedfile.append(newline)
    return changedfile

def write_to_csv(filename, newfile):
    newfilename = filename.replace("txt","csv")
    with open (newfilename, mode="w") as file:
        for line in newfile:
            file.write(line+"\n")
    return newfilename

#chenge_to_csv("a.csv") 
