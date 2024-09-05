from copy import deepcopy
from format_des import *

format = Formatting()

#Permuted Choice 2 Table
PC_2 = [[14, 17, 11, 24, 1, 5],
        [2, 28, 15, 6, 21, 10],
        [23, 19, 12, 4, 26, 8],
        [16, 7, 27, 20, 13, 2],
        [41, 52, 31, 37, 47, 55],
        [30, 40, 51, 45, 33, 48],
        [44, 40, 39, 56, 34, 53],
        [46, 42, 50, 36, 29, 32]]


PC_2_LENGTH = 7

# S-tables
S = [
        [
            [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
            [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
            [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
            [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
        ],
        [
            [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
            [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
            [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
            [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
        ],
        [
            [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
            [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
            [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
            [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
        ],
        [
            [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
            [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
            [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
            [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
        ],
        [
            [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
            [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
            [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
        ],
        [
            [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
            [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
            [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
            [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
        ],
        [
            [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
            [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
            [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
        ],
        [
            [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
            [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
            [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
            [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
        ] 
    ]


P = [
        [16, 7, 20, 21, 29, 12, 28, 17],
        [1, 15, 23, 26, 5, 18, 31, 10],
        [2, 8, 24, 14, 32, 27, 3, 9],
        [19, 13, 30, 6, 22, 11, 4, 25]
    ]


class Cipher:

    # number: num from lookup map
    # length: length of table data will be taken from; i.e. not lookup table
    def row_col_translate(self, number: int, length) -> list[int, int]:
        row, col = int(number/length), (number%length+length-1)%length
        if number/length - int(number/length) <= 0:
            row = row - 1
        return [row, col]

    # lr: left or right 32 bit table
    # rk: left or output of k 32 bit table
    # modifier: for accessing a elements in a transposed list
    def exclusive_or(self, lr: list, rk: list,rows=8, cols=6, modifier=0) -> list:
        xor = []
        if modifier == 0:
            for i in range(rows):
                row = []
                for j in range(cols):
                    row.append(lr[i][j] ^ rk[i][j])
                xor.append(row)
        else:
            for i in range(rows):
                row = []
                for j in range(cols):
                    row.append(lr[i][j] ^ rk[modifier-j][i])
                xor.append(row)
        return xor

    class User_Input:
        # 1.
        def initial_permutation(self, table: list) -> list:
        
            evens_table = deepcopy(table[0:4])
            odds_table = deepcopy(table[4:8])
            for i in range(4):
                    odds_table[i] = list(reversed([row[(i*2)] for row in table]))
                    evens_table[i] = list(reversed([row[1+(i*2)] for row in table]))
            
            table[0:4] = evens_table
            table[4:8] = odds_table
            return table

        def inverse_initial_permutation(self, table: list) -> list:
            thirty_two, sixty_four = [], []

            for k in range (4):
                thirty_two.append(list(reversed([table[k][i]  for i in range(8)])))
                sixty_four.append(list(reversed([table[4+(k)][i]  for i in range(8)])))

            transpose = []
            for i in range(8):
                row = []
                for j in range(4):
                    row.append(sixty_four[j][i])
                    row.append(thirty_two[j][i])
                transpose.append(row)

            return transpose
 

        def input_blocks(self, table: list) -> list[list, list]:
            left, right = [], []
            for i in range(4):
                    left.append(table[i])
                    right.append(table[i+4])
            return [left, right]


        def ebit_selection(self, table: list) -> list:
            e_table = []
            modfier=32
            for i in range(8):
                row = []
                for j in range(6):
                    row_col = Cipher.row_col_translate(self, (modfier+j)%32, 8)
                    row.append(table[row_col[0]][row_col[1]])
                modfier = (modfier+4)%32
                e_table.append(row)
            return e_table


        def key_dependent_computation(self, k: list, left: list, right: list) -> list[list, list]:
            prev_r = deepcopy(right)

            # 4. Create e_bit expansion table from right
            right = self.ebit_selection(right)

            # 5. xor right ebit and key
            right = Cipher.exclusive_or(self, right, k)

            # 6. S selection on 8 rows
            s_table = []
            for i in range(8):
                s_row = int(str(right[i][0]) + str(right[i][-1]), 2)
                s_col = int(''.join([str(num) for num in right[i][1:5]]), 2)
                s_out = f'{S[i][s_row][s_col]:04b}'
                row = []
                for char in s_out:
                    row.append(int(char))
                s_table.append(row)
            right = s_table
            # 7. P permutation
            p = []
            for i in range(4):
                row = []
                for j in range(8):
                    row_col = Cipher.row_col_translate(self, P[i][j],4)
                    row.append(right[row_col[0]][row_col[1]])
                p.append(row)
            right = p

            # 9. xor
            right = Cipher.exclusive_or(self, right, left, rows=4, cols=8)
            left = prev_r

            return [left, right]


        def main(self, keys, message, decrypt=False, l=0, r=1, result='En') -> str:
            # 1.
            z = 0
            result_message = ''
            message_table = format.populate_table(message, decrypt=True) if decrypt else format.populate_table(message)
            if not decrypt:
                original_message = ''
                for block in message_table:
                    original_message = original_message + format.get_bits(block)
                print(f'Original message: {original_message}')

            for message_block in message_table:
                z = z + 1
                # 2. get message into blocks of 64 bits
                block = self.initial_permutation(message_block)

                # 3. split into left and right 
                block = self.input_blocks(block)
                left, right = block[l], block[r]

                rounds = range(16) if not decrypt else reversed(range(16))
                for q in rounds:
                    comp_out = self.key_dependent_computation(keys[q], left, right)
                    if (q == 15 and not decrypt) or (q == 0 and decrypt):
                        l, r = (l+1)%2, (r+1)%2
                    left, right = comp_out[l], comp_out[r]

                cipher_table = left + right
                cipher_table = self.inverse_initial_permutation(cipher_table)
                cipher_block_bits = format.get_bits(cipher_table)
                result_message = result_message + cipher_block_bits

            print()
            print(f'{result}crypted: {result_message}')
            if decrypt:
                print(f'\nOriginal message: {format.bits_to_msg(result_message)}')
                return f'{result}crypted: {result_message}\nOriginal message: {format.bits_to_msg(result_message)}'
            else:
                return f'Original message:{original_message}\n{result}crypted: {result_message}' 

    # Key
    class Key:

        # PC-1 for C and D of key
        # Returns C in [0] and D in [1]
        def permuted_choice1(self, table: list) -> list[list, list]:
            PC_1_LENGTH = 7
            # Generate C
            @staticmethod
            def generate_C(table: list) -> list:
                c = []
                for i in range(4):
                    row = list(reversed([row[i] for row in table][i+1:]))
                    fill = len(row)
                    k = 0
                    while(fill < PC_1_LENGTH):
                        row.insert(0,table[k][i-1])
                        k, fill = k+1, fill + 1
                    c.append(row)
                return c

            # Generate D
            @staticmethod
            def generate_D(table: list) -> list:
                d = []
                for i in range(3):
                    row = list(reversed([row[len(table)-i-2] for row in table][i+1:]))
                    fill = len(row)
                    k = 0
                    while(fill < PC_1_LENGTH):
                        row.insert(0,table[k][len(table)-1-i])
                        k, fill = k+1, fill+1
                    d.append(row)
        
                row = list(reversed([row[len(table)-1-3] for row in table][0:3])) \
                    + list(reversed([row[len(table)-1-4] for row in table][0:4]))
                d.append(row)
                return d
            
            return [generate_C(table), generate_D(table)]


        def left_shift(self, table: list) -> list:
            shift_col = [row[0] for row in table]
            for i in range(4):
                table[i] = table[i][1:]
                table[i] = table[i] + [shift_col[(1+i)%4]]
            return table
        
        
        def permuted_choice2(self, table: list) -> list:
            pc_2 = []
            for i in range(PC_2_LENGTH+1):
                row = []
                for j in range(PC_2_LENGTH-1):
                    row_col = Cipher.row_col_translate(self, PC_2[i][j], PC_2_LENGTH)
                    row.append(table[row_col[0]][row_col[1]])
                pc_2.append(row)
            return pc_2


        def main(self, q:int, key_table:list, c:list, d:list, pc_2:list, decrypt:bool=False) -> list[list, list, list, list]:
            if q == 1:
                # The initial permutation generates c and d key already
                c, d = [list(row) for row in key_table][0], [list(row) for row in key_table][1]
            else:
                c, d = [list(row) for row in key_table][:5], [list(row) for row in key_table][4:]

            if q == 1 or 2 or 9 or 16:
                Cipher.Key.left_shift(self, c)
                Cipher.Key.left_shift(self, d)
            else:
                Cipher.Key.left_shift(self, c)
                Cipher.Key.left_shift(self, c)
                Cipher.Key.left_shift(self, d)
                Cipher.Key.left_shift(self, d)

            key_table = c+d
            pc_2 = self.permuted_choice2((c+d))

            return [key_table, c, d, pc_2]


            
"""
Notes
Algos based off of FIPS 46-3 DES PC-1 Tables
Notes for C
*Repeat 4 times fill backward, i.e. 1st col will go to last row
    * get 7 - i col (e.g.7, 6,5,4) rows from col 1 (0 indexed)
        * list(row[i] for row in table)[i+1:-1]
        * table[1:7];table[2:7];table[3:7]
    * temp = 7 - i
    * if temp < 7:
        * j = 0
        * get elements from or on pivot points until temp is 7
            * e.g. [1], [2,10], [3,11,19]
            * [current col - 1][j]

Notes for D BACKWARDS
* alg: 
* Repeat 4 times:
    * get list(row[second-to-last] for row in table)[i+1:-1]
    * that'll be the 1st row
"""