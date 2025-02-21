def print_fruits(t):
    
    if len(t) == 3:
        
        red, yellow, green = t
        
        
        for fruit in [red, yellow, green]:
            print(fruit)
            
    else:
        print("The tuple must contain exactly three elements.")


fruits = ("rambutan", "mangga", "grape")
print_fruits(fruits)

