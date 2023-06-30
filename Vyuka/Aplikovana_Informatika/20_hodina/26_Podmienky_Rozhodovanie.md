># Podmienky

>## Podmienený príkaz if - else

Pri programovaní často riešime situácie, keď sa program má na základe nejakej podmienky rozhodnúť medzi viacerými možnosťami. Napr. program má vypísať, či zadaný počet bodov stačí na známku z predmetu. Preto si najprv vyžiada číslo - získaný počet bodov, **porovná** túto hodnotu s požadovanou hranicou, napr. 50 bodov a na základe toho vypíše, buď že je to dosť na známku, alebo nie je:
~~~
body = int(input('Zadaj získaný počet bodov: '))
if body >= 50:
    print(body, 'bodov je dostačujúci počet na známku')
else:
    print(body, 'bodov je málo na získanie známky')
~~~
Použili sme tu podmienený príkaz (príkaz vetvenia) **if**. Jeho zápis vyzerá takto:
~~~
if podmienka:    # ak podmienka platí, vykonaj 1. skupinu príkazov
    prikaz
    prikaz
    ...
else:            # ak podmienka neplatí, vykonaj 2. skupinu príkazov
    prikaz
    prikaz
    ...
~~~
V našom príklade sú v oboch skupinách príkazov len po jednom príkaze print(). Odsadenie skupiny príkazov (blok príkazov) má rovnaký význam ako vo for-cykle: budeme ich **odsadzovať vždy presne o 4 medzery**.

V pravidlách predmetu programovanie máme takéto kritériá na získanie známky:

známka A za 90 a viac
známka B za 80
známka C za 70
známka D za 60
známka E za 50
známka Fx za menej ako 50
Podmienka pre získanie známky A:
~~~
if body >= 90:
    print('za', body, 'bodov získavaš známku A')
else:
    ...
~~~
Ak je bodov menej ako 90, už to môže byť len horšia známka: dopíšeme testovanie aj známky B:
~~~
if body >= 90:
    print('za', body, 'bodov získavaš známku A')
else:
    if body >= 80:
        print('za', body, 'bodov získavaš známku B')
    else:
        ...
~~~
Všetky riadky v druhej skupine príkazov (za else) musia byť odsadené o 4 medzery, preto napr. print(), ktorý vypisuje správu o známke B je odsunutý o 8 medzier. Podobným spôsobom zapíšeme všetky zvyšné podmienky:
~~~
body = int(input('Zadaj získaný počet bodov: '))
if body >= 90:
    print('za', body, 'bodov získavaš známku A')
else:
    if body >= 80:
        print('za', body, 'bodov získavaš známku B')
    else:
        if body >= 70:
            print('za', body, 'bodov získavaš známku C')
        else:
            if body >= 60:
                print('za', body, 'bodov získavaš známku D')
            else:
                if body >= 50:
                    print('za', body, 'bodov získavaš známku E')
                else:
                    print('za', body, 'bodov si nevyhovel a máš známku Fx')
~~~
akéto odsadzovanie príkazov je v Pythone veľmi dôležité a musíme byť pritom veľmi presní. Príkaz if, ktorý sa nachádza vo vnútri niektorej vetvy iného if, sa nazýva **vnorený príkaz if**.

>## Vnorený príkaz elif
V Pythone existuje konštrukcia, ktorá uľahčuje takúto vnorenú sériu if-ov:
~~~
if podmienka_1:      # ak podmienka_1 platí, vykonaj 1. skupinu príkazov
    prikaz
    ...
elif podmienka_2:    # ak podmienka_1 neplatí, ale platí podmienka_2, ...
    prikaz
    ...
elif podmienka_3:    # ak ani podmienka_1 ani podmienka_2 neplatia, ale platí podmienka_3, ...
    prikaz
    ...
else:                # ak žiadna z podmienok neplatí, ...
    prikaz
    ...
~~~
Ukážme ešte jedno riešenie tejto úlohy - jednotlivé podmienky zapíšeme ako intervaly:
~~~
body = int(input('Zadaj získaný počet bodov: '))
if body >= 90:
    print('za', body, 'bodov získavaš známku A')
if 80 <= body < 90:
    print('za', body, 'bodov získavaš známku B')
if 70 <= body < 80:
    print('za', body, 'bodov získavaš známku C')
if 60 <= body < 70:
    print('za', body, 'bodov získavaš známku D')
if 50 <= body < 60:
    print('za', body, 'bodov získavaš známku E')
if body < 50:
    print('za', body, 'bodov si nevyhovel a máš známku Fx')
~~~
>V tomto riešení využívame to, že **else-vetva v príkaze if môže chýbať** a teda pri neplatnej podmienke, sa nevykoná nič:

~~~
if podmienka:        # ak podmienka platí, vykonaj skupinu príkazov
    prikaz
    prikaz
    ...              # ak podmienka neplatí, nevykonaj nič
~~~
Zrejme každý príkaz if po kontrole podmienky (a prípadnom výpise správy) pokračuje na ďalšom príkaze, ktorý nasleduje za ním (a má rovnaké odsadenie ako if). Okrem toho vidíme, že teraz sú niektoré podmienky trochu zložitejšie, lebo testujeme, či sa hodnota nachádza v nejakom intervale. (podmienku 80 <= body < 90 sme mohli zapísať aj takto 90 > body >= 80)

