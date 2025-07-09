vogais=["a","e","i","o","u"]
letras=["a","e","f","g","h","i",]

def filtrar_vogais(a,b):
   
 for filtrados in b:
        if filtrados in a:
            print(filtrados)

filtrar_vogais(vogais,letras)
