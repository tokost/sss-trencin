# Premenné a operácie s premennými

O premenným môžeme hovoriť ako o rezervovaní miesta v pamäti na ukladanie hodnôt. Do premennej sa dajú ukladať rôzne dátové typy. V jazyku Python ich nie je potrebné pred používaním deklarovať, deje sa to automaticky pri priradení hodnoty k premennej. Každá premenná je v jazyku Python totiž objektom. Môžeme ich definovať ako miesto v pamäti k uloženiu určitej hodnoty. 

Deklarovaním premennej určíme jej názov a dátový typ (platí pre iné jazyky). Takejto premennej sa vyhradí miesto v pamäti spolu s hodnotou, ak ju určíme. 

Hodnoty sa pripisujú pomocou „=“, kde na ľavej strane sa nachádza názov premennej, napravo hodnota. Názov premennej má určité pravidlá:

## Nesmie začínať číslom, jedine písmenom alebo „_“

osX, _osY - je správne

24osX, 0vysledok0 - nie je správne

## V názve sa môžu nachádzať len čísla, písmená a „_“

dotyk_pin0 - správne

dotyk.pin0 - nesprávne

## Premenné sú citlivé na veľké/malé písmená

V skratke to znamená, že ak je premenná napísaná správne, každým rozdielom v premenných vzniká ďalšia - Strana_A, strana_A, strana_a - tri rôzne premenné.



Príkazom print(x) jednoducho vypíšeme hodnotu uloženú v premennej x. Pri zlučovaní dvoch premenných platí pravidlo, že nie je možné zlúčiť dve premenné rôznych typov bez deklarovania ich typu. Príklad:

https://pythontutor.com/python-debugger.html#mode=edit 

print("string" + 14) &emsp; &nbsp;&emsp; &nbsp;   # Nastane chyba lebo sa spaja str s int
## Správne použitie
var = "string "\
num = 14\
print(var + str(num))

# Operácie
https://lms.umb.sk/mod/book/view.php?id=91939&chapterid=3688

Operácie využívajú operandy a operátory. Operandami sú premenné/čísla a operátormi znamienka, napríklad + alebo -. Na vykonávanie operácií používame operátory. Poznáme napríklad:



## Aritmetické

( +, -, *, /, ale aj modul %, exponent ** a delenie bez zvyšku // )

a, b = 6, 3\
c = a + b\
print("a + b =", c) &emsp; &nbsp; # výsledok je 9\
c = a - b\
print('a - b =', c) &emsp; &nbsp; # výsledok je 3\
c = a * b\
print('a * b =', c) &emsp; &nbsp; # výsledok je 18\
c = a / b\
print('a / b =', c) &emsp; &nbsp; # výsledok je 2.0\

a, b = 17, 9\
c = a % b\
print('a % b =', c) &emsp; &nbsp; # výsledok je 8\
c = a**2 + b**2\
print('a**2 + b**2 =', c) &emsp; &nbsp; # výsledok je 370\
c = a // b\
print('a // b =', c) &emsp; &nbsp; # výsledok je 1\
 

## Logické

AND a OR

if a < b and b > 3:\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   print('b je väčšie ako a, zároveň je b väčšie ako 3')\
elif a > b or a == 6:\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  print('a je väčšie ako b, zároveň a sa a rovná 6')
 

## Bitové

používajú sa na bitové operácie – and(&), or(|), xor(^), komplement(~), binárny posun vľavo(<<) a vpravo(>>)

x = 10  # zodpoveda podľa pravdivostnej tabuľky kombinácii 1010\
y = 14  # zodpoveda podľa pravdivostnej tabuľky kombinácii 1110
### and(&) - bude 1 ak bude na bitovom mieste oboch premenných 1
z = x & y\
print('x & y =', bin(z)[2:])
### or(|) - bude 1 ak na bitovom mieste je aspoň jedna hodnota 1
z = x | y\
print('x | y =', bin(z)[2:])
### xor(^) - bude 1 ak bude na bitovom mieste presne jedenkrát 1
z = x ^ y\
print('x ^ y =', bin(z)[2:])
### komplement(~) - prevod každej 1 na 0 a opačne
z = ~x\
print('~x =', bin(z))
### binárny posun vľavo(<<) - posun bitov o určitý počet miest vľavo (číslo sa zväčší)
z = x << 2\
print('x << 2 =', bin(z)[2:])
### vpravo(>>) - posun bitov o určitý počet miest vpravo (číslo sa zmenší)
z = x >> 2\
print('x >> 2 = ', bin(z)[2:])
 

## Porovnávacie

rovná sa(==), nerovná sa(!= a <>), väčší(>), menší(<), väčší rovný(>=), menší rovný(<=)

x, y, z = 24, 17, 14\
if x == y:
<pre>print('x je rovné y')
if x != z:\
    print('x je rozdielne od z')
if x > z:
    print('x je väčšie ako z')
if x < y:
    print('x je menšie ako y')
if z >= y:
    print('z je väčšie alebo rovné y')
elif z <= y:
    print('z je menšie alebo rovné y')</pre>
## Identifikačné

porovnáva objekty, či sú rovnaké – is a is not

a = 15\
b = a
<pre>if a is b:
    print('a = b')
if a is not b:
    print('a sa nerovná b')</pre>
 

## Členské

testujú, či sa premenná nachádza v inej – in a not in

zoznam = ['Andrej', 'Martin', 'Igor', 'Dávid', 'Ondrej']\
hladanyA = 'Martin'\
hladanyB = 'Arnold'\
<pre>if hladanyA in zoznam:
    print('Našla sa zhoda')
else:
    print('Nenašla sa zhoda')
if hladanyB not in zoznam:
    print('Hľadaný sa v zozname nenachádza')
else:
    print('Hľadaný sa v zozname nachádza')</pre>
## Priraďovacie

priraďujú hodnotu do premennej (=) alebo sčítajú(+=), odčítajú(-=), vynásobia(*=), vydelia(/=), použijú modulus(%=), exponent(**=) alebo sa vydelí bez zvyšku(//=) a hodnota sa súčasne pridelí do premennej

premenna = 0\
premenna += 1\
print('premenna += 1 =', premenna) &emsp; &nbsp; # výsledok je 1\
premenna -= 2\
print('premenna -= 2 =', premenna) &emsp; &nbsp; # výsledok je -1\
premenna *= 3\
print('premenna *= 3 =', premenna) &emsp; &nbsp; # výsledok je -3\
premenna /= 2
print('premenna /= 2 =', premenna) &emsp; &nbsp; # výsledok je -1.5\
premenna **= 2
print('premenna **= 2 =', premenna &emsp; &nbsp; # výsledok je 2.25\
premenna //= 4
print('premenna //= 4 =', premenna) &emsp; &nbsp; # výsledok je 0.0\
 