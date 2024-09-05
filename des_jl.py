from format_des import *
from cipher import *

format = Formatting()
encrypt = Cipher()
key = encrypt.Key()
user_input = encrypt.User_Input()
'''

# Constants for testing
test28 = []
for i in range(1,5):
    tr = []
    for j in range((i*7)-6, (i*7)+1):
        tr.append(j)
    test28.append(tr)

test56 = []
for i in range(1,9):
    tr = []
    for j in range((i*7)-6, (i*7)+1):
        tr.append(j)
    test56.append(tr)

test64 = []
for i in range(1,9):
    tr = []
    for j in range((i*8)-7, (i*8)+1):
        tr.append(j)
    test64.append(tr)
    
test48 = []
modfier = 31
for i in range(8):
    tr = []
    for j in range(6):
        tr.append((modfier+j)%32+1)
    modfier = (modfier+4)%32
    test48.append(tr)

TWENTY_EIGHT = test28
FIFTY_SIX = test56
EBIT_SELECTION = test48
SIXTY_FOUR = test64
TEST_KEY = 'THisKEy1'

'''
if __name__ == "__main__":
    # TODO remove this test code 
    # TODO if key is not equal to 8 ask for another key "cannot ecrypt"
    print()
    while True:
        user_choice = input('Enter \'q\' to quit\nWould you like to [1] encrypt or [2] decrypt a message?\n>> ')
        if user_choice.lower() not in ('1', '2', 'q'):
            print('\nResponse not valid...\n')
        else:
            if user_choice == '1':
                encrypted_message = ''
                # KEYS
                user_key = input('Please enter an 8 character key\n>> ')
                user_key = format.filter_text(user_key)
                while len(user_key) != 8:
                    user_key = input('The key must be exactly 8 characters. \
                                        Special characters are not allowed.\n>> ')

                user_key = format.filter_text(user_key)
                key_table = format.populate_table(user_key, key=True)
                key_table = key.permuted_choice1(key_table)

                keys, c, d, permutated_choice2 = [], [], [], []
                for i in range(1,17):
                    permutations = key.main(i, key_table, c, d, permutated_choice2)
                    keys.append(permutations[-1])
                    key_table, c, d = permutations[0], permutations[1], permutations[2]

                while True:
                    user_choice1 = input('Would you like to [1] read from a file or [2] type the message here?\n>>')     
                    if user_choice.lower() not in ('1', '2', 'q'):
                        print('\nResponse not valid...\n')
                    else:
                        if user_choice1 == '1':
                            user_file = input(str('Please provide the file directory. i.e. plaintext.txt\n>> '))
                            try:
                                file = open(user_file, 'r')
                                message = file.read()
                                message = format.filter_text(message)
                                print(f'\nfiltered: {message}\n')

                                # Encryption
                                encrypted_message = user_input.main(keys, message)
                                file_out = open("encryption.txt", "w+")
                                file_out.write(encrypted_message)
                                file_out.close()
                                file.close()
                                print('Written to encryption.txt\n')
                                break

                            except FileNotFoundError:
                                print('File and/or file path does not exist...')
                        elif user_choice1 == '2':
                            # Message    
                            message = input('\nEnter a mesage to encrypt\n>> ')
                            print(f'\ninput: {message}')
                            message = format.filter_text(message)
                            print(f'\nfiltered: {message}\n')

                            # Encryption
                            encrypted_message = user_input.main(keys, message)
                            file_out = open("encryption.txt", "w+")
                            file_out.write(encrypted_message)
                            file_out.close()
                            print('Written to encryption.txt\n')
                            break
                        else:
                            break

            elif user_choice == '2':
                # Key
                user_key = input('Enter the encryption key.\n>> ')
                while len(user_key) != 8:
                    user_key = input('The key must be exactly 8 characters. \
                                        Special characters are not allowed.\n>> ')
                    user_key = format.filter_text(user_key)

                key_table = format.populate_table(user_key, key=True)
                key_table = key.permuted_choice1(key_table)

                keys, c, d, permutated_choice2 = [], [], [], []
                for i in range(1,17):
                    permutations = key.main(i, key_table, c, d, permutated_choice2)
                    keys.append(permutations[-1])
                    key_table, c, d = permutations[0], permutations[1], permutations[2]

                while True:
                    user_choice2 = input('Would you like to [1] read from a file or [2] copy and paste the encryption here?\n>>')     
                    if user_choice.lower() not in ('1', '2', 'q'):
                        print('\nResponse not valid...\n')
                    else:
                        if user_choice2 == '1':
                            user_file = input(str('Please provide the file directory. i.e. encryption.txt\n>> '))
                            try:
                                # 
                                message = ''
                                with open(user_file, 'r') as user_file:
                                    for line in user_file:
                                        if line.__contains__('Encrypted'):
                                            message = line.split(' ')[1]
                                if message == '':
                                    print('No encryption found in file.')
                                    break

                                message = format.filter_text(message)
                                print(f'\nfiltered: {message}\n')

                                # Decryption
                                decrypted_message = user_input.main(keys, message, decrypt=True, result='De')
                                file_out = open('decryption.txt', 'w+')
                                file_out.write(decrypted_message)
                                file_out.close()
                                print('Written to decryption.txt\n')
                            except FileNotFoundError:
                                print('File and/or file path does not exist...')
                            else:
                                break

                        elif user_choice2 == '2':
                            # User Input
                            message = input('Enter an encrypted message\n>> ')
                            message = format.filter_text(message)
                            print(f'filtered: {message}\n')

                            # Decryption
                            decrypted_message = user_input.main(keys, message, decrypt=True, result='De')
                            file_out = open('decryption.txt', 'w+')
                            file_out.write(decrypted_message)
                            file_out.close()
                            print('Written to decryption.txt\n')

            else:
                print("\nQuiting program...")
                break