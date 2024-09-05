import re
#des_formatting.py
class Formatting:
    
    def print_table(self, table,
                    table2: list=None, 
                    n1: str=None, n2: str=None,
                    rows=4,
                    cols=8,
                    test=None):
        if test is None:
            if table2 is None:
                for row in table:
                    print(row)
            elif n1 is None or n2 is None:
                for i in range(rows):
                    print(f'{table[i]} | {table2[i]}')
            else:
                print(f' {n1:{cols*3+2}} {n2}')
                for i in range(rows):
                    print(f'{table[i]} | {table2[i]}')
            print()
        else:
            if table2 is None:
                for row in table:
                    print(["%2d" % elem for elem in row])
            elif n1 is None or n2 is None:
                for i in range(rows):
                    print(f'{["%2d" % elem for elem in table[i]]} | {["%2d" % elem for elem in table2[i]]}')
            else:
                print(f' {n1:{cols*4}} {n2}')
                for i in range(rows):
                    print(f'{["%2d" % elem for elem in table[i]]} | {["%2d" % elem for elem in table2[i]]}')
            print()
            

    def filter_text(self, message: str, decrypt=False) -> str:
        if not decrypt:
            return re.sub(r'[\W_]|[;]', "", message)
#             return message.strip() -- This way works but is not part of the rules

        return re.sub(r'[\D_]|[\w;]', "", message)    


    def populate_table(self, message: str, key=False, decrypt=False) -> list:
        blocks, table = [], []
        byte_count = 0

        if decrypt:
            row = []
            bit_count = 0
            for bit in message:
                row.append(int(bit))
                bit_count = bit_count + 1

                if bit_count == 8:
                    table.append(row)
                    row = []
                    bit_count, byte_count = 0, byte_count+1

                if byte_count == 8:
                    blocks.append(table)
                    table = []
                    bit_count, byte_count = 0, 0
        else: 
            for letter in message:
                bits = ord(letter)
                formated_bits = f'{bits:08b}'
                row = []

                for bit in formated_bits:
                    row.append(ord(bit) - 48)

                table.append(row)
                byte_count = byte_count + 1

                if byte_count == 8 and not key:
                    blocks.append(table)
                    byte_count = 0
                    table = []
            if key:
                return table

        if byte_count != 0:
            blocks.append(table)
            pad = blocks[-1]
            while(byte_count != 8):
                row = [0] * 8
                pad.append(row)
                byte_count = byte_count + 1

        return blocks


    def get_bits(self, messge_table: list) -> str:
        e_message = ''
        for row in messge_table:
            row_encryption = ''.join([str(num) for num in row])
            e_message = e_message + row_encryption
        return e_message

    
    def bits_to_msg(self, decryption: str) -> str:
        msg_blocks = (decryption[i:i+8] for i in range(0 , len(decryption), 8))
        return ''.join(chr(int('0b'+bit, 2)) for bit in msg_blocks)

