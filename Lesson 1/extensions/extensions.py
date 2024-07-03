filename = input("Write the name of the file ")
suffixes = (".jpg", ".jpeg")

if filename.strip().casefold().endswith(".gif"):
    print("image/gif")
elif filename.strip().casefold().endswith(suffixes):
    print("image/jpeg")
elif filename.strip().casefold().endswith(".png"):
    print("image/png")
elif filename.strip().casefold().endswith(".pdf"):
    print("application/pdf")
elif filename.strip().casefold().endswith(".txt"):
    print("text/plain")
elif filename.strip().casefold().endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
