# Množiny (set)
Množina alebo set je druh kolekcie **immutable** ktorá opäť vychádza zo zoznamu s tým rozdielom, že môže obsahovať iba unikátné položky t.j. **každá položka môže byť v množine iba jeden krát**. Tým že táto vlastosť zodpovedá matematickéj definicii množiny vznikol dôvod aby táto kolekcia aj v Pythone dostala názov množiny. Ak hovoríme že **položky nie sú zotriedené** - neusporiadané, znamená to to, že položka bude pridaná svojvolne na ľubovolné miesto do množiny a výraz **neopakujúce sa** znamená, že ak zadáme príkaz na pridanie hodnoty do množiny, bude táto hodnota vložená do množiny, len vtedy ak sa v nej ešte nevyskytuje. 
~~~
a_set = {1}     ①
print(a_set)

{1}
type(a_set)     ②
<class 'set'>

a_set = {1, 2}  ③
print(a_set)

{1, 2}
~~~
①	Zápis množiny keď chceme vytvoriť množinu s jednou hodnotou. Vtedy uzatvoríme túto hodnotu do zložených zátvoriek {}.
②	Množiny sú v skutočnosti implementované ako triedy, ale týmto sa teraz nebudeme zatažovať.
③	Ak chceme vytvoriť množinu s viacerými hodnotami, oddelíme hodnoty čiarkami a všetko uzatvoríme do zložených zátvoriek.

Pre množiny **neexistuje žiadná zvláštna syntax** ako to bolo v prípade zoznamov či n-tic, vytvárame ich jednoducho použitím globálnej funkcie set(), ktorej môžeme napr. prostredníctvom  parametra funkcie add priložiť novú hodnotu:
~~~
planety = set(("Země", "Mars", "Jupiter", "Saturn", "Uran", "Neptun"))
print(planety)

planety.add("Pluto")
print(planety)

planety.add("Neptun")
print(planety)

Výsledok:
{'Jupiter', 'Uran', 'Saturn', 'Mars', 'Neptun', 'Země'}
{'Jupiter', 'Uran', 'Saturn', 'Mars', 'Neptun', 'Země', 'Pluto'}
{'Jupiter', 'Uran', 'Saturn', 'Mars', 'Neptun', 'Země', 'Pluto'}
~~~
V príklade výššie sme vytvorili množinu šiestich mien planet. Dvojité zátvorky na riadku s funkciou set() znamenajú, že sme odovzdali názvy planet formou n-tice ako parameter tejto
funkcie. Poradie položiek není zoradené podľa abecedy, a nezmení sa ani po pridaní novej položky. To ale neni židná chyba, lebo položky sú vnútorne udržované v poradí, čo pomahá množine efektivne určiť jedinečnosť každej položky.

>**Množinu môžeme vytvoriť aj zo zoznamu.**
~~~
a_list = ['a', 'b', 'mpilgrim', True, False, 42]    # toto je zoznam, viete preco
a_set = set(a_list)                           ①
a_set                                         ②

{'a', False, 'b', True, 'mpilgrim', 42}

a_list                                        ③
['a', 'b', 'mpilgrim', True, False, 42]
~~~
①	K vytvoreniu množiny zo zoznamu sme použili funkciu set(). (Odborníci na Python vedia ako sú množiny implementované. Vedia teda že aj to že v skutočnosti nejde o volanie funkcie, ale o vytváranie tzv. inštancie triedy. Táto problematika spadá do vlastného OOP ktorou sa budeme zaoberať v ďalšom ročníku lebo teraz našu pozornosť sústreďujeme hlavne na základy Pythonu. Preto nám yzatiaľ bude stačit vedieť, že set() sa chová ako funkcia a že vracia množinu.)\
②	Ako sme sa už zmienili skôr, jedna množina môže obsahovať hodnoty ľubovolného datového typu. A tiež sme už spoznali, že množiny sú neusporiadané. Táto množina si nepamätuje pôvodné poradie prvkov v zozname, ktorý ból použitý k jej vytvoreniu. Ak by sme do množiny pridávali ďalšie prvky, nebude si množina pamätovať poradie, v akom ste ich vkladali.\
③	Pôvodný zoznam zostáva nezmenený.

>**Vytvorenie prázdnej množiny**

Ak nemáme k dispozícii žiadne hodnoty (budú vytvorené resp. načítané podľa nejakého kritéria neskôr) nie je to žiadny problém. Môžeme totiž vytvoriť prázdnu množinu čím si vyčleníme (alokujeme) priestor a názov množiny pre neskoršiu aktualizáciu.
~~~
a_set = set()    ①
a_set            ②
set()
type(a_set)      ③

<class 'set'>
len(a_set)       ④
0

not_sure = {}    ⑤
type(not_sure)

