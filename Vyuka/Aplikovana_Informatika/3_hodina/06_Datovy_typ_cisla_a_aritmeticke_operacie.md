Na rozdiel od mnohých iných jazykov, ktoré sú kompilačné (napr. Pascal, C/C++, C#) je Python interpreter. To znamená, že interpreter nevytvára spustiteľný kód (napr. .exe súbor vo Windows)
na spustenie programu musí byť v počítači nainštalovaný Python interpreter umožňuje aj interaktívnu prácu s prostredím.
## Interaktívny režim¶
Po spustení IDE (Python GUI) - čo je vývojové prostredie (Integrated Development Environment), vidíme informáciu o verzii Pythonu a tiež riadok s tromi znakmi >>> (tzv. výzva, t.j. prompt). Za túto výzvu budeme písať príkazy pre Python.

Python 3.9.9 (tags/v3.9.9:ccb0e6a, Nov 15 2021, 18:08:50) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.

## Ako to funguje

Python je interpreter a pracuje v niekoľkých možných režimoch
teraz sme ho spustili v príkazovom režime: očakáva zadávanie textových príkazov (do riadka za znaky >>>), každý zadaný príkaz vyhodnotí a vypíše prípadnú reakciu (alebo chybovú správu, ak sme zadali niečo nesprávne)
po skončení vyhodnocovania riadka sa do ďalšieho riadka znovu vypíšu znaky >>> a očakáva sa opätovné zadávanie ďalšieho príkazu
takémuto interaktívnemu oknu hovoríme shell
niekedy sa môžete dočítať aj o tzv. REP cykle interprétra, znamená to Read, Evaluate, Print, teda prečítaj, potom tento zápis vyhodnoť a na koniec vypíš výsledok, toto celé stále opakuj.

Môžeme teda zadávať, napr. nejaké matematické výrazy

<p>>>> 12345</p>
<p>12345</p>
<p>>>> 123 + 456</p>
<p>579</p>
<p>>>> 1 * 2 * 3 * 4 * 5 * 6</p>
<p>720</p>
<p>>>></p>

V tomto príklade sme pracovali s celými číslami a niektorými celočíselnými operáciami. Python poskytuje niekoľko rôznych typov údajov; na začiatok sa zoznámime s tromi základnými typmi: celými číslami, desatinnými číslami, binárnymi čislami a bytami.

> **Celé čísla** (integer skratka int)
* majú rovnaký význam, ako ich poznáme z matematiky: zapisujú sa v desiatkovej sústave a môžu začínať znamienkom mínus
* ich veľkosť (počet cifier) je obmedzená len kapacitou pracovnej pamäte Pythonu (hoci aj niekoľko miliónov cifier)

Pracovať môžeme aj s desatinnými číslami (tzv. floating point), napr.

<p>>>> 22 / 7</p>
<p>3.142857142857143</p>
<p>>>> .1 + .2 + .3 + .4</p>
<p>1.0</p>
<p>>>> 9999999999*99999999999</p>
<p>999999999890000000001<p/>
<p>>>> 9999999999*99999999999.</p>
<p>9.9999999989e+20</p>
<p>>>></p>

>**Desatinné čísla** (float)

* obsahujú desatinnú bodku alebo exponenciálnu časť (napr. 1e+15)
* môžu vzniknúť aj ako výsledok niektorých operácií (napr. delením dvoch celých čísel)
* majú obmedzenú presnosť (približne 16-17 platných cifier)

Všimnite si, že 3. výraz 9999999999*99999999999 násobí dve celé čísla a aj výsledkom je celé číslo. Hneď ďalší výraz 9999999999*99999999999. obsahuje jedno desatinné číslo a teda aj výsledok je desatinné číslo.

> **Komplexné čísla** (complex)

Komplexný dátový typ v pythone pozostáva z dvoch hodnôt, z ktorých prvá je reálna časť komplexného čísla a druhá je imaginárna časť komplexného čísla . Reálnu časť zvyčajne označujeme pomocou i a imaginárnu časť j. Napríklad (3 + 7j) alebo (3i + 7j).
'''
~~~
>>>3 + 0j
(3+0j)

>>>0 + 3j
3j

>>>2 + 3j + 4 + 5j
(6+8j)

>>>3 + 2j == 2j + 3
True

>>>z = 3 + 2
>>>type(z)     # prve pouzitie nejakej funkcie !!!
<class 'int'>    
~~~

~~~
>>>z = 3.14 + 2.71j
>>>type(z)
<class 'complex'>
~~~