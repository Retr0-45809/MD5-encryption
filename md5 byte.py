import hashlib

while(True):
 n=int(input("----MD5 Algorithm----\n1) String input\n2) File encoding\n3) Exit\nEnter your choice:"))
 if(n==1):
    import hashlib 
    string = input("Enter String:")
    encoded=string.encode()
    result = hashlib.md5(encoded)
    print("String : ", end ="")
    print(string)
    print("Hash Value : ", end ="")
    print(result)
    print("Hexadecimal equivalent : ",result.hexdigest())
 elif(n==2):
    with open("sample.txt","rb") as f:
        bytes = f.read()
        print("String : ",bytes.decode())
        result = hashlib.md5(bytes)
        print("Hash Value : ",result)
        print("Hexadecimal equivalent : ")
        print(result.hexdigest())
 elif(n==3):
     break
 else:
    print("Wrong choice")