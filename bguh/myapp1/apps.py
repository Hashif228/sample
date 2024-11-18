from django.apps import AppConfig
class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

import json



# with open('data.txt', 'r') as file:
#     # print(file.readline())
#     line = file.readline()
#     while line:
#         print(line,end='')
#         line=file.readline()






# def read_file(file_name):
#     print(f"Reading {file_name}...")
#     time.sleep(2)  
#     print(f"{file_name} read complete!")
# read_file('dfh')

# from datetime import datetime
# h=datetime.now()
# print(h.strftime('%H:%M:%S    %Y-%m-%d'))

import time
# dt=time.strftime('%H:%M:%S    %Y-%m-%d')
# print(dt)



# import time
# timestamp = time.time()
# local_time = time.localtime()
# print(timestamp)



# from datetime import datetime
# date_string = "2024-12-11 14:30:00"
# datetime_obj = datetime.strptime(date_string, "%Y-%m-%d %S:%M:%H")
# print("Converted datetime object:", datetime_obj)




from datetime import timedelta,date,datetime


# times=date.today()
# print(times)
# h='2000-02-28'
# sd=datetime.strptime(h,'%Y-%m-%d').date()
# print(sd-times)





# today=date.today()
# dob=datetime.strptime("2000-02-28",'%Y-%m-%d').date()
# print(f'{dob}       {dob.year}          {today.year}')





# i=datetime.now()
# print(i+timedelta(days=2))




# i=[]
# s=['hjh','dsffgfdh','ergrg']
# i.extend(s)
# print(i)





# i=['one','two','zero','hjhjh','gugg']
# print(i[0:2])











