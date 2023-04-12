https://www.gymmoldava.sk/ICV/INF/doc/python/Udajove%20typy%20zadania%20na%20hodinu.pdf

uloha1. čo urobí nasledujúci program?
moj=random.choice( (‘Times New Roman’, ‘Arial’, ‘Consolas’, ‘Courier New’, ‘Calibri’) ) ... choice ma iba jeden parameter!
velkost=int(34/3)
canvas.create_text(150, 100, text=‘skúška’, font=(moj, velkost,’bold’), angle=random.choice((45, 90, 135, 180)) )

uloha2. vypíšte v jednom riadku vedľa seba 10 krúžkov s polomerom 10 (s náhodnou farbou) s číslicami 0, 1, 2, ... 9 v týchto farebných
krúžkoch /ako by ste dosiahli, aby boli krúžky pod sebou?
y=100
x=10
for i in range(10):
 x=x+30
 farba=random.choice( ('blue', 'red', 'cyan', 'purple', 'yellow', 'green', 'white') )
 canvas.create_oval(x-10, y-10, x+10, y+10, fill=farba)
 canvas.create_text(x, y, text=i)
 canvas.update()
 canvas.after(400)

uloha3. zmeňte predchádzajúci program tak, aby boli v krúžkoch čísla:
a) od 5 do 15 (vrátane) for i in range(5,16):
b) párne od 0 do 10 (vrátane) for i in range(0,11, 2):
c) všetky čísla od 11 do 1 (vrátane) for i in range(11, 0, -1):
d) 1, 3, 4, 7, 8, 11 for i in (1, 3, 4, 7, 8, 11):
Načítanie vstupu od užívateľa (zo shellu), pozor, načítaný je vždy vo forme reťazca:
premenna = input('Ako sa voláš? ')
vek = input('Koľko máš rokov? ') vek=int ( input('Koľko máš rokov? ') )
vyska = input('Akú máš výšku, uveď v metroch: ') vyska = float ( input('Akú máš výšku, uveď v metroch: ') )

uloha4. načítajte od užívateľa rozsah vykresľovaných čísel v krúžkoch (od, do) / pod nimi nech sú v štvorčekoch čísla v opačnom poradí

uloha5. od užívateľa načítajte počet štvorčekov (n), ktoré zobrazíte v uhlopriečke štvorcového plátna, očíslujte ich v poradí 1, 2,... n

uloha6*. v opačnej uhlopriečke nech sú čísla v klesajúcom poradí