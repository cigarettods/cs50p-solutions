def main():
    message = input("")
    print(convert(message))

def convert(message):
    return message.replace(":)", "🙂").replace(":(", "🙁")

main()