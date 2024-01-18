username = "arish@gmail.com"
password = "dogcatmouse"

email = input("Enter the email : ")
EnteredPassword = input("Please enter your password : ")

if email == username:
    if EnteredPassword == password:
        print("Login successful! ")
    else:
        print("Email or password is incorrect")
else:
    print("User does not exist")
