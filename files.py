import os

def getNameFromDir(dirName, fileName):
   file = open(fileName, "w")
   for root, dirs, files in os.walk(dirName, topdown=False):
      #print(root)
      directory = os.getcwd() + "/" + root + "/"

      print(directory)
      for name in files:
         #check if keyword is in name
         ## this was used to distinguish between two different directories
         ## boths directories shared similar names but with different naming and extensions
         if ".mkv" in name:
            #file.write(os.path.join(root, name)[42:])
            #For videos with pattern "Tom & Jerry (1940) - S03E18 - "
            tmpName = name.split(" - ", 2)
            fileName = tmpName[2].split(" (", 1)
            newName = directory + fileName[0]
            
            os.rename((directory + name), newName)
            os.rename(newName, newName + ".mkv")
            
            file.write(fileName[0].lower())
            file.write("\n")

         elif ".mp4" in name:
            tmpName = name.split(" - ", 1)

            os.rename((directory + name), (directory + tmpName[1]))

            file.write(fileName[0].lower())
            file.write("\n")
   file.close()

def getSetFromFile(fileName):
   file = open(fileName, "r")
   fNames = set()

   for line in file:
      fNames.add(line.strip())

   return fNames

def filesNum(nameSet):
   print(len(nameSet))

getNameFromDir("Tom&Jerry2", "vidNames2.txt")
names1 = getSetFromFile("vidNames2.txt")

# getNameFromDir("Tom&Jerry1", "vidNames1.txt")
# names2 = getSetFromFile("vidNames1.txt")

# intersect = names1 & names2
# filesNum(intersect)

# if (len(intersect) == (len(names2) - len(names1))):
#    print("Process is a success")
