'''Writing to a csv file'''
with open('file.csv','a') as file:
    for _ in range(2):
        data=input('Enter first name and last name using commas ')
        first_name,last_name=data.split(',') #returns a list
        file.write(f'{first_name},{last_name}\n')
        




'''print(f'{last_name},{first_name}')'''


