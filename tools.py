# DES functions

import constants as c


# Takes a integer array/list of 0s and 1s and converts it to an integer. 
def binToInt(bits):
    
    # printing original list
    print("Binary: " + str(bits))
    
    # using join() + list comprehension
    # converting binary list to integer
    res = int("".join(str(x) for x in bits), 2)
    
    # printing result
    return res


# This function takes an integer representing a number in decimal to be converted to binary, and the length of the resulting binary number.
def intToBin(num, length): 

    print ("Decimal: " + str(num))
    
    # decimal to binary number conversion 
    result = [int(i) for i in list('{0:0b}'.format(num))]
    
    # list of bits 
    bitArray = (result)

    # add padding
    while(length!= len(bitArray)):
        bitArray.insert(0,0)

    return bitArray


# Receives two integer arrays containing 0s and 1s, and returns a new array containing the bit-by-bit xor of the two arrays.
def xor(a, b):
    
    newBit = []
    
    for i in range(len(a)):

        if a[i] != b[i]:
            newBit.append(1)

        if a[i] == b[i]:
            newBit.append(0)    

    return newBit


# Receives an integer array of 0s and 1s, and returns a new permuted integer array of 0s and 1s based on the permutation perm.
def permute(bits, perm): 
    
    binBits = [0]  * len(perm)

    index = 0 
    for i in perm: 
        binBits[index] = bits[i - 1]
        index = index + 1

    return binBits

    
# Receives a length 6 integer array of 0s and 1s and a 2D integer array (one of the S-boxes). Returns the 4-bit conversion as an integer \
# array of 0s and 1s based on the 6-bits and the S-box.
def sBox(bits, box): 

    length = len(bits)

    row = [bits[0], bits[length - 1]]
    rowInt = binToInt(row)
    
    # remove the 2 outer bits 
    bits.pop(length - 1)
    bits.pop(0)
    col = [0] * len(bits)

    count = 0 
    for i in bits: 
        col[count] = i 
        count = count + 1

    colInt = binToInt(col)
    result = box[rowInt][colInt]
    binNum = intToBin(result,4)

    return binNum


# This function takes in the 64-bit key as an integer array/list of 0s and 1s, and outputs the subkey for the first round of DES. 
def generateK1(k):

    result = permute(k,c.PC1)

    left1 = [] 
    left2 = [] 
    right1 = [] 
    right2 = [] 

    for i in range(28): 
        left1.append(result[i])
        right1.append(result[i+28])

    for i in range(28): 
        if i == 27: 
            left2.append(left1[0])
            right2.append(right1[0])

        else: 
            left2.append(left1[i+1])
            right2.append(right1[i+1])

    ki = left2 + right2
    subKey = permute(ki,c.PC2)

    return subKey



    








            


    
