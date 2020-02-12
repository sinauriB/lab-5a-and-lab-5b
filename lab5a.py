#sinauri tapia
#lab 5a


#starting documentation table of context for starting docuemntation

#- name
#-program prompt
#-variable dictionary




#PRORGAM PROMPT
#A PROGRAM THAT READS DATA  FROM CSV FILE AND STORES ALL THAT DATA IN LISTSPRORGAM THEN HAS USER INPUT(ALLOWS USER TO FIND PERSON LAST NAME IN THE LISTS)
#  THIS IS KNOW AS SEQUENTIAL SEARCH!!!
#THIS SEQUENTIAL SEARCH WITH ANOTHER PRINT STATEMENT SHOULD PROMPT INPUT TO USER SO THEY CAN  SEARCH FOR AS MANY  LAST NAMES AS THEY WANT IN THE LIST
#FINALLY A PRINT STATEMENT THAT ASKS THE USER HOW MANY TIMES IT TOOK LOOP TO FIND THE  "REQUESTED SEARCH"



#VARIABLE DICTIONARY
#





#base program..........


Fnamez = []
Lnamez = []
birth_date = []





records = 0
search_count = 0

import csv

with open(" . ")as csv file:
    file = csv.reader(csvfile)

     for rec in file:

          records += 1

          
Fnamez.append(rec[0])
Lnamez.append(rec[1])
birth_date.append(rec[2])


#leaving csv file alll data is now stored into lists

print("finished processing file.\n\n\n")





















