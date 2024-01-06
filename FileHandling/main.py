f = open("F:\PythonRepo\PythonRepo\FileHandling\check.txt","r")
print(f.read())

print("----------------------------------------------------------------------------------")

#Writing into a file
f = open("check1.txt","w")
f.write("I have created this file using python")

print("----------------------------------------------------------------------------------")

#Opening check1.txt file
f = open("F:\PythonRepo\PythonRepo\check1.txt","r")
print(f.read())

print("----------------------------------------------------------------------------------")

#Reading the file check.txt line by line
f = open("F:\PythonRepo\PythonRepo\FileHandling\check.txt","r")
print(f.readline())
print(f.readline())
print(f.readline())

print("----------------------------------------------------------------------------------")

f = open("F:\PythonRepo\PythonRepo\FileHandling\check.txt","r")
print(f.readlines()[1])