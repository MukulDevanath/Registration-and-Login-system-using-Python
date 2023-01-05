import re

def register():
  data_file = open("File_Handler.txt", "a")

  email_pattern = "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}"
  password_pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{5,16}$"
  
  email = input("Enter email/username : ")
  password = input("Enter Password : ")

  match_email = re.findall(email_pattern, email)
  match_password = re.findall(password_pattern, password)

  if match_email == []:
    print("Invalid Email, Please Try Again\n")
    register()
  elif match_password == []:
    print("Invalid Password, Please Try Again\n")
    register()
  else:
    data_file.write(email + ", " + password + "\n")
    print("User Registered.\n")

  data_file.close()


def login():
  email = input("Enter email/username : ")
  password = input("Enter Password : ")

  data_file = open("File_Handler.txt", "r")
  d = []
  f = []
  for i in data_file:
    a,b = i.split(",")
    b = b.strip()
    c = a,b
    d.append(a)
    f.append(b)
    data = dict(zip(d, f))

  if (email, password) in data.items():
    print("Logged in Successfully.\n")
  else:
    print("User not found, Please Register\n")
    register()

  data_file.close()

def forgot_password():
  email = input("Enter email/username : ")

  data_file = open("File_Handler.txt", "r")
  d = []
  f = []
  for i in data_file:
    a,b = i.split(",")
    b = b.strip()
    c = a,b
    d.append(a)
    f.append(b)
    data = dict(zip(d, f))

  if email in data:
      print("Your Password is", data[email])
  else:
      print("User doesn't exist, Please Register\n")
      register()

  data_file.close()


print('''Please select an option
1. Register
2. Login
3. Forgot Password\n''')
option = int(input())

if option == 1:
  register()
elif option == 2:
  login()
elif option == 3:
  forgot_password()
else:
  print("Invalid Option")

