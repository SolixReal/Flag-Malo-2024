# Flag'Malo 2024

## Daddy PIN

Crypto - Medium

### Contenu

En se connectant au challenge avec nc il est demandé de rentrer un code PIN.

Le serveur répond à chaque essai la position du premier chiffre à être mauvais.

Exemple avec 5485 si le 5 est mauvais : [-] Number 0 doesn't match \
Exemple avec 7294 si le 2 est mauvais : [-] Number 1 doesn't match
```
Give me the right PIN code to get the flag!
>>> 0000
[-] Number 0 doesn't match
```

### Résolution

Il faut tout d'abord connaître la taille. Pour cela on peut tester différentes tailles jusqu'à ne plus avoir le message d'erreur :
```
[-] Length doesn't match
```
On obtient alors une taille de 11.

Au vu de la taille du code PIN, on ne peut le résoudre à la main sans y passer énormément de temps. Il est donc nécessaire de réaliser un programme qui va tester pour le premier chiffre toutes les possibilités et quand il obtient la bonne réponse, tester sur le second chiffre ect…

Le fichier ![solution.py](solution.py) propose une manière de résoudre le challenge.

Au final, si on utilise le code 91583320932 le serveur retourne : FMCTF{lookAtHisMuscle}

### Flag

Le flag est FMCTF{lookAtHisMuscle}

