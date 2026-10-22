greeting = input("Greeting: ").strip().lower()
first_char = greeting[0] 
five_characters = greeting[:5]

match greeting:
    case _ if five_characters == "hello":
        print("$0")
    case _ if first_char == "h":
        print("$20")
    case _:
        print("$100")
