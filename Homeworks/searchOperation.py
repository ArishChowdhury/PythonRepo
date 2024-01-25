f = open("F:\PythonRepo\PythonRepo\Homeworks\Thing.txt","r")
file_content = f.read()

print("----------------------------------------------------------------------------------")

search_phrase = input("Please enter the phrase you want to enter: ")
if search_phrase.lower() in file_content.lower():
    print("The phrase is present")
else:
    print("The phrase is not present")