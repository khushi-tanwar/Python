import os.path
def copyodd(f1):
    count=1
    try:
        file1=open(f1,'r')
    except FileNotFoundError:
        print(f1,"doesn't exists.")
        return
    print ("To check if output file alraedy exists or not....")
    if(os.path.isfile('copyodd.txt')):
        print("Output File exists")
    else:
        print("File doesn't exists")
    file2=open('copyodd.txt','w')
    r1=file1.read()
    for i in range(0,len(r1)):
        if(count%2!=0):
            file2.write(r1[i])
        if r1[i]=='\n':
            count=count+1
    file1.close()
    file2.close()
def main():
    f1=input("Enter the name of file to be opened in read mode:")
    copyodd(f1)
if __name__=="__main__":
    main()
