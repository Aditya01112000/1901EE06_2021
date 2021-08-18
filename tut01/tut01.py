# defining function to check whether the given number present in the list pass to the function is meraki number or not 
def MERAKI(n):
        f=0
            # finding the absolute difference between number and its adjacent
        for j in range(len(str(n))-1):
            n=str(n)
                
            if abs(int(n[j])-int(n[j+1]))==1:
                f=0
            else:
                f=1
                break

        # printing yes / no based on the flag value
        if f==0:
            print("Yes,", n, "is a Meraki number.")
            return True
        else:
            print("No,", n, "is not a Meraki number.")
            return False

input = [int(item) for item in input("Enter the input : ").split()] 
# input = [12, 14, 56, 78, 98, 54, 678, 134, 789, 0, 7, 5, 123, 45, 76345, 987654321]

cnt_yes = 0
cnt_no = 0 
# iterating through the given input
for n in input:
    if MERAKI(n):
        cnt_yes += 1
    else:
        cnt_no += 1
    
print("The input list contains", cnt_yes,"meraki and", cnt_no,"non meraki numbers.")