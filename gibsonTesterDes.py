# Kolby Gibson 
# Tester for des 

from tools import *


# testing for binToInt 
def testBinToInt():

    inp1 = [0,0,1,0,1,0,0,1]
    inp2 = [1,0]
    inp3 = [0,1,0,1]

    exp1 = 41
    exp2 = 2
    exp3 = 5

    result1  = binToInt(inp1)
    result2 = binToInt(inp2)
    result3 = binToInt(inp3)

    print("****************************** Binary to Integer Function Test *********************************")
    print("\n")
    print("Function takes in a list of bits of any size and returns its associated integer value")
    print("\n")
    print(f"Expected Results: Binary List: {inp1}   --->   Integer Value: {exp1}")
    print(f"Expected Results: Binary List: {inp2}   --->   Integer Value: {exp2}")
    print(f"Expected Results: Binary List: {inp3}   --->   Integer Value: {exp3}")
    print("\n")
    print(f"Test one: ... Binary List: {inp1}   --->   Integer Value: {result1}")
    print(f"Test two: ... Binary List: {inp2}   --->   Integer Value: {result2}")
    print(f"Test three: ... Binary List: {inp3}   --->   Integer Value: {result3}")
    print("\n")
  


# testing for IntToBin
def testIntToBin():

    exp1 = [0,0,1,0,1,0,0,1]
    exp2 = [1,0,1,0,0,1]
    exp3 = [0,1,0,1]

    result1 = intToBin(41,8)
    result2 = intToBin(41,6)
    result3 = intToBin(5,4)

    print("\n")
    print("\n")
    print("****************************** Integer to Bianry Test *********************************")
    print("\n")
    print("Function takes in a number and a prefered length and returns its binary association with padding if necessary")
    print("\n")
    print(f"Expected Results: Number: 41  Length: 8   --->   Binary Value: {exp1}")
    print(f"Expected Results: Number: 41  Length: 6   --->   Binary Value: {exp2}")
    print(f"Expected Results: Number: 5  Length: 4   --->   Binary Value: {exp3}")
    print("\n")
    print(f"Test one: ...  Number: 41  Length: 8   --->   Binary Value: {result1}")
    print(f"Test two: ... Number: 41  Length: 6   --->   Binary Value: {result2}")
    print(f"Test three: ... Results: Number: 5  Length: 6   --->   Binary Value: {result3}")
    print("\n")
   


def testXor():

    leftInp1 = [1,1,1,1]
    leftInp2 = [0,0,0,0,1,1]
    leftInp3 = [1]
    rightInp1 = [0,1,0,1]
    rightInp2 = [1,1,0,0,0,0]
    rightInp3 = [1]

    exp1 = [1,0,1,0]
    exp2 = [1,1,0,0,1,1]
    exp3 = [0]

    result1  = xor(leftInp1,rightInp1)
    result2 = xor(leftInp2,rightInp2)
    result3 = xor(leftInp3,rightInp3)

    print("\n")
    print("\n")
    print("****************************** XOR Test *********************************")
    print("\n")
    print("Function takes in a number and a prefered length and returns its binary association with padding if necessary")
    print("\n")
    print(f"Expected Results: Bits 1: {leftInp1}  Bits 2: {rightInp1}  --->   XOR Value: {exp1}")
    print(f"Expected Results: Bits 1: {leftInp2}  Bits 2: {rightInp2}  --->   XOR Value: {exp2}")
    print(f"Expected Results: Bits 1: {leftInp3}  Bits 2: {rightInp3}  --->   XOR Value: {exp3}")
    print("\n")
    print(f"Test one: ... Bits 1: {leftInp1}  Bits 2: {rightInp1}  --->   XOR Value: {result1}")
    print(f"Test two: ... Bits 1: {leftInp2}  Bits 2: {rightInp2}  --->   XOR Value: {result2}")
    print(f"Test three: ... Bits 1: {leftInp3}  Bits 2: {rightInp3}  --->   XOR Value: {result3}")
    print("\n")
   