V Pythone môžeme zapisovať podmienky podobne, ako je to bežné v matematike. Treba si však uvedomiť že príkaz je vyhodnotený ako True ak zápis platí a False ak nie:
| Zápis    | Popis                                                                    |
|-----------|---------------------------------------------------------------------------|
| body < 90 | je menšie ako 90
|body <= 50| je menšie alebo rovné ako 50
| body == 50 | rovná sa 50
|body != 77| nerovná sa 77
| body > 100 | je väčšie ako 100
|body >= 90| je väčšie alebo rovné ako 90
| 40 < body <= 50 | je väčšie ako 40 a zároveň menšie alebo rovné ako 50
|a < b < c| a je menšie ako b a zároveň je b menšie ako c

Ukážme použitie podmieneného príkazu aj v grafickom programe. Program na náhodné pozície nakreslí 1000 malých krúžkov, pričom tie z nich, ktoré sú v ľavej polovici plochy budú červené a zvyšné v pravej polovici (teda else vetva) budú modré:
~~~
import tkinter  # vyuzijeme funkcie z kniznice co
import random   # zapiseme prikazom import

canvas = tkinter.Canvas(bg='white', width=300, height=300)
canvas.pack()

for i in range(1000):
    x = random.randrange(300)
    y = random.randrange(300)
    if x < 150:
        farba = 'red'
    else:
        farba = 'blue'
    canvas.create_oval(x-5, y-5, x+5, y+5, fill=farba, outline='')
~~~
Skúsme pridať ešte jednu podmienku: všetky bodky v spodnej polovici (y > 150) budú zelené, takže rozdelenie na červené a modré bude len v hornej polovici. Jedno z možných riešení:
~~~
import tkinter
import random

canvas = tkinter.Canvas(bg='white', width=300, height=300)
canvas.pack()

for i in range(1000):
    x = random.randrange(300)
    y = random.randrange(300)
    if y < 150:
        if x < 150:
            farba = 'red'
        else:
            farba = 'blue'
    else:
        farba = 'green'
    canvas.create_oval(x-5, y-5, x+5, y+5, fill=farba, outline='')
~~~
Podobne, ako sme to robili s intervalmi bodov pre rôzne známky, môžeme aj toto riešenie zapísať tak, že použijeme komplexnejšiu podmienku:
~~~
import tkinter
import random

canvas = tkinter.Canvas(bg='white', width=300, height=300)
canvas.pack()

for i in range(1000):
    x = random.randrange(300)
    y = random.randrange(300)
    if y < 150 and x < 150:
        farba = 'red'
    elif y < 150 and x >= 150:
        farba = 'blue'
    else:
        farba = 'darkgreen'
    canvas.create_oval(x-5, y-5, x+5, y+5, fill=farba, outline='')
~~~

Podmienky v Pythone môžu obsahovať logické operácie - majú obvyklý význam ako sa používajú v matematike:

* podmienka1 **and** podmienka2 … (a súčasne) znamená, že musia platiť obe podmienky
* podmienka1 **or** podmienka2 … (alebo) znamená, že musí platiť aspoň jedna z podmienok
*  podmienka **not**… (neplatí) znamená, že daná podmienka neplatí

Otestovať rôzne kombinácie podmienok môžeme napr. takto:
~~~
>>> a = 10
>>> b = 7
>>> a < b
False
>>> a >= b + 3
True
>>> b < a < 2 * b
True
>>> a != 7 and b == a - 3
True
>>> a == 7 or b == 10
False
>>> not a == b
True
>>> 1 == '1'
False
>>> 1 < '2'
...
TypeError: unorderable types: int() < str()
~~~

Všimnite si, že podmienky ktoré platia, majú hodnotu True a ktoré neplatia, majú False - sú to dve špeciálne hodnoty, ktoré Python používa ako výsledky porovnávania - tzv. logických výrazov. Sú logického typu, tzv. bool. Môžeme to skontrolovať:

~~~
>>> type(1 + 2)
<class 'int'>
>>> type(1 / 2)
<class 'float'>
>>> type('12')
<class 'str'>
>>> type(1 < 2)
<class 'bool'>
~~~

V prípadoch, keď Python očakáva logickú hodnotu (napr. v príkaze if, alebo v operáciách and, or, not) môžeme uvádzať aj hodnoty iných typov. Napr.
~~~
pocet = int(input('zadaj:'))
if pocet:
    print('pocet je rôzny od 0')
else:
    print('pocet je 0')
meno = input('zadaj:')
if meno:
    print('meno nie je prázdny reťazec')
else:
    print('meno je prázdny reťazec')
~~~

Logické operácie majú v skutočnosti trochu rozšírenú interpretáciu:

>**operácia: prvý and druhý**

* ak **prvý** nie je False, tak
    * výsledkom je **druhý**
* inak (teda **prvý** je False)
    * výsledkom je **prvý**

>**operácia: prvý or druhý**

