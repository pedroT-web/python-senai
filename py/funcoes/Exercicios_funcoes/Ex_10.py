# Validador de senha:
# Crie uma função que receba uma senha como parâmetro e verifique se ela atende aos 
# seguintes requisitos:
# Possui no mínimo 8 caracteres Contém pelo menos uma letra maiúscula Contém pelo menos uma 
# letra minúscula Contém pelo menos um número Contém pelo menos um caractere especial A função 
# deve retornar True se a senha for válida ou False caso contrário.
import re

def validarSenha(senha):
   comprimento = len(senha) >= 8
   maiuscula = re.search("[A-Z]", senha)
   minuscula = re.search("[a-z]", senha)
   numero = re.search("[0-9]", senha)
   especial = re.search(r"[@!#$%¨&*()?:;^~`´]", senha)
   
   if comprimento and maiuscula and minuscula and numero and especial:
    print("Parabéns, senha válida!!")
    return True;
   else:
       print("Senha incorreta!!")
       print(""" A senha deve seguir o padrão a seguir
        - mínimo de 8 caracteres
        - pelo menos uma letra maiúscula
        - pelo menos uma letra minúscula
        - pelo menos um número             
        """)
       return False
       
   
    
validarSenha("Oa!*2")
            