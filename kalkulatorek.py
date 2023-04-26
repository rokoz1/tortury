while True:
    print("aby użyć kalkulatora wciśnij \'k\'")
    print('aby zakończyć matematyczną przygodę wciśnij \'f\'')
    decyzja = input()
    if decyzja == 'k':
        print('ahoj kamracie, jakie liczby masz dziś w głowie?')
        print('powiedz pierwszą')
        liczba1 = int(input())
        print('ok. ok. nadążam.\n','podaj drugą')
        liczba2= int(input())
        print('a co byś chciał?')
        odp=input()
        if odp == 'dodawanie':
            wynik1=liczba1+liczba2
            print('wynikiem dodawania będzie:', wynik1)
        elif odp == 'odejmowanie':
            wynik2=liczba1-liczba2
            wynik3=liczba1-liczba2
            print('wynikiem odejmowania będzie:', wynik2, "lub:", wynik3)
        elif odp == 'mnożenie':
            wynik4=liczba1*liczba2
            print('ok, wynikiem mnożenia będzie"', wynik4)
        elif odp == 'dzielenie':
            wynik5=liczba1/liczba2
            print('wynikiem tego dzielenia będzie:', wynik5)
        else:
            print('sora, ale nie znam takiego działania')
    elif decyzja == 'f':
        break
    else:
        print('niunia, szanujmy się, nie takie były opcje wyboru')
        print('dam ci kolejną szansę')
        
        #mam coś tu zmienic, ale odmawiam. Let my boy kalkulatorek live </3
