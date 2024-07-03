answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ")

if not (answer.strip() == "42" or answer.casefold() == "forty-two" or answer.casefold() == "forty two"):
    print("No")
else:
    print ("Yes")