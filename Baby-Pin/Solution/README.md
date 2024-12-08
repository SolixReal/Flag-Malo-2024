# Flag'Malo 2024

## Baby PIN

Crypto - Easy

### Contenu

En se connectant au challenge avec nc il est demandé de rentrer un code PIN.

Le serveur répond à chaque essai quel est le premier chiffre à être mauvais.
Exemple avec 5485 si le 5 est mauvais : [-] Number 0 doesn't match
Exemple avec 7294 si le 2 est mauvais : [-] Number 1 doesn't match
```
Give me the right PIN code to get the flag!
>>> 0000
[-] Number 0 doesn't match
```

### Résolution

Il faut tout d'abord connaître la taille. Pour cela on peut tester différentes taille jusqu'à ne plus avoir le message d'erreur :
```
[-] Length doesn't match
```
On obtient alors une taille de 4.

On peut ensuite résoudre le challenge à la main ou en réalisant un programme qui va tester pour le premier chiffre toutes les possibilités et quand il obtient la bonne réponse, tester sur le second chiffre ect…

Le fichier ![Solution.py](https://github.com/SolixReal/Flag-Malo-2024/blob/main/Baby-Pin/Solution/solution.py) propose une manière de résoudre le challenge.

Au final si on utilise le code 7491 le serveur retourne : aLittlePIN

### Flag

Le flag est FMCTF{aLittlePIN}
