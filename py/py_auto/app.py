import pyautogui
import time

# pequena pausa de segurança entre os comandos (0.5s)
pyautogui.PAUSE = 0.5

# 1. Pressionar a tecla Windows para abrir o menu Iniciar 
pyautogui.press('win')

# 2. Digitar 'bloco de notas' e pressionar Enter para abrir
pyautogui.write("bloco de notas", interval=0.05)
pyautogui.press('enter')

# 3. Aguardar 2 segundos para a janela carregar completamente
time.sleep(2)

# 4. Digitar a mensagem com um pequeno intervalo entre cada letra
pyautogui.write('Hello World')