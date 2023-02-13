import  royhat_otish
def avtosalon():
    cars = ["Matiz", "Spark", "Damas", "Nexia R3",  "Cobalt", "Gentra","Tracker-2","Equinox","Traverse"]
    while True:
        try:
            print(cars)
            x = input(f"Qanday rusumdagi avtomabil hohlaysiz {royhat_otish.name}: ")
            if x == "Matiz":
                narx = 6700
                print(f"Hurmatli {royhat_otish.name} siz tanlagan {x} avtomabili {narx} dollar narxida xarid qilishingiz mumkin")
                sorov = input(f"{x} avtomabilini harid qilasizmi? ha yoki yoq :")
                if sorov == "ha":
                    print(f"Siz {narx} $ bo'ldi, to'lovni to'lashingiz mumkin.")
            elif x == "Spark":
                narx = 8700
                print(f"Hurmatli {royhat_otish.name} siz tanlagan {x} avtomabili {narx} dollar narxida xarid qilishingiz mumkin")
                sorov = input(f"{x} avtomabilini harid qilasizmi? ha yoki yoq :")
                if sorov == "ha":
                    print(f"Siz {narx} $ bo'ldi, to'lovni to'lashingiz mumkin.")
            elif x == "Damas":
                narx = 8300
                print(f"Hurmatli {royhat_otish.name} siz tanlagan {x} avtomabili {narx} dollar narxida xarid qilishingiz mumkin")
                sorov = input(f"{x} avtomabilini harid qilasizmi? ha yoki yoq :")
                if sorov == "ha":
                    print(f"Siz {narx} $ bo'ldi, to'lovni to'lashingiz mumkin.")
            elif x == "Damas":
                narx = 8300
                print(f"Hurmatli {royhat_otish.name} siz tanlagan {x} avtomabili {narx} dollar narxida xarid qilishingiz mumkin")
                sorov = input(f"{x} avtomabilini harid qilasizmi? ha yoki yoq :")
                if sorov == "ha":
                    print(f"Siz {narx} $ bo'ldi, to'lovni to'lashingiz mumkin.")
            elif x == "Nexia R3":
                narx = 11000
                print(f"Hurmatli {royhat_otish.name} siz tanlagan {x} avtomabili {narx} dollar narxida xarid qilishingiz mumkin")
                sorov = input(f"{x} avtomabilini harid qilasizmi? ha yoki yoq :")
                if sorov == "ha":
                    print(f"Siz {narx} $ bo'ldi, to'lovni to'lashingiz mumkin.")
            elif x == "Cobalt":
                narx = 14000
                print(f"Hurmatli {royhat_otish.name} siz tanlagan {x} avtomabili {narx} dollar narxida xarid qilishingiz mumkin")  
                sorov = input(f"{x} avtomabilini harid qilasizmi? ha yoki yoq :")
                if sorov == "ha":
                    print(f"Siz {narx} $ bo'ldi, to'lovni to'lashingiz mumkin.")
            elif x == "Gentra":
                narx = 13500
                print(f"Hurmatli {royhat_otish.name} siz tanlagan {x} avtomabili {narx} dollar narxida xarid qilishingiz mumkin") 
                sorov = input(f"{x} avtomabilini harid qilasizmi? ha yoki yoq :")
                if sorov == "ha":
                    print(f"Siz {narx} $ bo'ldi, to'lovni to'lashingiz mumkin.")
            elif x == "Tracker-2":
                narx = 21000
                print(f"Hurmatli {royhat_otish.name} siz tanlagan {x} avtomabili {narx} dollar narxida xarid qilishingiz mumkin")

            elif x == "Equinox":
                narx = 45000
                print(f"Hurmatli {royhat_otish.name} siz tanlagan {x} avtomabili {narx} dollar narxida xarid qilishingiz mumkin") 

            elif x == "Traverse":
                narx = 71000
                print(f"Hurmatli {name} siz tanlagan {x} avtomabili {narx} dollar narxida xarid qilishingiz mumkin")

            
        except:
            print("Bunday rusumdagi avtomil mavjud emas!")
        yana = input("Yana avtomabil xarid qilishni hohlaysizmi? ha yoki yoq: ")
        if yana == "yoq":
            break

