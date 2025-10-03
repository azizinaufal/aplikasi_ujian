password = "password"
percobaan = 0
max = 3

while percobaan < max:
    password_input = input("Password: ")
    percobaan +=1

    if password_input == password:
        print("Password benar")
        break
    else:
        print("Password salah coba lagi")
else:
    print("Percobaan melebihi batas")