succesful = 0
min = 101

while 1:
    name = input('Dwse onoma upopsifiou alliws dwse TELOS gia termatismo: ')
    if name == 'TELOS':
        break
    enothta1 = int(input('Dwse bathmo prwths enothtas: '))
    enothta2 = int(input('Dwse bathmo deuterhs enothtas: '))
    enothta3 = int(input('Dwse bathmo triths enothtas: '))

    total_enothta= (enothta1+enothta2+enothta3)/3
    if total_enothta >=55 and enothta1 >=50 and enothta2 >=50 and enothta3 >=50:
        print ('O upopsifios ',name,'einai epityxhs me synoliko bathmo ',total_enothta)
        succesful+= 1
        print ('Sunolo pou perasan',succesful)
        if total_enothta < min:
            min=total_enothta
        print ('O mikroteros sunolikos bathmos einai: ',min)
