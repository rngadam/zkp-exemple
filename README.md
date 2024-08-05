# Preuve à divulgation nulle de connaissance (Zero-knowledge proof) ZKP

## Introduction

Un exemple d'une communication entre un agent alice et un agent bob où alice doit prouver à bob qu'elle connait x mais sans révéler la valeur de x.

Pour ce faire, nous utilisons:

* loi des exposants
* des fonctions non-réversible

## lois des exposants

NB: ```x**y``` est x à la puissance y en Python (et non pas x^y, qui est bitwise XOR!)

```
x**a * x**b = x**(a+b)
```

et 

```
(x**a)**b = x**(a*b)
```

## fonction non-réversible

 facile à calculée, il n'est pas possible de trouver la variable d'entrée puisque la valeur vient d'un restant d'une division i.e. modulo

```
f(x) = g ** x % p
```

où 

* g est une constante connue de alice et bob
* p est un nombre premier connu de alice et bob
* x est le secret que seul alice connait

## communication interprocessus


Nous lançons un processus par agent avec une communication par deux canaux nommés (type FIFO), un de alice vers bob et un de bob vers alice.


## Sortie exemple

terminal 1:

```bash
$ python3 alice.py 
créé ./zkp.alice.fifo
r=510 x=83
g=240 p=320902338832813374930143536447 fx=223780349919490882457807813796, fr=295709063760314061456845428928
notification du pair de la fin de session
```

terminal 2:

```bash
$ python3 bob.py 
créé ./zkp.bob.fifo
g=240 p=320902338832813374930143536447 fx=223780349919490882457807813796, fr=295709063760314061456845428928
le pair connait le secret de x
```

## Références

* [Comparing Information Without Leaking It](https://www.stat.berkeley.edu/~aldous/157/Papers/fagin.pdf)
* [ZKP Math - High School Edition](https://www.youtube.com/watch?v=sKEabURqj28)
* [Kazui Sako Zero Knowledge Proof 101 Notes from IIW 26](https://github.com/afroDC/Personal/wiki/Kazui-Sako-Zero-Knowledge-Proof-101-Notes-from-IIW-26)
