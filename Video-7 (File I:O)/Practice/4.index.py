def check_line():
    word="learning"
    data=True
    line_no=1
    with open("Practice.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print("Index no:",line_no)
                return
            line_no+=1
    return -1
check_line()