import os
os.chdir("../fileset_folda")

def chenge_to_csv(filename):
    changedfile = replace_colon(filename)
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
