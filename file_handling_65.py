
f1 = open('file1.txt', 'r+')
f1.write("this is file1")
f1.write("we need to copy data in file2")
f2 = open('file2.txt', 'a')
for i in f1:
    f2.write(i)
