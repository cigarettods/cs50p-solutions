file_name = input("File name: ").strip().lower()

match file_name:
    case _ if file_name.endswith(".gif"):
        print("image/gif")
    case _ if file_name.endswith((".jpg", ".jpeg")):
        print("image/jpeg")
    case _ if file_name.endswith(".png"):
        print("image/png")
    case _ if file_name.endswith(".pdf"):
        print("application/pdf")
    case _ if file_name.endswith(".txt"):
        print("text/plain")
    case _ if file_name.endswith(".zip"):
        print("application/zip")
    case _:
        print("application/octet-stream")