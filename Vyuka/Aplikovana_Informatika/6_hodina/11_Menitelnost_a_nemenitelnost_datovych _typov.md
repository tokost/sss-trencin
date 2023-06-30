# Menitelnosť a nemenitelnosť dátových typov

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
Keď už sme sa zoznámili so základnými prvkami jazyka: typy hodnôt, premenné a hlavne priradovanie (napr. používanie rovnítka) môžeme sa zoznámiť s prvým zloženým príkazom. Začneme príkazom na opakovanie nejakej činnosti t.j. for-cyklom.
Skôr než k tomu pristúpime zopakujme si niektoré veci ktoré súvisia s priradením nejakej hodnoty.
~~~
meno = input('ako sa volas? ')
print('ahoj', meno)
~~~
V tomto príklade sa využíva funkcia input(), ktorá zastaví bežiaci výpočet, vypýta si od používateľa zadať nejaký text a tento uloží do premennej meno. Na koniec toto zadané meno vypíše. Program spustíme klávesom F5. Beh programu v konzolovom okne (shell pythonu) môže vyzerať napr. takto
~~~
ako sa volas? Jozef
ahoj Jozef
>>>
~~~
Týmto program skončil a môžeme pokračovať aj v skúmaní premenných, napr. v programovom režime zistíme hodnotu premennej meno:
~~~
>>> meno
'Jozef'
~~~
V našich budúcich programoch bude bežné, že na začiatku sa vypýtajú hodnoty nejakých premenných a ďalej program pracuje s nimi.

Ďalší program ukazuje, ako to vyzerá, keď chceme načítať nejaké číslo:
~~~
cislo = input('zadaj cenu jedneho vyrobku: ')
spolu = cislo * 4
print('4 vyrobky stoja', spolu, 'euro')
~~~
Týmto programom sme chceli prečítať cenu jedného výrobku a z toho vypočítať, aká je cena 4 takýchto výrobkov. Po spustení programu dostávame:
~~~
zadaj cenu jedneho vyrobku: 1.2
4 vyrobky stoja 1.21.21.21.2 euro
~~~
Takýto výsledok je zrejme nesprávny: očakávali sme celkovú cenu 4.8 euro. Problémom tu bolo to, že funkcia input() zadanú hodnotu vráti nie ako číslo, ale ako znakový reťazec, teda '1.2'. Na tomto mieste potrebujeme takýto reťazec **prekonvertovať** na desatinné číslo. Využijeme jednu z troch konvertovacích (pretypovacích) funkcií:
># Pretypovanie hodnôt
Mená typov int, float a str zároveň súžia ako mená pretypovacích funkcií, ktoré dokážu z jedného typu vyrobiť hodnotu iného typu:

* int(hodnota) z danej hodnoty vyrobí celé číslo, napr.
    *   int(3.14) => 3
    *   int('37') => 37
* float(hodnota) z danej hodnoty vyrobí desatinné číslo, napr.
    *   float(333) => 333.0
    *   float('3.14') => 3.14
*   str(hodnota) z danej hodnoty vyrobí znakový reťazec, napr.
**      str(356) => '356'
    *   str(3.14) => '3.14'
    *   
Zrejme pretypovanie reťazca na číslo bude fungovať len vtedy, keď je to správne zadaný reťazec, inak funkcia vyhlási chybu.

Aby náš program poskytol správny výsledok, potom po pretypovan=i bude vyzerať takto:
~~~
cislo_str = input('zadaj cenu jedneho vyrobku: ')
cislo = float(cislo_str)       # pretypovanie
spolu = cislo * 4
print('4 vyrobky stoja', spolu, 'euro')
~~~