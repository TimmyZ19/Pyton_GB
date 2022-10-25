NAME_FILE = "phone directory.csv"


def File_recording(data):
    with open(NAME_FILE, "a") as directory:
        text = data["name"] + ";" + data["surname"] +\
            ";" + data["phone"] + ";" + data["comment"] + "\n"
        directory.writelines(text)


def File_reading():
    with open(NAME_FILE, "r") as directory:
        for line in directory.read().split():
            print(line.split(";"))
