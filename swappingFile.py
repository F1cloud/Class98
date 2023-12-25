def swapFileData():
    file1 = input("Select the first file ")
    file2 = input("Select the second file ")

    data_a = open(file1,"r") 
    a = data_a.read()
    print(a)

    data_b = open(file2,"r") 
    b = data_b.read()
    print(b)

    data_a = open(file1,"w")
    data_a.write(b)

swapFileData()    
