# Flag'Malo 2024

## Grandpa PIN

Crypto - Medium

### Contenu

En se connectant au challenge avec nc il est demandé de rentrer un code PIN.

Le serveur répond uniquement pour dire si le code PIN est bon et ne donne aucune autre information.
```
Give me the right PIN code to get the flag!
>>>
```

### Résolution

Etant donné que nous n'avons pas d'information et que, comme le dit l'énoncé, il ne faut pas passer par du brute force, on va utiliser une technique de side-channel, en observant les temps d'exécution.

Il faut tout d'abord connaître la taille. Pour cela on peut tester différentes tailles de chaîne de 0 et observer celle où le temps d'exécution est le plus important.

Voici un programme correspondant :

```
def main():
    try:
        # Create a TCP/IP socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Connect to the server
            s.connect((SERVER_HOST, SERVER_PORT))
            print("Connected to the server.")

            ## To get the size
            #'''
            # Receive the initial prompt from the server
            data = s.recv(1024).decode()
            print (data)
            end_size = 20
            delta = np.zeros(end_size)

            for i in range(end_size):
                while ('>>>' not in data):
                    data = s.recv(1024).decode ()

                t0 = time.time ()
                passwd = '0'*i

                s.sendall((passwd + '\n').encode())
                data = s.recv(1024).decode ()
                t1 = time.time ()

                delta[i] = t1 - t0
                print(data, delta[i], i)

            tmp_res = np.argmax(delta)
            print(f"------------------")
            print(f"Taille : {tmp_res}")
```

On obtient alors une taille de 8.

On va maintenant tester pour chaque chiffre les 10 possibilités en mesurant le temps puis on enregistrera le chiffre correspondant à la valeur la plus importante.

```
## To get the PIN
            print (data)
            passwd = '0'*size

            # while (True):
            for i in range(size):
                times = np.zeros(10)  # Réinitialise les temps pour chaque position du mot de passe
                if i == size - 1:
                    print(f"Traitement de la dernière position {i}")
                    for j in range(10):
                        passwd = list(passwd)  # Convertit passwd en liste pour modification
                        passwd[i] = f'{j}'  # Essaye la valeur actuelle
                        passwd = ''.join(passwd)  # Reconstruit passwd comme une chaîne

                        s.sendall((passwd + '\n').encode())  # Envoie le mot de passe
                        data = s.recv(1024).decode()  # Reçoit la réponse
                        if '[+]' in data:
                                print(f"Succès détecté : {data}")
                                print("Programme terminé.")
                                exit(0)  # Quitte le programme ou termine proprement



                for j in range(10):  # Teste toutes les valeurs possibles (0 à 9)
                    start_time = time.time()
                    while '>>>' not in data :
                        data = s.recv(1024).decode()

                    t0 = time.time()
                    passwd = list(passwd)  # Convertit passwd en liste pour modification
                    passwd[i] = f'{j}'  # Essaye la valeur actuelle
                    passwd = ''.join(passwd)  # Reconstruit passwd comme une chaîne

                    s.sendall((passwd + '\n').encode())  # Envoie le mot de passe
                    data = s.recv(1024).decode()  # Reçoit la réponse
                    t1 = time.time()

                    times[j] = t1 - t0  # Stocke le temps pour cette tentative
                    #print(f"Temps pour la position {i}, valeur {j} : {times[j]}")

                # Trouve la valeur de j correspondant au temps maximum
                tmp_res = np.argmax(times)
                print(f"Position {i}, meilleure valeur : {tmp_res}")

                # Met à jour la position i du mot de passe
                passwd = list(passwd)
                passwd[i] = f'{tmp_res}'
                passwd = ''.join(passwd)

            print(f"Mot de passe final : {passwd}")


    except Exception as e:
        print(f"An error occurred: {e}")
```

Le fichier ![solution.py](solution.py) propose un programme complet pour résoudre le challenge.

Au final si on utilise le code 82795215 le serveur retourne : FMCTF{anOldPinCode}

### Flag

Le flag est FMCTF{anOldPinCode}

