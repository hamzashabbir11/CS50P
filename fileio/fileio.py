from unicodedata import name


file = open('names.txt','a')

for _ in range(3):
    student_names=input('Enter Name ').title()
    file.write(f'{student_names}\n')
   
    
file.close()