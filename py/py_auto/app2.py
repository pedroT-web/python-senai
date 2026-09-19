import pyautogui as gui
import pandas as pd
import time

# Segurança e velocidade 
gui.PAUSE = 0.5
gui.FAILSAFE = True

# 1. Carregar a planilha ajusta
df = pd.read_excel("Clientes.xlsx")

# 2. Abre o bloco de notas para testar o preenchimento
gui.press("win")
gui.write('bloco de notas')
gui.press("enter")

time.sleep(2)

# 3. Executa a automação para cada registro 
print("iniciando a automação...")

# 4.
for index, linha in df.iterrows():
    gui.write(f'--- Cliente # {index + 1} ---', interval=0.02)
    gui.press('enter')

    gui.write(f'Nome: {linha['Nome']}', interval=0.02)
    gui.press('enter')

    gui.write(f'Email: {linha['Email']}', interval=0.02)
    gui.press('enter')
    
    gui.write(f'Telefone: {linha["Telefone"]}', interval=0.02)
    gui.press('enter')

    gui.press('enter')
    time.sleep(0.5)
print("Automação Concluída")
