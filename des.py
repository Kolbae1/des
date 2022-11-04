import tools
import constants 




# main 



#print(binToInt(bits))


#intToBin(2, 20)

a = [0,1,1,0,0,0]
b = [3,1,5,2,4,1,3]

#xor(a,b)
#print(permute(a,b))
bits = []
for i in range(64):
    bits.append(0)
    bits.append(1)

print(tools.generateK1(bits))
