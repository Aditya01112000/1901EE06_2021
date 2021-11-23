from openpyxl import Workbook
from openpyxl import load_workbook
from collections import defaultdict
from os import name
import os.path
import csv

d = defaultdict(list)
course_lt = defaultdict(list)
info = defaultdict(list)


"""
   Name - Aditya Goyal
   Roll No. - 1901EE06
"""


def generate_ltp():
    
    # course_lt dictionary containing count of L-T-P and no. of non-zero bits
    with open('course_master_dont_open_in_excel.csv','r') as f:
        reader =csv.reader(f)
        for words in reader:
            sub_no=words[0]
            if sub_no=="subno":
              continue
            split=words[2].split("-")
            count=0;
            for x in split:
                  course_lt[sub_no].append(x)
                  if x=="0":
                      continue
                  else:
                      count=count+1
            course_lt[sub_no].append(count)
    
    """
    d dictationary -> d[roll_no]=[course,register_sem,schedule_sem,0,0,0,roll_no]
    [0,0,0] in d dict is count of L-T-P in each index for that particular course which is updated in feedback_not_submitted() function

    """
    with open('course_registered_by_all_students.csv','r') as f:
        reader =csv.reader(f)
        for words in reader:
          roll_no=words[0]
          roll_no.upper()
          if roll_no=="rollno":
                continue
          course_t=words[3]
          final_string=roll_no+course_t
          d[final_string].append(course_t)
          d[final_string].append(words[1])
          d[final_string].append(words[2])
          d[final_string].append(0)
          d[final_string].append(0)
          d[final_string].append(0)
          d[final_string].append(roll_no) 
    
    #  info dic containing information about students

    with open('studentinfo.csv','r') as f:
        reader =csv.reader(f)
        for words in reader:
          roll_no=words[1]
          if roll_no=="Roll No":
                continue
          roll_no.upper()
          info[roll_no].append(words[0])
          info[roll_no].append(words[8])
          info[roll_no].append(words[9])
          info[roll_no].append(words[10])
     
def feedback_not_submitted():
  
  ltp_mapping_feedback_type = {1: 'lecture', 2: 'tutorial', 3:'practical'}
  output_file_name = "course_feedback_remaining.xlsx" 
  with open('course_feedback_submitted_by_students.csv','r') as f:
        reader =csv.reader(f)
        for words in reader:
          roll_no=words[3]
          if roll_no=="stud_roll":
                continue
          roll_no.upper()
          course_t=words[4]
          final_string=roll_no+course_t
          feedback_type=int(words[5])
          # adding no. of particular feedback type from [1,2,3] in d{}
          d[final_string][2+feedback_type]=d[final_string][2+feedback_type]+1;

  temp=0
  arr=[]
  for key,value in d.items():
      flag=0
      # check if L is non-zero and count of L in d dict is zero then students doesn't give feedback
      if(course_lt[value[0]][0]!='0' and value[3]==0):
            flag=1
      #  similarly for T
      if(course_lt[value[0]][1]!='0' and value[4]==0):
            flag=1
      #  similarly for P
      if(course_lt[value[0]][2]!='0' and value[5]==0):
            flag=1
      if(flag==1):
            # info is not provided in xlsx file
            if(info[value[6]]==[]):   
                  arr.append([value[6],int(value[1]),int(value[2]),value[0],"NA_IN_STUDENTINFO","NA_IN_STUDENTINFO","NA_IN_STUDENTINFO","NA_IN_STUDENTINFO"])
            else:
                  arr.append([value[6],int(value[1]),int(value[2]),value[0],info[value[6]][0],info[value[6]][1],info[value[6]][2],(info[value[6]][3])])
  
  if os.path.isfile(output_file_name) is True:
      os.remove(output_file_name) 
      
  # appending all the output(arr) into workbook
  wb = Workbook()
  sheet = wb.active
  sheet.append(["rollno","register_sem","schedule_sem","subno","Name","email","aemail","contact"])
  for x in arr:
      sheet.append(x)
  wb.save(output_file_name)

generate_ltp()
feedback_not_submitted()
