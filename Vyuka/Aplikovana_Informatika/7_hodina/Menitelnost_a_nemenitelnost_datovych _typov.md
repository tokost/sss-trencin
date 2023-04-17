Udajové typy rozlišujeme aj podla toho, či ich hodnoty môžeme měnit apodľa toho poznáme:

* **nemenitelné (immutable)** typy ku ktorým patrí int, float, bool, str, tuple.
* **menitelné (mutable)** typy ku ktorým patrí list, set, dict

Toto rozlišenie je dôležité napríklad pri využití slovníkov – slovníky môžeme totiž indexovat iba tie ktoré obsahujú nemenitelné typy.

### Pretypovanie
Názvy typov sú súčasne názvami tzv.vstavaných funkcí, ktoré uskutočnia tzv. **pretypovanie**. Typy premenných sú veľmi dôležité a je im potrebné venovať zvýšenú pozornosť a ev. kontrolu pomocou funkcie type(). Ovlyvňujú napríklad význam operátorov. Typický príklad je pretypovanie čísla na retezec:
~~~
x = 15      # x predstavuje celé číslo
print(x)    # vypíše 15
print(3*x)  # vypíše 45
x = str(x)  # pretypovanie na re+tazec, x teraz nepredstavuje celé číslo, ale kombináciu znakov "15"
print(x)    # vypíše 15 (tu sa ešte rozdiel typu neprejaví)
print(3*x)  # vypíše 3x 15 t.j. 151515 (pretože x je teraz retazec a operácia * pre retťazec znamená opakované zreťazenie)
~~~

Pretypovanie alebo použitie konverzných funkcii (ktoré spôsobia zmenu typu premennej):
* celociselnapremenna = int(premenna) napr.\
a=int(2.7) ... v premennej a bude celé číslo 2
b=int(-3.14) ... v premennej b bude celé číslo -3
c=int(‘524’) ... v premennej c bude celé číslo 524

* realnapremenna = float(premenna) napr. \
d=float(2) ... v premennej d bude reálne číslo 2.0
e=float(‘-3.14’) ... v premennej e bude číslo -3.14

* retazec = str(premenna) napr.\ 
w=str(27) ... v premennej w bude reťazec ‘27’

* vyber nahodnej farby z n-tice mojefarby pomocou knižnice obsahujúcej funkciu random
~~~
import random
mojefarby=(‘red’‚ ‘ pink’, ‘ purple ‘, ‘#A0FF54’)
vybrana_farba=random.choice(mojefarby)
print(f"Vybrana farba je :", vybrana_farba)
~~~