# Flag'Malo 2024

## Connexion vétuste

Réseau - Easy

### Contenu

Le challenge est composé d’un fichier wireshark.

### Résolution

Dans le contenu du fichier wireshark on remarque des échanges avec le protocole Telnet.

C'est un protocole reconnu comme vulnérable, qui ne chiffre pas les échanges.

Afin de facilement observer les échanges, on peut filtrer les trames telnet :

![Image1](img/Solution1.png)

Puis suivre les flux en se rendant dans *Analyser* / *Suivre* / *TCP Steam* :

![Image2](img/Solution2.png)

![Image3](img/Solution3.png)

On peut voir que le mot de passe est superSecret22.

### Flag

Le flag est FMCTF{superSecret22}