* ak **prvý** nie je False, tak
    * výsledkom je **prvý**
* inak (teda **prvý** je False)
    * výsledkom je **druhý**

>**operácia: not prvý**

* ak **prvý** nie je False, tak
    * výsledkom je False
* inak
    *výsledkom je True

Napr.
~~~
>>> 1 + 2 and 3 + 4       # keďže 1+2 nie je False, výsledkom je 3+4
7
>>> 'ahoj' or 'Python'    # keďže 'ahoj' nie je False, výsledkom je 'ahoj'
'ahoj'
>>> '' or 'Python'        # keďže '' je False, výsledkom je 'Python'
'Python'
>>> 3 < 4 and 'kuk'       # keďže 3<4 nie je False, výsledkom je 'kuk'
'kuk'
~~~

>### Podmienený príkaz sa často používa pri náhodnom rozhodovaní. 

Napr. hádžeme mincou (náhodné hodnoty 0 a 1) a ak padne 1, kreslíme náhodnú kružnicu, inak náhodný štvorec. Toto opakujeme 10-krát:
~~~
# je potrebné inštalovat knižnicu: $ pip install tkinter

import tkinter  # vyuzijeme funkcie z kniznice co
                # tkinter je rozhranie pythonu k GUI Tcl/Tk
import random   # zapiseme prikazom import

# metoda na pripravu pracovneho ramca - okna
canvas = tkinter.Canvas(bg='white', width=300, height=300)

# metoda ktora sposobi vytvorenie pracovneho ramca - okna
canvas.pack()


for i in range(10):
    x = random.randrange(300)
    y = random.randrange(300)
    a = random.randrange(5, 50)

    if random.randrange(2):     # t.j. random.randrange(2) != 0
        # vytvorenie a umiestnenie kruzku v pracovnom ramci
        canvas.create_oval(x-a, y-a, x+a, y+a)
    else:
        canvas.create_rectangle(x-a, y-a, x+a, y+a)

# zobrazenie pracovneho ramca
canvas.mainloop()
~~~

Približne rovnaké výsledky by sme dostali, ak by sme hádzali kockou so 6 možnosťami (random.randrange(1, 7)) a pre čísla 1, 2, 3 by sme kreslili kružnicu inak štvorec.

Túto myšlienku môžeme využiť aj pre takúto úlohu: vygenerujte 1000 farebných štvorčekov - modré a červené, pričom ich pomer je **1:50**, t.j. na 50 červených štvorčekov pripadne približne 1 modrý:
~~~
import tkinter  # vyuzijeme funkcie z kniznice co
                # tkinter je rozhranie pythonu k GUI Tcl/Tk
import random   # zapiseme prikazom import

# metoda na pripravu pracovneho ramca
canvas = tkinter.Canvas(bg='white', width=300, height=300)
# vytvorenie pracovneho ramca
canvas.pack()

for i in range(1000):
    x = random.randrange(300)
    y = random.randrange(300)
    if random.randrange(50):       # t.j. random.randrange(50) != 0
        farba = 'red'
    else:
        farba = 'blue'

    # vytvorenie a umiestnenie kruzku v pracovnom ramci
    canvas.create_rectangle(x-5, y-5, x+5, y+5, fill=farba, outline='')

# zobrazenie pracovneho ramca
canvas.mainloop()
~~~

Ďalší príklad zisťuje, akých deliteľov má zadané číslo:
~~~
cislo = int(input('Zadaj číslo: '))
pocet = 0
print('delitele:', end=' ')
for delitel in range(1, cislo+1):
    if cislo % delitel == 0:
        pocet += 1
        print(delitel, end=' ')
print()
print('počet deliteľov:', pocet)
~~~

Výstup môže byť napríklad takýto:
~~~
Zadaj číslo: 100
delitele: 1 2 4 5 10 20 25 50 100
počet deliteľov: 9
~~~

Malou modifikáciou tejto úlohy vieme urobiť ďalšie dva programy. 

Prvý zisťuje, či je číslo prvočíslo:
~~~
cislo = int(input('Zadaj číslo: '))
pocet = 0
for delitel in range(1, cislo+1):
    if cislo % delitel == 0:
        pocet += 1
if pocet == 2:
    print(cislo, 'je prvočíslo')
else:
    print(cislo, 'nie je prvočíslo')
~~~

Po spustení napr.:
~~~
Zadaj číslo: 101
101 je prvočíslo
~~~

Druhý program zisťuje, či je nejaké číslo dokonalé, t.j. súčet všetkých deliteľov menších ako samotné číslo sa rovná samotnému číslu. Na základe tohto nájde (postupne preverí) všetky dokonalé čísla do 10000:
~~~
print('dokonalé čísla do 10000 sú', end=' ')
for cislo in range(1,10001):
    sucet = 0
    for delitel in range(1, cislo):
        if cislo % delitel == 0:
            sucet += delitel
    if sucet == cislo:
        print(cislo, end=' ')
print()
print('=== viac ich už nie je ===')
~~~
Program vypíše:
~~~
dokonalé čísla do 10000 sú 6 28 496 8128
=== viac ich už nie je ===
~~~