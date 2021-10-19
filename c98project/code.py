def fileWordReader():
    File1 = input("Name of File1 ")
    File2 = input("Name of File2 ")
    with open(File1,'r') as a:
        data_a = a.read()
    with open(File2,'r') as b:
        data_b = b.read()
    with open(File1,'w') as a:
        a.write(data_b)
    with open(File2,'w') as b:
        b.write(data_a)
fileWordReader()