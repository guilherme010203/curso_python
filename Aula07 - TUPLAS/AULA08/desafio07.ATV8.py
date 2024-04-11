matriz= [[0,0,0],[1,1,1],[2,2,2]]
c=0

for i in range (0,3):
   
    for j in matriz[i]:
       
        if c==3:
            c=0
                 
        numero= int(input(f"Digite um valor para[{i},{c}]: "))
       
        matriz[i][c]=numero    
        c +=1
       
# print(matriz)
print(matriz[0])
print(matriz[1])
print(matriz[2])

# matriz[0][1] ="joão"
# print(matriz)


# print(matriz[0][0])
# print(matriz[0][1])
# print(matriz[0][2])