<class 'dict'>
~~~
①	K vytvoreniu prázdnej množiny zavoláme set() bez argumentov.\
②	Zobrazená reprezentácia prázdnej množiny vypadá trochu divne. Asi ste očakávali niečo ako {} . Týmto spôsobom sa ale vyjadruje prázdny slovník (dictionary) a nie množina. O slovníkoch se dozvieme v nasledujúcej časti.\
③	Navzdory podivnosti zobrazenej reprezentácie to skutočne je množina...\
④	...a táto množina neobsahuje žiadné prvky.\
⑤	Prázdnu množinu nie je možné vytvoriť zápisom dvoch zložených zátvoriek kvôli histórii vývoja verzii (z Pythonu ver. 2). Týmto zpôsobom sa vyjadruje prázdny slovník a nie množina.
# Operácie nad množinami (set-mi)
>## Pridávanie hodnôt do množiny
Do existující množiny můžeme přidávat hodnoty dvěma různými způsoby: metodou add() a metodou update().
~~~
>>> a_set = {1, 2}
>>> a_set.add(4)  ①
>>> a_set
{1, 2, 4}
>>> len(a_set)    ②
3
>>> a_set.add(1)  ③
>>> a_set
{1, 2, 4}
>>> len(a_set)    ④
3
~~~
①	Metoda add() přebírá jeden argument, který může být libovolného datového typu, a přidává zadanou hodnotu do množiny.
②	Množina teď má tři členy.
③	Množiny jsou kolekcemi jedinečných hodnot. Pokud do množiny zkusíme přidat hodnotu, která se v ní již nachází, neudělá to nic. Nevznikne chyba. Jde zkrátka o prázdnou operaci.
④	Množina má pořád jen tři členy.
~~~
>>> a_set = {1, 2, 3}
>>> a_set
{1, 2, 3}
>>> a_set.update({2, 4, 6})                       ①
>>> a_set                                         ②
{1, 2, 3, 4, 6}
>>> a_set.update({3, 6, 9}, {1, 2, 3, 5, 8, 13})  ③
>>> a_set
{1, 2, 3, 4, 5, 6, 8, 9, 13}
>>> a_set.update([10, 20, 30])                    ④
>>> a_set
{1, 2, 3, 4, 5, 6, 8, 9, 10, 13, 20, 30}
~~~
①	Metoda update() přebírá jeden argument, rovněž množinu, a přidá všechny její členy do původní množiny. Je to, jako kdybychom volali metodu add() pro všechny členy množiny předané argumentem.
②	Protože cílová množina nemůže obsahovat jednu hodnotu dvakrát, duplicitní hodnoty se ignorují.
③	Ve skutečnosti můžete metodu update() volat s libovolným počtem argumentů. Pokud ji zavoláte s dvěma množinami, metoda update() přidá všechny členy z každé z předaných množin do původní množiny (duplicitní hodnoty se přeskočí).
④	Metoda update() umí zpracovat objekty různých datových typů, včetně seznamů. Pokud jí předáte seznam, pak metoda update() přidá do původní množiny všechny členy seznamu.

>## Odstraňovanie položiek z množiny
ednotlivé hodnoty lze z množiny odstranit třemi způsoby. První dva, discard() a remove(), se liší v jedné malé drobnosti.
~~~
>>> a_set = {1, 3, 6, 10, 15, 21, 28, 36, 45}
>>> a_set
{1, 3, 36, 6, 10, 45, 15, 21, 28}
>>> a_set.discard(10)                        ①
>>> a_set
{1, 3, 36, 6, 45, 15, 21, 28}
>>> a_set.discard(10)                        ②
>>> a_set
{1, 3, 36, 6, 45, 15, 21, 28}
>>> a_set.remove(21)                         ③
>>> a_set
{1, 3, 36, 6, 45, 15, 28}
>>> a_set.remove(21)                         ④
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 21
~~~
①	Metoda discard() přebírá jeden argument a zadanou hodnotu odebere z množiny.\
②	Pokud metodu discard() voláme s hodnotou, která v množině neexistuje, neprovede se nic. Nevznikne chyba. Jde o prázdnou operaci.\
③	Metoda remove() také přebírá hodnotu jediného argumentu a také odstraňuje hodnotu z množiny.\
④	Odlišnost se projeví v případě, kdy se zadaná hodnota v množině nenachází. V takovém případě metoda remove() vyvolá výjimku KeyError.

>### Použitie metódy pop()
Na odstraňovanie prvkov z množiny, tak ako tomu bolo pri zoznamoch aj tu možno použiť funkciu či metódu pop().
~~~
>>> a_set = {1, 3, 6, 10, 15, 21, 28, 36, 45}
>>> a_set.pop()                                ①
1
>>> a_set.pop()
3
>>> a_set.pop()
36
>>> a_set
{6, 10, 45, 15, 21, 28}
>>> a_set.clear()                              ②
>>> a_set
set()
>>> a_set.pop()                                ③
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'pop from an empty set'
~~~
①	Metoda pop() odstraní jeden prvek z množiny a vrátí jeho hodnotu. Ale množiny jsou neuspořádané a neexistuje u nich nic takového jako „poslední“ hodnota. Proto také neexistuje možnost ovlivnit, která hodnota bude odstraněna. Je to zcela náhodné.\
②	Metoda clear() odstraní všechny prvky množiny a množina se stane prázdnou. Ve výsledku je to stejné jako provedení příkazu a_set = set(), který vytvoří novou prázdnou množinu a přepíše původní hodnotu proměnné a_set.\
③	Pokus o volání metody pop() pro prázdnou množinu vede k vyvolání výjimky KeyError.

Pokračovanie č. I

