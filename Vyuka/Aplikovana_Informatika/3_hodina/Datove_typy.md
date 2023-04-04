# Dátové typy


Každá premenná je určitým dátovým typom. V jazyku Python nie je nutné pri vytváraní premennej deklarovať aj jej typ ale možné to samozrejme je. Dátové typy je vhodné určiť kvôli tomu, aby sme kompileru dali vedieť, s akými dátami má pracovať aby nedošlo k chybám. Samozrejme aj nám, programátorom, uľahčuje prácu presná informácia, s čím pracujeme. 

## Boleánsky typ (boolean)

tento dátový typ môže mať len dve možnosti – True alebo False
používame ich napríklad pri logických operátoroch
pravda = bool(True) # Určenie typu boolean
nepravda = False # Bez určenia typu - fungovať bude ako False
print(type(pravda)) # Vypísanie dátového typu:  <class 'bool'>

## Čísla

### Celé čísla (integers, skratka int) 
– dátový typ celých čísel, ktorý teoreticky nemá limit na dĺžku hodnoty (limitom bude vždy systém, v ktorom sa pracuje). Celé čísla môžeme zapisovať v rôznych číselných sústavách: 
#### binárna sústava (dvojková)
– pred čísla dávame predponu 0b (0B) – print(0b15)
bin1 = bin(43)
bin2 = 0b10110110
bin3 = 14
print('bin1 =', bin1, 'bin2 =', bin2, 'bin3 =', bin(bin3)[2:]) # bin1 = 0b101011 bin2 = 182 bin3 = 1110

#### decimálna sústava (desiatková)
– print(15)
dec1 = 18
dec2 = int(67)
print('dec1 =', dec1, 'dec2 =', dec2) # dec1 = 18 dec2 = 67
print(type(dec1)) # <class 'int'>

#### oktálna sústava (osmičková) 
– pred čísla dávame predponu 0o (0O) – print(0o15)
okt1 = 0o24
okt2 = 24
okt3 = oct(10)
print('okt1 =', okt1, 'okt2 =', oct(okt2), 'okt3 =', okt3) # okt1 = 20 okt2 = 0o30 okt3 = 0o12

#### hexadecimálna sústava (šestnástková)
– pred čísla dávame predponu 0x (0X) – print(0x15)
hex1 = 0x142
hex2 = 16
hex3 = hex(32)
print('hex1 =', hex1, 'hex2 =', hex2, 'hex3 =', hex3) # hex1 = 322 hex2 = 16 hex3 = 0x20

### Desatinné čísla (floatI)
– desatinné čísla sa píšu s bodkou
flt1 = 24.8
flt2 = float(18 / 4)
flt3 = 5.476e9
print('flt1 =', flt1, 'flt2 =', flt2, 'flt3 =', flt3) # flt1 = 24.8 flt2 = 4.5 flt3 = 5476000000.0
### Komplexné čísla  (complex)
– komplexné čísla sa skladajú s reálnej časti a imaginárnej (15j)
cmp1 = 4j
cmp2 = 7 + 4j
cmp3 = cmp1 + cmp2
print('cmp1 =', cmp1, 'cmp2 =', cmp2, 'cmp3 =', cmp3) # cmp1 = 4j cmp2 = (7+4j) cmp3 = (7+8j)


## Reťazce (string)
– určitý rad znakov, príkladom použitia je print("Miesto dvojitých úvodzoviek môžeme použiť jednoduché úvodzovky")

uvodnyText = str("Vitajte na našom webe")
print(type(uvodnyText)) # <class 'str'>
## Zoznam (list)
– určitý zoznam, napríklad mien - list(("Matej", "Gabriel", "Zuzana"))

zoznam = list(("Matej", "Gabriel", "Zuzana"))
print(type(zoznam)) # <class 'list'>

## N-tice (tuple)

### podobne ako pri reťazcoch, obsahuje znaky, v tomto prípade sa tu môžu nachádzať aj hodnoty

### uchovávajú napríklad informácie o charaktere v počítačovej hre –meno hráča, úroveň, množstvo peňazí, počet ocenení a trieda - hrac = tuple(("Apolonius", "44", "14.547", "12", "Farmári"))

### k uloženým informáciám pristupujeme napríklad print(tuple[0]) kde sa v tomto prípade vypíše len meno hráča
hrac = tuple(("Apolonius", "44", "14.547", "12", "Farmári"))
print(hrac[0]) # Vypíšeme meno hráča, ktoré sa nachádza na pozícií 0
print(type(hrac)) # <class 'tuple'>

## Slovník (dictionary)

#### slovník je podobný n-ticiam, len v tomto prípade sa označuje, ktorá hodnota čo znamená

#### použiť ho môžeme napríklad pri zozname žiakov a ich veku: ziaci= {"Adam": "12", "Adela": "11", "Martin": "12"}

#### k dátam pristupujeme napríklad print(ziaci.get("Adela")), v tomto prípade sa vypíše vek Martina

ziaci= {"Adam": "12", "Adela": "11", "Martin": "12"} # Vytvorenie slovníka bez priradenia typu 
print(ziaci.get("Adela")) # Zobrazí vek Adely
print(type(ziaci)) # <class 'dict'>

## Sety (set)

### zbierka podobná ako zoznam, len bez poradia alebo indexovania

### set = {"Nemocnica", "Škola", "Polícia", "74.14"}

### výpis funguje ako print(set) kde v každom novom behu programu bude zoznam v inom poradí

set = {"Nemocnica", "Škola", "Polícia", "74.14"} # Vytvorenie setu bez určenia typu
print(set) # Zobrazenie stále v inom poradí
print(type(set)) # <class 'set'>
