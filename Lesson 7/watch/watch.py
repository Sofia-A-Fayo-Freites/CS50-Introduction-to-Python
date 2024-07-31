import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
   link = re.search(r"(\"https?://(?:www\.)?youtube\.com/embed/)([a-z0-9]+)\"", s, re.IGNORECASE)
   if link:
       last = link.group(2)
       short_link = f"https://youtu.be/{last}"
       return short_link
   else:
       return None

if __name__ == "__main__":
    main()