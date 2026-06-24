import random

def robot():
    objetos = random.choice(["caja", "humano"])
    bateria = random.randint(1, 100)
    metros = random.randint(1, 100)

    if objetos == "caja" and bateria >= 50:
        return f"Me he encontrado con una caja, bateria suficiente para moverla | a {metros} de distancia | {bateria}% de bateria"
    
    elif objetos == "caja" and bateria < 50:
        return f'Me he encontrado una caja, bateria insuficiente para moverla, parar |  a {metros} de distancia | {bateria}% de bateria'
    
    elif objetos == "humano" and bateria >= 50:
        print(f'Me he encontrado con un humano, suficiente bateria para analizarlo |  a {metros} de distancia | {bateria}% de bateria')
    
    elif objetos == "humano" and bateria < 50:
        print(f"Me he encontrado con un humano, bateria insuficiente para analizarlo |  a {metros} de distancia | {bateria}% de bateria")

resultado = robot()
print(resultado)

# Return, a diferendia de print, no imprime los datos como tal, sino que devuelve y ejecuta algo que tu le indiques
    