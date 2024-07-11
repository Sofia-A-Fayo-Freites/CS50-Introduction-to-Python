months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    date = input("Date: ")

    if formatted_date(date) == "":
        return main()
    else:
        print(formatted_date(date))

def formatted_date(date):
    import re
    fdate = ""
    if date.split(" ")[0] in months:
        try:
            if date.split(",")[1].strip().isdigit():
                if int(re.split("[ ,]+", date)[1]) >= 1 and int(re.split("[ ,]+", date)[1]) <= 31:
                    return(f"{re.split("[ ,]+", date)[2].strip()}-{months.index(re.split("[ ,]+", date)[0]) + 1:02}-{int(re.split("[ ,]+", date)[1].strip()):02}")
        except IndexError:
            return ""
    elif date.split("/")[0].strip().isdigit():
        if int(date.split("/")[0]) >= 1 and int(date.split("/")[0]) <= 12:
            if int(date.split("/")[1]) >= 1 and int(date.split("/")[1]) <= 31:
                return(f"{date.split("/")[2].strip()}-{int(date.split("/")[0].strip()):02}-{int(date.split("/")[1].strip()):02}")
    return fdate

main()
