
Pokračovanie č. I

# Funkcie nad množinami (set-mi)

>## Bežné množinové funkcie (metódy)
Pythonovský datový typ set podporuje niekoľko bežných množinových funkcii (metód) či operácií.

~~~
a_set = {2, 4, 5, 9, 12, 21, 30, 51, 76, 127, 195}
30 in a_set                        ①        
True

31 in a_set
False

b_set = {1, 2, 3, 5, 6, 8, 9, 12, 15, 17, 18, 21}
a_set.union(b_set)                 ②

{1, 2, 195, 4, 5, 6, 8, 12, 76, 15, 17, 18, 3, 21, 30, 51, 9, 127}

a_set.intersection(b_set)          ③
{9, 2, 12, 5, 21}

a_set.difference(b_set)            ④
{195, 4, 76, 51, 30, 127}

a_set = {2, 4, 5, 9, 12, 21, 30, 51, 76, 127, 195}
b_set = {1, 2, 3, 5, 6, 8, 9, 12, 15, 17, 18, 21}
a_set.symmetric_difference(b_set)  ⑤
{1, 3, 4, 6, 8, 76, 15, 17, 18, 195, 127, 30, 51}
~~~
①	Ak chceme otestovať, či je daná hodnota prvkom množiny, použijeme operátor **in**. Funguje rovnakým spôsobom ako u je to u zoznamov.\
②	Metóda union() (zjednotenie) vracia novú množinu, ktorá obsahuje všetky prvky ako z jednej, tak aj z druhej množiny.\
③	Metoda intersection() (prienik) vracia novú množinu, ktorá obsahuje všetky prvky ktoré sa nachádzajú se v oboch množinách súčasne.\
④	Metoda difference() (rozdíl) vrací novou množinu obsahující všechny prvky, které se nacházejí v množině a_set, ale nenacházejí se v množině b_set.\
⑤	Metoda symmetric_difference() (symetrický rozdiel) vracia novú množinu obsahujúcu všetky prvky, ktoré se nachádzajú práve v jednej z množín.\

Tri z týchto funkcii (metód) sú tzv. symetrické čo znamená súmernosť z hladiska. V náväznosti na predchádzajúci príklad sú to tieto funkcie:
~~~
b_set = {1, 2, 3, 5, 6, 8, 9, 12, 15, 17, 18, 21}
a_set = {2, 4, 5, 9, 12, 21, 30, 51, 76, 127, 195}
b_set.symmetric_difference(a_set)  ①
{3, 1, 195, 4, 6, 8, 76, 15, 17, 18, 51, 30, 127}

b_set.symmetric_difference(a_set) == a_set.symmetric_difference(b_set)  ②
True


b_set.union(a_set) == a_set.union(b_set)  ③
True

b_set.intersection(a_set) == a_set.intersection(b_set)  ④
True

b_set.difference(a_set) == a_set.difference(b_set)  ⑤
False
~~~
①	Symetrický rozdiel množín a_set od b_set vypadá inak ako symetrický rozdiel množín b_set od a_set. Ale pamätujme na to, že množiny sú neusporiadané. Akékoľvek dve množiny, ktorých všetky hodnoty sa zhodujú (žiadna nesmie byť vynechaná), sa považujú za zhodné.\
②	A presně tento prípad nastal tu. Nenechajme sa zmiať reprezentáciami týchto množín ktoré zobrazené v pythonovskom shelle. Obsahujú rovnaké hodnoty, takže sú zhodné.\
③	Zjednocenie dvoch množín je tiež symetrické.\
④	Prienik dvoch množín je taktiež symetrický.\
⑤	Rozdiel dvoch množín symetrický neni. Ono to dáva zmysel. Podobá sa to na odčítanie jedného čísla od druhého. Na poradí operandov tu ale záleží !

A nakoniec tu máme niekoľk funkcii ktoré vyhodnocujú zadané otázky vztiahnuté na množiny. 
~~~
a_set = {1, 2, 3}
b_set = {1, 2, 3, 4}
a_set.issubset(b_set)    ①
True

b_set.issuperset(a_set)  ②
True

a_set.add(5)             ③
a_set.issubset(b_set)
False

b_set.issuperset(a_set)
False
~~~
①	Množina a_set je podmnožinou množiny b_set — všechny prvky množiny a_set jsou současně prvky množiny b_set.\
②	Stejnou otázku můžeme položit obráceně. Množina b_set je nadmnožinou množiny a_set, protože všechny prvky množiny a_set jsou současně prvky množiny b_set.\
③	Jakmile do množiny a_set přidáme hodnotu, která se v množině b_set nenachází, oba testy vrátí hodnotu False.

>## Množiny v booleovském kontextu

Množiny můžeme použít v booleovském kontextu, například v příkazu if.
~~~
>>> def is_it_true(anything):
...   if anything:
...     print("yes, it's true")
...   else:
...     print("no, it's false")
...
>>> is_it_true(set())          ①
no, it's false
>>> is_it_true({'a'})          ②
yes, it's true
>>> is_it_true({False})        ③
yes, it's true
~~~
①	Prázdná množina se v booleovském kontextu vyhodnocuje jako false.
②	Libovolná množina s alespoň jedním prvkem se vyhodnocuje jako true.
③	Libovolná množina s alespoň jedním prvkem se vyhodnocuje jako true. Hodnota prvků je nepodstatná.