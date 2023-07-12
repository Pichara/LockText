from defs import ceaser, defs
from time import sleep

defs.linha()
print("CEASER ENCRYPT".center(55))
while True:
    defs.linha()
    the_choice = defs.choice()
    if the_choice == 1:
        while True:
            to_encrypt = str(input("What do you wanna encrypt: "))
            if to_encrypt.isnumeric():
                print("We can input; for now; only a string, sir!")
            else:
                break
        while True:
            try:
                key = int(input("Inform the key to encrypt:  "))
                break
            except:
                print("Only numbers, please!")
        encrypted = ceaser.Ceaser_encrypt(to_encrypt, key)
        sleep(0.25)
        print(f"\n{to_encrypt} with the key {key} is: {encrypted}")
        sleep(2)
                
    elif the_choice == 2:
        while True:
            to_decrypt = str(input("What do you wanna decrypt: "))
            if to_decrypt.isnumeric():
                print("We can input; for now; only a string, sir!")
            else:
                break
        while True:
            try:
                key = int(input("Inform the key to decrypt:  "))
                break
            except:
                print("Only numbers, please!")
        decrypted = ceaser.Ceaser_decrypt_with_key(to_decrypt, key)
        sleep(0.25)
        print(f"\n{to_decrypt} with the key {key} is: {decrypted}")
        sleep(2)

    elif the_choice == 3:
        while True:
            to_decrypt = str(input("What do you wanna decrypt: "))
            if to_decrypt.isnumeric():
                print("We can input; for now; only a string, sir!")
            else:
                break
        probability_decrypted = ceaser.Ceaser_decrypt_withot_key(to_decrypt)
        for i in range(26):
            print(f"{i} - {probability_decrypted[i]}")
        while True:
            choice = int(input("\nWhat of these is [0/25]:  "))
            if choice > 0 and choice < 27:
                break
        
        sleep(0.25)
        print(f"\nThe encrypt {to_decrypt} is most probability to be {probability_decrypted[choice]}")
        sleep(2)
    
    elif the_choice == 4:
        break