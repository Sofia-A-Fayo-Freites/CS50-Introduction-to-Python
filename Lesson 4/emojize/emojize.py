import emoji

def main():
    text = input("Input: ")
    
    print("Output: ", emoticon(text))

def emoticon(text):
    return(emoji.emojize(text, language="alias"))

main()