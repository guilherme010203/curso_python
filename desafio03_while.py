while True:

    numero1= int(input("Digite um numero:  "))
    numero2 = int(input("Digite um numero:  "))

    media = (numero1 + numero2) /2

    if media:
        print(media)

    if numero1 > numero2 :
        print(f"o Maior valor é o {numero1}")
        
    if numero2 >  numero1:
        print(f"o Maior valor é o {numero2}")
    
    
        
    if numero1 < numero2 :
        print(f"o Menor valor é o {numero1}")
        
    if numero2 <  numero1:
        print(f"o Menor valor é o {numero2}")
    
    else:
        continuar = input("Deseja continuar [S/N]:  ").upper()
        if continuar == "N":
            print("SAINDO DO LOOP")
            break
        print("CONTINUANDO NO LOOP")