def testPermute():

    bits1 = [1,1,0,0,0]
    bits2 = [0,1,1,0,0,0]
    bits3 = [1,1,0,0,0]
    perm1 = [1,2,3,4,5]
    perm2 = [6,5,4,3,2,1]
    perm3 = [3,1,5,2,4,1,3]

    exp1 = [1,1,0,0,0]
    exp2 = [0,0,0,1,1,0]
    exp3 = [0,1,0,1,0,1,0]

    result1 = permute(bits1, perm1)
    result2 = permute(bits2, perm2)
    result3 = permute(bits3, perm3)

    print("\n")
    print("\n")
    print("******************************************** Permute Test ****************************************************")
    print("\n")
    print("Receives an integer array of 0s and 1s, and returns a new permuted integer array of 0s and 1s based on the permutation perm.")
    print("\n")
    print(f"Expected Results: Bits 1: {bits1}  Perm: {perm1}  --->   Permuted Value: {exp1}")
    print(f"Expected Results: Bits 1: {bits2}  Perm: {perm2}  --->   Permuted Value: {exp2}")
    print(f"Expected Results: Bits 1: {bits3}  Perm: {perm3}  --->   Permuted Value: {exp3}")
    print("\n")
    print(f"Test one: ... Bits 1: {bits1}  Perm: {perm1}  --->   Permuted Value: {result1}")
    print(f"Test two: ... Bits 1: {bits2}  Perm: {perm2}  --->   Permuted Value: {result2}")
    print(f"Test three: ... Bits 1: {bits3}  Perm: {perm3}  --->   Permuted Value: {result3}")
    print("\n")
  


def testSBox():

    bits1 = [0,1,1,0,0,0]
    bits2 = [0,1,1,0,0,1]
    bits3 = [1,1,0,0,0,0]
    
    exp1 = [0,1,0,1]
    exp2 = [0,1,1,0]
    exp3 = [1,0,1,1]

    result1 = sBox(bits1, S1)
    result2 = sBox(bits2, S2)
    result3 = sBox(bits3, S3)

    print("\n")
    print("\n")
    print("******************************************** sBox Test ****************************************************")
    print("\n")
    print("Receives a length 6 integer array of 0s and 1s and a 2D integer array (one of the S-boxes). Returns the 4-bit conversion ")
    print("\n")
    print(f"Expected Results: Bits 1: {bits1}  Box: {S1}  --->   SBox Value: {exp1}")
    print(f"Expected Results: Bits 1: {bits2}  Box: {S2}  --->   SBox Value: {exp2}")
    print(f"Expected Results: Bits 1: {bits3}  Box: {S3}  --->   SBox Value: {exp3}")
    print("\n")
    print(f"Test one: ... Bits 1: {bits1}  Box: {S1}  --->   SBox Value: {result1}")
    print(f"Test two: ... Bits 1: {bits2}  Box: {S2}  --->   SBox Value: {result2}")
    print(f"Test three: ... Bits 1: {bits3}  Box: {S3}  --->   SBox Value: {result3}")
    print("\n")


def testGenerateK1():

    inp1 = [1 if i in [8,16,24,32,40,48,56,64] else 0 for i in range(64)]
    inp2 = [1 if i == 6 else 0 for i in range(64)]
    inp3 = [1 if i == 23 else 0 for i in range(64)]
    inp4 = [1 if i == 60 else 0 for i in range(64)]
    
    exp1 = [0 for i in range(48)]
    exp2 = [0 for i in range(48)]
    exp3 = [1 if i == 35 else 0 for i in range(48)]
    exp4 = [1 if i == 4 else 0 for i in range(48)]

    result1 = generateK1(inp1)
    result2 = generateK1(inp2)
    result3 = generateK1(inp3)
    result4 = generateK1(inp4)

    print("\n")
    print("\n")
    print("******************************************** Generate k1 Test ****************************************************")
    print("\n")
    print("This function takes in the 64-bit key as an integer array/list of0s and 1s, and outputs the subkey for the first round of DES.")
    print("\n")
    print(f"Expected Results: 64 Bit Input: {inp1}   --->   48 Bit Return: {exp1}")
    print(f"Expected Results: 64 Bit Input: {inp2}   --->   48 Bit Return: {exp2}")
    print(f"Expected Results: 64 Bit Input: {inp3}   --->   48 Bit Return: {exp3}")
    print(f"Expected Results: 64 Bit Input: {inp4}   --->   48 Bit Return: {exp4}")
    print("\n")
    print(f"Test one: ...   64 Bit Input: {inp1}   --->   48 Bit Return: {result1}")
    print(f"Test two: ... 64 Bit Input: {inp2}   --->   48 Bit Return: {result2}")
    print(f"Test three: ... 64 Bit Input: {inp3}   --->   48 Bit Return: {result3}")
    print(f"Test four: ... 64 Bit Input: {inp4}   --->   48 Bit Return: {result4}")
    print("\n")


