Ak potrebujeme 5-krát vypísať ten istý text, môžeme to zapísať napr. takto:
~~~
print('programujem v Pythone')
print('programujem v Pythone')
print('programujem v Pythone')
print('programujem v Pythone')
print('programujem v Pythone')
~~~
Namiesto toho použijeme novú konštrukciu for-cyklu:
~~~
for i in 1, 2, 3, 4, 5:
    print('programujem v Pythone')
~~~
Ako to funguje:

* do premennej i sa bude postupne priraďovať nasledovná hodnota zo zoznamu hodnôt
* začíname s prvou hodnotou, teda v tomto prípade 1
* pre každú hodnotu so zoznamu sa vykonajú príkazy, ktoré sú v **tele cyklu**, t.j. tie príkazy, ktoré sú odsadené
* v našom príklade sa päťkrát vypíše rovnaký text 'programujem v Pythone', hodnota premennej i nemá na tento výpis žiadny vplyv
* všimnite si znak ‚:‘ na konci riadka s for - ten je tu povinne, bez neho by to nefungovalo

**Telo cyklu:**

* tvoria príkazy, ktoré sa majú opakovať; definujú sa **odsadením** príslušných riadkov
* odsadenie je povinné a musí byť minimálne 1 medzera, odporúča sa odsadzovať vždy o **4 medzery**
* ak telo cyklu obsahuje viac príkazov, všetky **musia** byť odsadené o rovnaký počet medzier
* telo cyklu **nesmie** byť prázdne, musí obsahovať aspoň jeden príkaz
* niekedy sa môže hodiť **prázdny príkaz pass**, ktorý nerobí nič, len oznámi čitateľovi, že sme na telo cyklu nezabudli, ale zatiaľ tam nechceme mať nič
* prázdne riadky v tele cyklu nemajú žiaden význam, často slúžia na sprehľadnenie čitateľnosti kódu

Podobný výpis dostaneme aj takýmto zápisom for-cyklu:
~~~
for i in 1, 1, 1, 1, 1:
    print('programujem v Pythone')
    print('---------------------')
~~~
Aj v tomto prípade sa telo cyklu bude opakovať 5-krát. Telo cyklu sa tu teraz skladá z dvoch príkazov print(), preto sa vypíše týchto 10 riadkov textu:
~~~
programujem v Pythone
---------------------
programujem v Pythone
---------------------
programujem v Pythone
---------------------
programujem v Pythone
---------------------
programujem v Pythone
---------------------
~~~

Ak by sme ale druhý riadok tela cyklu neodsunuli:
~~~
for i in 1, 1, 1, 1, 1:
    print('programujem v Pythone')
