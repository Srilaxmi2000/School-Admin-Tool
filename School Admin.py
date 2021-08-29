#BASIC SCHOOLD ADMIN TOOL

import csv
def write_into_csv(info_list):
    with open('student_info', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        if csv_file.tell()==0:
             writer.writerow(["Name", "Age","Phone Number","Email-ID"])
        writer.writerow(info_list)
            
       
        
if __name__ == '__main__':
    condition=True
    student_num=1
    
while(condition):
    student_info=input("Enter the information of the student #{} in the following format(Name Age Phone Number Email-ID):".format(student_num))
    
    
    
    #split
    student_info_list=student_info.split(' ')
    
    print("\nThe Entered information is-\nName:{}\nAge:{}\nPhone Number:{}\nEmail-ID:{}"
          .format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
    choice_check=input("Is the entered information is correct? (yes/no):")
   
    if choice_check=="yes":
        write_into_csv(student_info_list)
        
    condition_check=input("Do you wanna enter anther students information? (yes/no)")
    if condition_check=="yes":
        condition=True
    elif condition_check=="no":
        condition=False
        student_num=student_num+1
    elif choice_check=="no":
        print("Please Re-enter the values again")
            
     
    
    

