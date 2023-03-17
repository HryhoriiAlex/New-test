
l = []

with open("files/menu/files/end.txt", "r") as file:
    f = file.readlines()

name = []
types = []
path = []

for i in f:
    n = i.split("(")[0]
    if n != "\n":
        name.append(n)
        
        if "(прогамма)" in i:
            n = i.split("(прогамма) -")
            t = "(прогамма)"
        elif "(сайт)" in i:
            n = i.split("(сайт) -")
            t = "(сайт)"
        elif "(комбінація)" in i:
            n = i.split("(комбінація) -")
            t = "(комбінація)"
        types.append(t)
        t = ""

        try:
            path.append(n[1].lstrip().rstrip())
        except:
            pass
        n = ""

end = []
for i, b, c in zip(name, types, path):
    l = [i.split(", "), b, c, "команда"]
    end.append(l)

menu = end