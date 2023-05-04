with open('C:\\Users\\tomast\\Documents\\sss-trencin\\Vyuka\\Aplikovana_Informatika\\13_hodina\\dva.txt', 'w') as f:
    f.write('first\nsecond\n')

with open('C:\\Users\\tomast\\Documents\\sss-trencin\\Vyuka\\Aplikovana_Informatika\\13_hodina\\dva.txt') as subor:
    prvy, druhy = subor

print(prvy)