print('for i in 1, 1, 1, 1, 1:
    print('programujem v Pythone')
print('---------------------')')
~~~
telo cyklu je teraz len jeden príkaz. Program najprv 5-krát vypíše text 'programujem v Pythone' a až potom jeden riadok s minuskami:
~~~
programujem v Pythone
programujem v Pythone
programujem v Pythone
programujem v Pythone
programujem v Pythone
---------------------
~~~
V tele cyklu môžeme použiť aj **premennú cyklu**, ktorej hodnota sa pri každom prechode cyklom automaticky mení. V nasledovnom príklade je premennou cyklu prem:
~~~
for prem in 1, 2, 3, 4, 5:
    print(prem)
~~~
Po spustení programu sa postupne vypíšu všetky nadobudnuté hodnoty:
~~~
1
2
3
4
5
~~~
Ďalší program počíta druhé mocniny niektorých zadaných prvočísel:
~~~
for x in 5, 7, 11, 13, 23:
    x2 = x ** 2
    print('druhá mocnina', x, 'je', x2)
~~~
Po spustení dostávame:
~~~
druhá mocnina 5 je 25
druhá mocnina 7 je 49
druhá mocnina 11 je 121
druhá mocnina 13 je 169
druhá mocnina 23 je 529
~~~
Premenná cyklu nemusí nadobúdať len celočíselné hodnoty, ale hodnoty úplne ľubovoľného typu, napr.
~~~
>>> for x in 22/7, 3, 14, 8., 1000-1e-3:
        print('druha odmocnina z', x, 'je', x ** .5)

druha odmocnina z 3.142857142857143 je 1.7728105208558367
druha odmocnina z 3 je 1.7320508075688772
druha odmocnina z 14 je 3.7416573867739413
druha odmocnina z 8.0 je 2.8284271247461903
druha odmocnina z 999.999 je 31.62276079029154
~~~
Niektoré hodnoty postupnosti hodnôt for-cyklu sú tu celočíselné, iné sú desatinné. V tomto príklade si všimnite, ako sme tu počítali druhú odmocninu čísla: číslo sme umocnili na 1/2, t.j. 0.5.

V ďalšom cykle sme namiesto zoznamu hodnôt použili znakový reťazec: už vieme, že znakový reťazec je vlastne postupnosť znakov, preto for-cyklus tento znakový reťazec „rozoberie“ na jednotlivé znaky a s každým znakom vykoná telo cyklu (znak vypíše 10-krát):
~~~
>>> for pismeno in 'Python':
        print(pismeno * 10)

PPPPPPPPPP
yyyyyyyyyy
tttttttttt
hhhhhhhhhh
oooooooooo
nnnnnnnnnn
~~~
Rovnaký výsledok by sme dosiahli aj týmto zápisom for-cyklu:
~~~
for pismeno in 'P', 'y', 't', 'h', 'o', 'n':
    print(pismeno * 10)
~~~

>## Generovanie postupnosti čísiel
Cyklus for sa často používa pri generovaní náhodných čísiel. Táto množina náhodných čísiel sa používa pri testování algoritmov, spracovaní grafov a pod. Využijeme k tomu funkciu **range()** s ktorou už sme sa stretli a ktorá môže mať rôzpočet parametrov. A práve podľa týchto parametrov ktoré sú čeločíselné sa bude generovať aj výsledná postupnosť.

funkcia **range()**

range(stop)\
range(start, stop)\
range(start, stop, krok)

***Parametre:***	
* start – prvý prvok vygenerovanej postupnosti (ak chýba, predpokladá sa 0)
* stop – hodnota, na ktorej sa už generovanie ďalšej hodnoty postupnosti zastaví - táto hodnota už v postupnosti nebude
* krok – hodnota, o ktorú sa zvýši (resp. zníži pre záporný krok) každý nasledovný prvok postupnosti, ak tento parameter chýba, predpokladá sa 1


Väčšinou platí, že do parametra stop nastavíme o 1 väčšiu hodnotu, ako potrebujeme poslednú hodnotu vygenerovanej postupnosti.

Najlepšie si to ukážeme na príkladoch rôzne vygenerovaných postupností celých čísel. V tabuľke vidíme výsledky pre rôzne parametre:
| Zápis    | Výsledok                                                                    |
|-----------|---------------------------------------------------------------------------|
| range(10) | 0,1,2,3,4,5,6,7,8,9
|range(0, 10)| 0,1,2,3,4,5,6,7,8,9
| range(0, 10, 1) | 0,1,2,3,4,5,6,7,8,9
|range(3, 10)| 3,4,5,6,7,8,9
| range(3, 10, 2) | 3,5,7,9
|range(10, 100, 10)| 10,20,30,40,50,60,70,90
| range(10, 1, -1) | 10,9,8,7,6,5,4,3,2
|range(10, 1)| prázdna postupnosť
|range(1, 1)|prázdna postupnosť

Niekoľko ukážok použitia for pri tvorbe kódu:
~~~
>>> for n in range(5):     # postupnosť čísel od 0 pre menšie ako 5
        print(n)

0
1
2
3
4
>>> for n in range(5, 9):  # postupnosť čísel od 5 pre menšie ako 9
        print(n)

5
6
7
8
>>> print(range(7, 100, 11))
range(7, 100, 11)
~~~
Všimnite si, že volaním print(range(7, 100, 11)) sa nedozvieme nič užitočné o vygenerovanej postupnosti. Pre kontrolu hodnôt vygenerovaných pomocou range() musíme zatiaľ použiť for-cyklus.

Ak potrebujeme vypisovať pomocou for-cyklu väčší počet čísel, je veľmi nepraktické, ak každý jeden print() vypisuje do ďalšieho riadka. Hodilo by sa nám, keby print() v niektorých situáciách nekončil prechodom na nový riadok. Využijeme nový typ parametra:

funkcia **print()**

print(..., end='reťazec')

**Parametre:**	
* **...** - obsah výpisu
* **end='reťazec'** – tento reťazec nahradí štandardný '\n' na ľubovoľný iný, najčastejšie je to jedna medzera ' ' alebo prázdny reťazec ''

Tento parameter musí byť v zozname parametrov funkcie print() uvedený ako posledný za všetkými vypisovanými hodnotami. Vďaka nemu po vypísaní týchto hodnôt sa namiesto prechodu na nový riadok vypíše zadaný reťazec.
~~~
print('programujem', end='_')
print(10, end='...')
print('rokov')
~~~
Tieto 3 volania print() vypíšu len jeden riadok:
~~~
programujem_10...rokov
~~~
Funkciu print sme spolu s jej špecialnym parametrom spomenuli preto, lebo táto funkcia sa takto používa vo for-cykloch. V nasledovnom uvedieme príklad kedy vypíšeme 100 hodnôt do jedného dlhého riadku a čísla pritom oddelíme čiarkami s medzerou: 
~~~
>>> for cislo in range(100,200):
        print(cislo, end=', ')

100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115,
116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147,
148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163,
164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179,
180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195,
196, 197, 198, 199,
~~~
Pri tvorbe programu bude funkciou print() na konci posledného riadka a ďalšie výpisy by pokračovali tu. Tiež sa zvykne po skončení takéhoto cyklu zavolať print() bez parametrov.

Pri tlačení napr. tabuliek nejakých hodnôt často potrebujeme slušne naformátovať takýto výstup. Napr.
~~~
>>> for i in range(1,11):
        print(i, i * i, i ** 3, i ** 4)

1 1 1 1
2 4 8 16
3 9 27 81
4 16 64 256
5 25 125 625
6 36 216 1296
7 49 343 2401
8 64 512 4096
9 81 729 6561
10 100 1000 10000
~~~
Najčastejšie použijeme formátovanie znakového reťazca (metódou format()):
~~~
>>> for i in range(1,11):
        print('{:3} {:4} {:5} {:6}'.format(i, i * i, i ** 3, i ** 4))

  1    1     1      1
  2    4     8     16
  3    9    27     81
  4   16    64    256
  5   25   125    625
  6   36   216   1296
  7   49   343   2401
  8   64   512   4096
  9   81   729   6561
 10  100  1000  10000
~~~
V tomto príklade vidíte, že formátovacia dvojica znakov '{}' môže obsahovať šírku vypisovanej hodnoty - uvádzame ju za dvojbodkou, teda '{:3}' označuje, že hodnota sa vypisuje na šírku 3 a ak je kratšia (napr. jednociferné číslo), zľava sa doplní medzerami.

Ďalší príklad ilustruje for-cyklus, v ktorom počet prechodov určuje načítaná hodnota nejakej premennej:

~~~
n = int(input('zadaj pocet: '))
for i in range(1, n + 1):
    print('*' * i)
~~~
Program vypíše n riadkov, pričom v prvom je jedna hviezdička, v druhom 2, atď. Napr. takéto spustenie programu:
~~~
zadaj pocet: 5
*
**
***
****
*****
~~~
Túto my+slienku môžeme rôzne rozvíjať tak, že v každom riadku bude nejaký počet medzier a nejaký iný počet hviezdičiek, napr.
~~~
n = int(input('zadaj pocet: '))
for i in range(n):
    print(' '*(n-1-i) + '*'*(2*i+1))
for i in range(n):
    print(' '*i + '*'*(2*n-2*i-1))
~~~
Výsledok potom bude vyzerať takto:
~~~
zadaj pocet: 5
    *
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *
~~~

For-cyklus sa dobre využije v **prípadoch, keď sa v tele cyklu** vyskytuje príkaz, ktorý **inkrementuje nejakú premennú** (alebo ju mení inou operáciou). Zrejme toto inkremenovanie prejde toľkokrát, koľko je prechodov cyklu a často sa pritom využije premenná cyklu.

Ukážme túto ideu na príklade, v ktorom spočítame všetky hodnoty premennej cyklu. Použijeme na to ďalšiu premennú, do ktorej sa bude postupne pripočítavať premenná cyklu:
~~~
n = int(input('zadaj pocet: '))
sucet = 0
for i in range(1, n + 1):
    sucet = sucet + i                  # alebo  sucet += i
print('sucet cisel =', sucet)
~~~
V tomto programe sme použili premennú sucet, do ktorej postupne pripočítavame všetky hodnoty z intervalu (range) od 1 do n. Vďaka tomu sa po skončení cyklu v tejto premennej nachádza práve súčet všetkých celých čísel do n. Spustíme napr.
~~~
zadaj pocet: 10
sucet cisel = 55
~~~
Tento program nám môže slúžiť ako nejaká **šablóna**, pomocou ktorej riešime podobnú triedu úloh: v každom prechode cyklu niečo pripočítavame, násobíme, delíme, … 

Takáto **pripočítavacia šablóna** sa skladá z:

* inicializácia pomocnej premennej (alebo viacerých premenných), do ktorej sa bude pripočítavať, najčastejšie je to vynulovanie;
* v tele cyklu sa do tejto pomocnej premennej pripočíta nejaká hodnota, najčastejšie premenná cyklu;
* po skončení cyklu sa v tejto pomocnej premennej nachádza očakávaný výsledok sčitovania.

Ukážeme to na niekoľkých príkladoch.

****Výpočet faktoriálu****, čo je vlastne súčin čísel 1 * 2 * 3 * … * n. 

Pomocná premenná musí byť inicializovaná 1, namiesto pripočítavania bude násobenie:
~~~
n = int(input('zadaj cislo: '))
sucin = 1
for i in range(1, n + 1):
    sucin = sucin * i                  # alebo  sucin *= i
print('{}! = {}'.format(n, sucin))
~~~
V záverečnom výpise sme použili formátovanie reťazca. Po spustení, napr.
~~~
zadaj cislo: 6
6! = 720
~~~

Úplne rovnaký princíp môžeme použiť aj keď **premenná cyklu** nebude obsahovať čísla nejakého intervalu, ale budú to **znaky z rozoberaného znakového reťazca**. 

Nasledovný príklad postupne prechádza znak za znakom daného reťazca a za každým k pomocnej premennej pripočíta 1:
~~~
retazec = input('zadaj retazec: ')
pocet = 0
for znak in retazec:
    pocet = pocet + 1                  # alebo  pocet += 1
print('dlzka retazca =', pocet)
~~~

Tento program spočíta počet znakov zadaného znakového reťazca, napr.
~~~
zadaj retazec: python
dlzka retazca = 6
~~~

Ďalší príklad ilustruje, ako môžeme využiť **premennú cyklu, ktorá obsahuje znak zadaného reťazca**. 

Pomocná premenná bude znakového typu a v tomto príklade ju budeme inicializovať prázdnym reťazcom:
~~~
retazec = input('zadaj retazec: ')
novy = ''
for znak in retazec:
    novy = novy + znak + znak
print('novy retazec =', novy)
~~~
V tele cyklu sa k pomocnej premennej prireťazujú dva rovnaké znaky. Vďaka tomuto sa vytvorí nový reťazec, v ktorom bude každý znak z pôvodného reťazca dvakrát, napr.
~~~
zadaj retazec: Python
novy retazec = PPyytthhoonn
~~~
>## Vnorené cykly
Problematiku vnorenia cyklu si najlepšie priblýžime pomocou príkladu. 

Zoberme si najprv povôdný príplad, ktorý vypíše čísla od 0 do 99 do 10 riadkov tak, že v prvom stĺpci sú čísla od 0 do 9, v druhom od 10 do 19, … v poslednom desiatom sú čísla od 90 do 99. Podľa vyššie uvedeného tomu zodpovedá nasledovný kód:
~~~
for i in range(10):
    print(i, i+10, i+20, i+30, i+40, i+50, i+60, i+70, i+80, i+90)
~~~
A výsledok vyzerá takto:
~~~
0 10 20 30 40 50 60 70 80 90
1 11 21 31 41 51 61 71 81 91
2 12 22 32 42 52 62 72 82 92
3 13 23 33 43 53 63 73 83 93
4 14 24 34 44 54 64 74 84 94
5 15 25 35 45 55 65 75 85 95
6 16 26 36 46 56 66 76 86 96
7 17 27 37 47 57 67 77 87 97
8 18 28 38 48 58 68 78 88 98
9 19 29 39 49 59 69 79 89 99
~~~
Riešenie tohto príkladu využíva for-cyklus len na vypísanie 10 riadkov, pričom obsah každého riadka sa vyrába bez cyklu jedným príkazom print(). Toto je ale nepoužiteľný spôsob riešenia v prípadoch, ak by tabuľka mala mať premenlivý počet stĺpcov, napr. keď je počet zadaný zo vstupu. Vytvorenie jedného riadka by sme teda tiež mali urobiť for-cyklom, t.j. **budeme definovať for-cyklus, ktorý je vo vnútri iného cyklu, tzv. vnorený cyklus**. Všimnite si, že celý tento cyklus musí byť odsadený o ďalšie 4 medzery:
~~~
for i in range(10):
    for j in range(0, 100, 10):
        print(i + j, end=' ')
    print()
~~~
Vnútorný for-cyklus vypisuje 10 čísel, pričom premenná cyklu i postupne nadobúda hodnoty 0, 10, 20, … 90. K tejto hodnote sa pripočítava číslo riadka tabuľky, teda premennú j. Tým dostávame rovnakú tabuľku, ako predchádzajúci program. Rovnaký výsledok vytvorí aj nasledovné riešenie:
~~~
for i in range(10):
    for j in range(i, 100, 10):
        print(j, end=' ')
    print()
~~~
V tomto programe má vnútorný cyklus tiež premennú cyklu s hodnotami s krokom 10, ale v každom riadku sa začína s inou hodnotou.

Túto istú ideu využijeme, aj keď budeme vytvárať tabuľku čísel od 0 do 99, ale organizovanú inak: v prvom riadku sú čísla od 0 do 9, v druhom od 10 do 19, … v poslednom desiatom sú čísla od 90 do 99:
~~~
for i in range(0, 100, 10):
    for j in range(i, i + 10):
        print(j, end=' ')
    print()
~~~
Možných rôznych zápisov riešení tejto úlohy je samozrejme viac.Ešte dve veľmi podobné úlohy:
1. Prečítať celé číslo n a vypísať tabuľku čísel s n riadkami, pričom v prvom je len 1, v druhom sú čísla 1 2, v treťom 1 2 3, atď. až v poslednom sú čísla od 1 do n:
~~~
pocet = int(input('zadaj počet riadkov: '))
for riadok in range(1, pocet + 1):
    for cislo in range(1, riadok + 1):
        print(cislo, end=' ')
    print()
~~~
Všimnite si mená oboch premenných cyklov riadok a cislo, vďaka čomu môžeme lepšie pochopiť, čo sa v ktorom cykle deje. Spustíme, napr.
~~~
zadaj počet riadkov: 7
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6
1 2 3 4 5 6 7
~~~
2. Zadanie je podobné, len tabuľka v prvom riadku obsahuje 1, v druhom 2 3, v treťom 4 5 6, atď. každý ďalší riadok obsahuje o jedno číslo viac ako predchádzajúci a tieto čísla v každom ďalšom riadku pokračujú v číslovaní. Zapíšeme jedno z možných riešení:
~~~
pocet = int(input('zadaj počet riadkov: '))
cislo = 1
for riadok in range(1, pocet + 1):
    for stlpec in range(1, riadok + 1):
        print(cislo, end=' ')
        cislo += 1
    print()
~~~
~~~
zadaj počet riadkov: 7
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21
22 23 24 25 26 27 28
~~~
V tomto riešení využívame pomocnú premennú cislo, ktorú sme ešte pred cyklom nastavili na 1, vo vnútornom cykle vypisujeme jej hodnotu (a nie premennú cyklu) a zakaždým ju zvyšujeme o 1.


