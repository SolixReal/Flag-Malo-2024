#!/usr/local/bin/python3

from time import sleep

def verify_pin(attempt, pin):
    if len(attempt) != len(pin):
        return False
    sleep(0.1)
    for i in range(len(pin)):
        if pin[i] != attempt[i]:
            return False
        sleep(0.1)

    return True

if __name__ == "__main__":

    with open("pin.txt", "r") as fp:
        pin = fp.read().strip()

    while True:
        print("Give me the right PIN code to get the flag!")
        try:
            pin_attempt = input(">>> ").strip()
            pin_check = verify_pin(pin_attempt, pin)

            if pin_check:
                with open("flag.txt", "rb") as fp:
                    flag = fp.read().strip().decode()
                print(f"\t[+] Congratulations! Here is the flag : {flag}")
                break
        except:
            break
