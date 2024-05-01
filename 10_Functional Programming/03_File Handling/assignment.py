file_path = "C:\\Users\\whiteana001\\Dev\\POC_Sem2_Assignments\\10_Functional Programming\\03_File Handling\\myFile.txt"

try:
    stream = open(file_path, "r")
    print(stream.read())
    stream.close
except:
    print("wrong")