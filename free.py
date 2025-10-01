sente=input("Enter the Your text\n")

# print(sente)


ansthe=int(input("Enter The choose"))
# print(ansthe)


match ansthe:
    case 1:
        sente=sente.upper()
        print(sente)
    case 2:
        sente=sente.lower()
        print(sente)
    case 3:
        sente=sente.capitalize()
        print(sente)
    case 4:
        count=0
        for i in sente:
            count+=1
        print(count)
    case __:
        print("error")
    

