file1 = open("D:\Desktop\Desktop_Important\Python\data_science.txt","r")
file2 = open("D:\Desktop\Desktop_Important\Python\data_write.txt","w")
for line in file1:
    file2.write(line)
file1.close()

