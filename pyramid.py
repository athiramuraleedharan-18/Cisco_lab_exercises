#Your task is to write a program which reads the number of blocks the builders have, and outputs the height of the pyramid that can be built using these blocks.
'''
Note: the height is measured by the number of fully completed layers – 
if the builders don't have a sufficient number of blocks and cannot complete the next layer, 
they finish their work immediately.
'''

blocks = int(input("Enter the number of blocks: "))
height=0
for i in range(blocks):
    if blocks==0:
        break
    elif blocks <= i:
        break
    else:
        height+=1
        blocks-=height
        
print("The height of the pyramid:", height)