def testFFunction():

    inp1 = [1 for i in range(32)]
    inp2 = [0 for i in range(32)]
    inp3 = [1 if i < 16 else 0 for i in range(32)]

    key1 = [1 for i in range(48)]
    key2 = [0 for i in range(48)]
    key3 = [0 for i in range(48)]
    
    exp1 = [0 if i in [3,6,7,8,11,14,15,16,19,22,26,31,32] else 1 for i in range(32)]
    exp2 = [0 if i in [3,6,7,8,11,14,15,16,19,22,26,31,32] else 1 for i in range(32)]
    exp3 = [1 if i in [4,9,12,13,14,16,18,20,21,24,29] else 0 for i in range(32)]

    result1 = fFunction(inp1, key1)
    result11 = result1.insert(0,1)
    result2 = fFunction(inp2, key2)
    result22 = result2.insert(0,1)
    result3 = fFunction(inp3, key3)
    result33 = result3.insert(0,0)

    print("\n")
    print("\n")
    print("******************************************** F Function Test ****************************************************")
    print("\n")
    print("This function receives the right half of the per-muted plaintext and the first subkey and outputs the result of the f-function.")
    print("\n")
    print(f"Expected Results: 32 Bit Plaintext: {inp1}   48 bit subkey: {key1}  --->   32 Bit Return: {exp1}")
    print(f"Expected Results: 32 Bit Plaintext: {inp2}   48 bit subkey: {key2}  --->   32 Bit Return: {exp2}")
    print(f"Expected Results: 32 Bit Plaintext: {inp3}   48 bit subkey: {key3}  --->   32 Bit Return: {exp3}")
    print("\n")
    print(f"Test one: ...   32 Bit Plaintext: {inp1}   48 bit subkey: {key1}  --->   32 Bit Return: {result1}")
    print(f"Test two: ... 32 Bit Plaintext: {inp2}   48 bit subkey: {key2}  --->   32 Bit Return: {result2}")
    print(f"Test three: ... 32 Bit Plaintext: {inp3}   48 bit subkey: {key3}  --->   32 Bit Return: {result3}")
    print("\n")
    

def testFeistalNetworkRound():

    inp1 = [1 for i in range(64)]
    inp2 = [0 for i in range(64)]
    inp3 = [0 if i < 60 else 0 for i in range(64)]

    key1 = [1 for i in range(64)]
    key2 = [0 for i in range(64)]
    key3 = [0 for i in range(64)]
    
    exp1 = [0 if i in [33,34,36,37,41,42,44,45,49,50,52,53,55,56,57,59,60,61,62] else 1 for i in range(64)]
    exp2 = [1 if i in [33,34,36,37,41,42,44,45,49,50,52,53,55,56,57,59,60,61,62] else 0 for i in range(64)]
    exp3 = [1 if i in [17,25,33,34,36,37,39,40,41,43,45,50,52,53,54,55,56,57,58,59,60,62] else 0 for i in range(64)]

    result1 = feistalNetworkRound(inp1, key1)
    result2 = feistalNetworkRound(inp2, key2)
    result3 = feistalNetworkRound(inp3, key3)

    print("\n")
    print("\n")
    print("******************************************** Feistal Network Round Test ****************************************************")
    print("\n")
    print("This function receives the 64-bit plain-text and the 64-bit key. It computes the first round of the Fiestal network")
    print("\n")
    print(f"Expected Results: 64 Bit Plaintext: {inp1}   64 bit subkey: {key1}  --->   32-64 Bit Return: {exp1}")
    print(f"Expected Results: 64 Bit Plaintext: {inp2}   64 bit subkey: {key2}  --->   32-64 Bit Return: {exp2}")
    print(f"Expected Results: 64 Bit Plaintext: {inp3}   64 bit subkey: {key3}  --->   32-64 Bit Return: {exp3}")
    print("\n")
    print(f"Test one: ...   64 Bit Plaintext: {inp1}   64 bit subkey: {key1}  --->   32-64 Bit Return: {result1}")
    print(f"Test two: ... 64 Bit Plaintext: {inp2}   64 bit subkey: {key2}  --->   32-64 Bit Return: {result2}")
    print(f"Test three: ...  64 Bit Plaintext: {inp3}   64 bit subkey: {key3}  --->   32-64 Bit Return: {result3}")
    print("\n")


def main(): 
    testBinToInt()
    testIntToBin()
    testXor() 
    testPermute() 
    testSBox() 
    testGenerateK1()
    testFFunction()
    testFeistalNetworkRound()


main()












