filename='Output.txt'
with open(filename,'w') as file1:
    text1=input('Enter text to write to file :')
    file1.write(text1 +'\n')
    print(f"Data successfully written to the '{filename}'")
with open(filename,'a') as file1:
    text2=input('Enter additional text to append to the file:')
    file1.write(text2 + '\n')
    print(f"Data successfully appended to the '{filename}'")
with open(filename,'r') as file1:
    print(f"Final content of the '{filename}':\n")
    read_file=file1.read()
    print(read_file)
    file1.close()