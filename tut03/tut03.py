import os.path

def output_by_subject():
    direc="output_by_subject"
     # check if file is not already exist ....if exist then updating the same folder
    if os.path.exists(direc)==False:
        os.mkdir(direc) 
    # opening input file
    with open("regtable_old.csv","r") as f:
        temp=""
        for line in f:
            initial=""
            subject=""
            words=line.split(',')
            initial=words[0]+","+words[1]+","+words[3]+","+words[8]
            if words[0]=="rollno":
                temp=initial
            else:
                subject=words[3]
                check=os.path.join(direc,subject+".csv")
                if os.path.isfile(check) is True:
                    with open(check,"a") as g:
                        g.write(initial)
                else:
                    with open(check,"w") as g:
                        g.write(temp)
                        g.write(initial)
    return

def output_individual_roll():
    direc="output_individual_roll"
    # check if file is not already exist ....if exist then updating the same folder
    if os.path.exists(direc)==False:
        os.mkdir(direc) 
    # opening input file
    with open("regtable_old.csv","r") as f:
        temp=""
        for line in f:
            initial=""
            roll_no=""
            words=line.split(',')
            initial=words[0]+","+words[1]+","+words[3]+","+words[8]
            if words[0]=="rollno":
                temp=initial
            else:
                roll_no=words[0]
                check=os.path.join(direc,roll_no+".csv")
                #checking if file already exist or not
                if os.path.isfile(check) is True:
                    with open(check,"a") as g:
                        g.write(initial)
                else:
                    with open(check,"w") as g:
                        g.write(temp)
                        g.write(initial)
    return

output_individual_roll()
output_by_subject()