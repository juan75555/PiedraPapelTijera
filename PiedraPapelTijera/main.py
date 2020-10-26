import random #Importamos random para que la maquina haga jugadas aleatorias.

print("Bienvenido al juego de Piedra,Papel o Tijera :) \n")

username= input("Dime el nombre de usuario: ") #Se inserta el nombre de usuario.

user_choice= input("Elige P/S/R: ") #Se elige la jugada que se desea realizar.

pc_choice = 'P','S','R' #Definimos que jugadas puede hacer la maquina.

pc_choice=random.choice(pc_choice) #El ordenador hace jugadas aleatorias segun las que hemos definido.

#Definimos segun nuestras jugadas y las de la maquina cuando ganamos,perdemos o empatamos.
if user_choice=='P' and pc_choice=='S':
    print("La maquina ha ganado :(")
elif user_choice=='P' and pc_choice=='R':
    print(username + " has ganado :)")
elif user_choice=='P' and pc_choice=='P':
    print("Empate")
elif user_choice=='S' and pc_choice=='S':
     print("Empate")
elif user_choice=='S' and pc_choice=='R':
    print("La maquina ha ganado :(")
elif user_choice=='S' and pc_choice=='P':
    print(username + "has ganado :)")
elif user_choice=='R' and pc_choice=='R':
     print("Empate")
elif user_choice=='R' and pc_choice=='P':
    print("La maquina ha ganado :(")
elif user_choice=='R' and pc_choice=='S':
    print(username + "has ganado :)")



