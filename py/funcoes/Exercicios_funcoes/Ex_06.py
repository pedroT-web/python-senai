# Conversor de temperatura:
# Crie uma função que receba um valor de temperatura em graus Celsius como parâmetro e 
# retorne o valor equivalente em graus Fahrenheit.

def graus_farenheit(graus):
    farenheit = (graus * 1.8) + 32
    
    print(f"{graus}°C em farenheit equivale: {farenheit}°F")
    
graus_farenheit(30)