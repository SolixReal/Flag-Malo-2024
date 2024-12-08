import socket
import time

# Server IP and port (replace with the actual server details)
SERVER_HOST = 'localhost'  # Replace with the server's IP if running remotely
SERVER_PORT = 4002        # Replace with the actual port the server is listening on

def main():
    try:
        # Create a TCP/IP socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Connect to the server
            s.connect((SERVER_HOST, SERVER_PORT))
            print("Connected to the server.")

            ## To get the size
            '''
            passwrd = '1'
            delta_t = 0
            while True:
                # Receive the initial prompt from the server
                data = s.recv(1024).decode()
                if not data:
                    break
                print(data)

                # Check if the server is requesting input (e.g., for a PIN attempt)
                if ">>> " in data:
                    # Get the time before sending the PIN
                    start_time = time.time()

                    # Send the PIN code (replace '1234' with your attempt)
                    s.sendall((passwrd + '\n').encode())

                    # Receive the response from the server after sending the PIN
                    response = s.recv(1024).decode()
                    print ('REP: ', response)

                    # Get the time after receiving the response
                    end_time = time.time()

                    # Calculate the round-trip time
                    round_trip_time = end_time - start_time

                    if ("Length doesn't match" not in response):
                        print ('length: ' + passwrd)
                        return 0
                    
                    print (round_trip_time, passwrd)
                    passwrd += '1'
                    delta_t = round_trip_time
            '''
            
            ## tto get the tag, one by one
             # Receive the initial prompt from the server
            data = s.recv(1024).decode()
            print (data)
            size  = 11
            passwd = '0'*size
            
            for si in range (size):
                for guess in range (10):
                    # data = s.recv(1024).decode ()
                    while ('>>>' not in data):
                        data = s.recv(1024).decode ()
                    
                    passwd = list (passwd) 
                    passwd [si] = f'{guess}'
                    passwd = ''.join (passwd)
                    
                    s.sendall((passwd + '\n').encode())
                        
                    data = s.recv(1024).decode ()
                    if (f'{si}' not in data):
                        print (passwd)
                        break
                
                
                if not data:
                    break
                print(data)
            #'''

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
