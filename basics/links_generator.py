import fileinput
for line in fileinput.input():
    ids = line.split("\n")
    for i in ids:
        if i:
            print("http://192.168.88.232:8080/user/{}".format(i))