# Flag'Malo 2024

## Connexion vétuste

Réseau - Easy

### Contenu

Le challenge est composé d’un fichier wireshark.

### Résolution

Dans le contenu du fichier wireshark on remarque des échanges avec le protocole Telnet.

C'est un protocole reconnu comme vulnérable, qui ne chiffre pas les échanges.

Afin de facilement observer les échanges, on peut filtrer les trames telnet :

<img src="img/solution1.png" alt="solution1" width="auto" height="300">

Puis suivre les flux en se rendant dans *Analyser* / *Suivre* / *TCP Steam* :

<img src="img/solution2.png" alt="solution2" width="auto" height="300">

<img src="img/solution3.png" alt="solution3" width="auto" height="300">

On peut voir que le mot de passe est superSecret22.

### Flag

Le flag est FMCTF{superSecret22}
