try:
    file1=open('Sample.txt','r')
    write_file1=file1.readline()
    write_file2 = file1.readline()
    print('Reading file content:\n')
    print('Line 1:',write_file1)
    print('Line 2:',write_file2)
    file1.close()
except FileNotFoundError as e:
    print(f"The file '{e.filename}' doesn't exist")
