from time import sleep

class ceaser(): #ceaser encrypt e decrypt; with and withot key.
    def Ceaser_encrypt(message, key):
        if key > 26:
            key = key%26 #Pegar o resto da divisão

        alfab = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
                'x', 'y', 'z','a','b','c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w','x', 'y', 'z']
        Alfab =['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                'R', 'S','T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        scripting = []

        for x in range(len(message)):
            if message[x].upper() == message[x]:
                for i in range(len(Alfab)-1):
                    if message[x] == " ":
                        scripting.append(" ")
                        break
                    elif message[x] == Alfab[i]:
                        scripting.append(Alfab[i+key])
                        break
            else:
                for i in range(len(alfab)-1):
                    if message[x] == " ":
                        scripting.append(" ")
                        break
                    elif message[x] == alfab[i]:
                        scripting.append(alfab[i+key])
                        break
        encrypted_message = ""           
        for y in range(len(scripting)):
            encrypted_message += scripting[y] 
        return encrypted_message

    def Ceaser_decrypt_with_key(message, key):
        if key > 26:
            key = key%26 #Pegar o resto da divisão

        alfab = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
                'x', 'y', 'z','a','b','c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w','x', 'y', 'z']
        Alfab =['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                'R', 'S','T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        scripting = []

        for x in range(len(message)):
            if message[x].upper() == message[x]:
                for i in range(len(Alfab)-1):
                    if message[x] == " ":
                        scripting.append(" ")
                        break
                    elif message[x] == Alfab[i]:
                        scripting.append(Alfab[i-key])
                        break
            else:
                for i in range(len(alfab)-1):
                    if message[x] == " ":
                        scripting.append(" ")
                        break
                    elif message[x] == alfab[i]:
                        scripting.append(alfab[i-key])
                        break
        encrypted_message = ""           
        for y in range(len(scripting)):
            encrypted_message += scripting[y] 
        return encrypted_message

    def Ceaser_decrypt_withot_key(message):
        alfab = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
                'x', 'y', 'z','a','b','c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w','x', 'y', 'z']
        Alfab =[ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                'R', 'S','T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        
        decrypts = []
        for key in range(26):
            scripting = []
            for x in range(len(message)):
                if message[x].upper() == message[x]:
                    for i in range(len(Alfab)-1):
                        if message[x] == " ":
                            scripting.append(" ")
                            break
                        elif message[x] == Alfab[i]:
                            scripting.append(Alfab[i-key])
                            break
                else:
                    for i in range(len(alfab)-1):
                        if message[x] == " ":
                            scripting.append(" ")
                            break
                        elif message[x] == alfab[i]:
                            scripting.append(alfab[i-key])
                            break
            encrypted_message = ""           
            for y in range(len(scripting)):
                encrypted_message += scripting[y] 
            decrypts.append(encrypted_message)

        return decrypts
        
class defs(): #defs normais de auxilio de string
    def linha():
        print("\n"+"=-"*29 + "\n")  

    def choice():
        while True:
            print("""1 - Ceaser_encrypt
2 - Ceaser_decrypt (with_key)
3 - Ceaser_decrypt (without_key)
4 - Exit\n""")
            
            the_choice = int(input("Choice a function:  "))
            if the_choice == 1 or the_choice == 2 or the_choice == 3 or the_choice == 4:
                return the_choice
            else:
                print("Choice only one of the choices!")

    #print(Ceaser_decrypt_withot_key("Bynbsqy"))

    def filter_numbers(text, from_undo):
        if text.isdigit():
            return text
        
    def filter_char(text, from_undo):
        for char in text:
                if not char.isalpha() and char != ' ':
                    return
                else:
                    return text
        


