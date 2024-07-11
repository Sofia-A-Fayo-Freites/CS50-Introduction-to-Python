import sys
import requests

def main():
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")

    if len(sys.argv) == 2:
        n = sys.argv[1]
        try:
            m = float(n)
            try:
                response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
                o = response.json()
                price = (o["bpi"]["USD"]["rate_float"])
                result = price * m
                print(f"${result:,.4f}")
            except requests.RequestException:
                pass
        except ValueError:
            sys.exit("Command line argument is not a number")

    else:
        sys.exit("Command-line argument is not a number")

if __name__ == "__main__":
    main()
