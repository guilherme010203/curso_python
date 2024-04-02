escolhaUsuario = input("informe a sua escolha:  ").upper()
from random import choice
opcoes = ["PEDRA", "PAPEL", "TESOURA"]
escolhaMaquina = choice(opcoes)
print(escolhaMaquina)

if escolhaMaquina == escolhaUsuario:
    print(f"EMPATE, AMBOS ESCOLHERAM {escolhaMaquina}, PORTATANTO DEU EMPATE")
    
elif escolhaMaquina == "PEDRA" and escolhaUsuario == "TESOURA" :
    print(f"A MAQUINA ESCOLHEU {escolhaMaquina}, PORTANTO ELA VENCEU")  
    
elif escolhaMaquina == "TESOURA" and escolhaUsuario == "PAPEL":
    print(f"A MAQUINA ESCOLHEU {escolhaMaquina}, PORTANTO ELA VENCEU")  
     
elif escolhaMaquina == "PAPEL" and escolhaUsuario == "PEDRA":
    print(f"A MAQUINA ESCOLHEU {escolhaMaquina}, PORTANTO ELA VENCEU")  
    
    
    
elif escolhaUsuario == "PEDRA" and escolhaMaquina == "TESOURA" :
    
    print(f"O USUARIO ESCOLHEU {escolhaUsuario}, PORTANTO ELE VENCEU")  
    
elif escolhaUsuario == "TESOURA" and escolhaMaquina == "PAPEL":
    print(f"O USUARIO ESCOLHEU {escolhaUsuario}, PORTANTO ELE VENCEU")    
    
elif escolhaUsuario == "PAPEL" and escolhaMaquina== "PEDRA":
    print(f"O USUARIO ESCOLHEU {escolhaUsuario}, PORTANTO ELE VENCEU")   
    
    

