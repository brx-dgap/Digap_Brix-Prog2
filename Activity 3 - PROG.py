Word_dict = {}

Word_input = input("Enter a sentence: ").lower()

words = Word_input.split(" ")

for word in words:
    if word in Word_dict:
        Word_dict[word] += 1
    else:
        Word_dict[word] = 1

for word, count in Word_dict.items():
    print(f"{word} : {count}")