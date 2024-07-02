def main():
    mass = int(input("What is the mass (in kg)? "))
    print("e=", conversor(mass))

def conversor(n):
    return int(n*(300000000*300000000))

main()

