bebelabsko = {}

ilan = int(input("ilan bebelabs mo: "))

for output in range(ilan):
    dict_name = input("Enter the name dictionary: ")

    bebelabsko[dict_name] = {}
    Name = input("Enter name: ")
    taon = int(input("Enter Age: "))
    
    bebelabsko[dict_name][Name] = taon
    
search = input("sino hanap mo?")

if search in bebelabsko:
    print (f"{bebelabsko [dict_name]}")

else:
    print("not found")


