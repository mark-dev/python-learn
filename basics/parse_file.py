FILE_PATH = "/home/mark/code/python-projects/helloworld/iris.csv"


def file_items(file_path):
    with open(file_path,"r") as f:
        line = f.readline()
        while(line):
            yield line.split(',')
            line = f.readline()

for e in file_items(FILE_PATH):
    v = (a,b,c,d,f) = e
    print(v)