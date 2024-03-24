def can_construct(word , letters):
    word=list(word)
    letters=list(letters)
    for letter in word:
        if letter not in letters:
            return False
        else:
            letters.remove(letter)
    return True

print(can_construct("apples", "aplespl"))
print(can_construct("apples", "aples"))

class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        real = self.a + other.a
        imaginary = self.b + other.b
        return Complex(real, imaginary)

    def __sub__(self, other):
        real = self.a - other.a
        imaginary = self.b - other.b
        return Complex(real, imaginary)

    def __mul__(self, other):
        real = self.a * other.a - self.b * other.b
        imaginary = self.a * other.b + self.b * other.a
        return Complex(real, imaginary)

    def __repr__(self):
        if self.b > 0:
            return (f'{self.a} + {self.b}i')
        if self. b < 0:
            self.b = -self.b
            return (f'{self.a} - {self.b}i')
        if self.b == 0:
            return (f'{self.a}')

cplx1 = Complex(5, 2)
print(cplx1)

import random
def create_permutation(n):
    list = [i for i in range(n)]
    list1 = []
    for i in range(1,n):
        k = len(list)
        num = list[random.randint(0,k-1)]
        list1.append(num)
        list.remove(num)
    list1.append(list[0])
    return list1

print(create_permutation(6))

def scramble_word(word):
    lst = create_permutation(len(word))
    string = ''
    for i in lst:
        string += word[i]
    return string

print(scramble_word("pokemon"))

def guessing(word):
    word = scramble_word(word)
    scram = ''
    for i in word:
        scram = scram + i + ' '
    print(f'Unscramble the word: {scram}')
    n = 1
    string = input(f'Try #{n}: ')
    while string != word and n < 3:
        print('Wrong!')
        n += 1
        string = input(f'Try #{n}: ')
    if string == word:
        print('Yay, you got it!')
    else:
        print('Wrong!')

guessing('poke')

def binary_to_decimal(binary_list):
    deci = 0
    for bit in range(1, len(binary_list)+1):
        deci += binary_list[-bit] * (2 ** (bit-1))
    return deci

def add_binary(bin_num1, bin_num2):
    num1 = num2 = 0
    for i in range(0, len(bin_num1)):
        num1 += int(bin_num1[-i-1])*(2**(i))
    for i in range(0, len(bin_num2)):
        num2 += int(bin_num2[-i-1])*(2**(i))
    num = num1 + num2
    print(num)
    list = []
    while True:
        digit = num // 2
        residue = num % 2
        list += [residue]
        if digit == 0:
            break
        num = digit
    list.reverse()
    bin_num = ''
    for char in list:
        bin_num += str(char)
    return bin_num
print(add_binary('11', '1'))








