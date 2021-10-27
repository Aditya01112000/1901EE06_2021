import re
import os
import shutil

direc="corrected_srt"
list_file={
	1:"Breaking Bad",
	2:"Game of Thrones",
	3:"Lucifer"
}

def got(filename,season,episode):
   file_name=""
   ragex = r"(.+?(?= -)) - (\w+) - (.+?(?=.WEB))"
   match=re.search(ragex,filename)
   if match != None:
      ragex1=r"0*(\d+)x0*(\d+)"
      match1=re.search(ragex1,match.group(2))
      temp="Season "+ (season-len(match1.group(1)))*"0"+match1.group(1)+" Episode "+(episode-len(match1.group(2)))*"0"+match1.group(2)
      file_name=match.group(1)+" - "+temp+" - "+match.group(3)
   return file_name

def bad(filename,season,episode):
    file_name=""
    ragex=r"(\w+ \w+) (\w+)"
    match=re.search(ragex,filename)
    if match != None:
      ragex1=r"\w0*(\d+)\w0*(\d+)"
      match1=re.search(ragex1,match.group(2)) 
      temp="Season "+ (season-len(match1.group(1)))*"0"+match1.group(1)+" Episode "+(episode-len(match1.group(2)))*"0"+match1.group(2)
      file_name=match.group(1)+" "+temp
    return file_name

def lucifer(filename,season,episode):
   file_name=""
   ragex = r"(.+?(?= -)) - (\w+) - (.+?(?=.HDTV))"
   match=re.search(ragex,filename)
   if match != None:
      ragex1=r"0*(\d+)x0*(\d+)"
      match1=re.search(ragex1,match.group(2))
      temp="Season "+ (season-len(match1.group(1)))*"0"+match1.group(1)+" Episode "+(episode-len(match1.group(2)))*"0"+match1.group(2)
      file_name=match.group(1)+" - "+temp+" - "+match.group(3)
   return file_name

def regex_renamer():
	# Taking input from the user

    print("1. Breaking Bad")
    print("2. Game of Thrones")
    print("3. Lucifer")
    webseries_num = int(input("Enter the number of the web series that you wish to rename. 1/2/3: "))
    season_padding = int(input("Enter the Season Number Padding: "))
    episode_padding = int(input("Enter the Episode Number Padding: "))
    if os.path.exists(direc)==False:
      os.mkdir(direc)
    copy_srt=os.path.join(direc,list_file[webseries_num])
    wrong_srt=os.path.join("wrong_srt",list_file[webseries_num])

    try:
        shutil.copytree(wrong_srt,copy_srt)
        for filename in os.listdir(copy_srt):
          split_tup = os.path.splitext(filename)
          extension=split_tup[1]
          f=os.path.join(copy_srt,filename) 
          if os.path.isfile(f):
            if(webseries_num==2):
              final=got(filename,season_padding,episode_padding)
            elif(webseries_num==1):
              final=bad(filename,season_padding,episode_padding)
            elif(webseries_num==3):
              final=lucifer(filename,season_padding,episode_padding)
          g=os.path.join(copy_srt,final+extension)
          try:
            os.rename(f,g)
          except FileExistsError:
            print("File already Exists")
    except Exception as e:
        print(e)



regex_renamer()