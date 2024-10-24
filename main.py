def decode(encoded_password):
    decoded = ""
    for char in encoded_password:
        temp = int(char) - 3
        if temp < 0:
            temp += 10
        decoded += str(temp)
    
    return decoded

if __name__ == "__main__":
    while True:
        print("     Menu     ")
        print("1. Decode password")
        print("2. Exit")
        choice = input("\nEnter menu option: ")

        if choice == "1":
            user_input = input("Enter encoded password: ")
            decoded_password = decode(user_input)
            print(f"Decoded password is: {decoded_password}")
        
        elif choice == "2":
            break
        
        else:
            print("Not a valid menu option")
