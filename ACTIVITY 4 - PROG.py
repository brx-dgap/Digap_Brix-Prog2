while True:
    try:
        currency = {
            "USD": 1.00,
            "EUR": 0.84,
            "GBP": 0.72,
            "JPY": 109.98,
            "AUD": 1.33,
            "CAD": 1.26,
            "CHF": 0.92,
            "CNY": 6.46,
            "HKD": 7.76,
            "NZD": 1.43,
        }


        current_currency = input("Enter currency: ").upper()
        if current_currency  not in currency:
            print(f"{current_currency} is a Unkown currency ")
            continue

        target_currency = input("Enter target currency: ").upper()
        if target_currency  not in currency:
            print(f"{target_currency} is a Unkown currency ")
            continue

        amount = float(input("Enter amount: "))
        
    except ValueError:
        print("error: invalid input")
    except KeyboardInterrupt:
        print("errors")
        
        result = amount / currency[current_currency] * currency[target_currency]
        print(f"{amount} {current_currency} = {result} {target_currency}")