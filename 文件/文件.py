def read_file():
    fname = eval(input("请输入文件名："))
    infile=open(fname,"r")
    data=infile.read()
    print(data)
read_file()
