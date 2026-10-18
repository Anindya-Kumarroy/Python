f=open("sample.txt","r+")     # r+ will start replacing from the beginning!
f.write("abc!")
print(f.read())               #Will be printed after the replaced area!
f.close()