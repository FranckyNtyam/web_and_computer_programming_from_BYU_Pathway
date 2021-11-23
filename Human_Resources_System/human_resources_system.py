with open("Human_Resources_System/hr_system.txt") as information:
    for infos in information:
        infos = infos.strip()
        infos = infos.split(" ")
        for index in range(len(infos)):
            if index == 0 :
                name = infos[index]
            elif index == 2:
                title = infos[index]
        print(f"Name: {name:10} Title: {title}\n")


print("STRETCH CHALLENGE\n")
with open("Human_Resources_System/hr_system.txt") as information:
    for infos in information :
         infos = infos.strip()
         infos = infos.split(" ")
         for index in range(len(infos)):
             if index == 0 :
                 name = infos[index]
             elif index == 1 :
                 id = infos[index]
             elif index == 2 :
                 title = infos[index]
             elif index == 3 :
                 salary = float(infos[index])
                 if title.lower() == "engineer":
                    pay_amount = (salary/ 24) + 1000
                 else:
                    pay_amount = salary/ 24      
         print(f"{name:10} (ID: {id:5}) {title:9} - ${pay_amount:.2f}")