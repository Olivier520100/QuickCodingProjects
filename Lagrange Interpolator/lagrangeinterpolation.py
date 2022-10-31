import numpy as np

nodes = np.array([1,1])
nodeamount = np.shape(nodes)[0]
print(nodes)
print(nodeamount)
i = 0
j = 0
functionstring = ""
while i < nodeamount:
    functionstring = functionstring + str(nodes[i,1]) 

    while j < nodeamount:

        if j == i:
            j+=1
        
        if j < nodeamount: 
            functionstring = functionstring + "*(" + "(x-"+ str(nodes[j,0]) +")" + "/("+ str(nodes[i,0]) + "-" + str(nodes[j,0]) +")"+")"
        j+=1
        
    functionstring = functionstring + "+"
    j=0
    i+=1

functionstring = functionstring + "0"

print(functionstring)

