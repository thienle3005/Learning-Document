from random import randrange
import datetime
import random
from record import  record_data
from threading import Thread



list_number_people_in =[]
list_number_people_out = []
total_people_in = 0 #test
total_people_out = 0 #test


def random_date(start,l):
   current = start
   if l < 30:
       while l >= 0:
          curr = current + datetime.timedelta( minutes = randrange(8), seconds = randrange(30) )
          yield curr
          current = curr
          l-=1
   elif l < 100 and l >= 30 :
       while l >= 0:
           curr = current + datetime.timedelta( minutes=randrange(6), seconds = randrange(10))
           yield curr
           current = curr
           l -= 1
   elif l < 200 and l >= 100:
       while l >= 0:
           curr = current + datetime.timedelta(minutes=randrange(4), seconds=randrange(10))
           yield curr
           current = curr
           l -= 1
   else:
       while l >= 0:
           curr = current + datetime.timedelta(seconds = randrange(8), milliseconds = randrange(100))
           yield curr
           current = curr
           l -= 1


def return_data(time_length, hour_time_loop, minutes_time_loop = 0):
   list_time =[]
   startDate = datetime.datetime(2018, 12, 13, hour_time_loop, minutes_time_loop)
   for x in random_date(startDate, time_length):
       list_time.append(x.strftime("%d/%m/%y %H:%M:%S"))
   return  list_time


def creating_data_in(start_time, end_time, list_total_peopple):
    hour_time_loop = start_time
    minutes_time_loop = 0
    total_peopple = list_total_peopple
    x = 0
    index_total_people = 0
    global number_people_in
    global people_id
    global list_number_people_in
    global  total_people_in #test


    while True:
        total_people_item = total_peopple[index_total_people]
        date_time_in_hour = return_data(total_people_item, hour_time_loop, minutes_time_loop)
        index_time = 0
        for x in range(total_people_item):
            date_time_in = date_time_in_hour[index_time]
            list_item_in = ["in",date_time_in]
            total_people_in += 1 #test
            print (str(list_item_in) +"...." + str(total_people_in)) #test
            list_number_people_in.append(list_item_in)
            index_time += 1
        #timeLoop += 1
        datetime_last = datetime.datetime.strptime(date_time_in_hour[index_time-1], "%d/%m/%y %H:%M:%S")
        hour_time_loop = datetime_last.hour
        minutes_time_loop = datetime_last.minute
        index_total_people += 1

        if(index_total_people ==(end_time - start_time)+1):
            break


def creating_data_Out(start_time, endTime, list_total_peopple):
    hour_time_loop = start_time
    total_peopple = list_total_peopple
    minutes_time_loop = 0
    x = 0
    index_total_people = 0
    global number_people_out
    global people_id
    global list_number_people_out
    global total_people_out

    while True:
        total_peopple_item =  total_peopple[index_total_people]
        date_time_in_hour = return_data(total_peopple_item, hour_time_loop, minutes_time_loop)
        index_time = 0
        for x in range(total_peopple_item):

            date_time_out = date_time_in_hour[index_time]
            list_item_out = ["out", date_time_out]
            total_people_out +=1 #test
            print (str(list_item_out) + "...." + str(total_people_out)) #test
            list_number_people_out.append(list_item_out)
            index_time += 1

        datetime_last = datetime.datetime.strptime(date_time_in_hour[index_time - 1],"%d/%m/%y %H:%M:%S")
        hour_time_loop = datetime_last.hour
        minutes_time_loop = datetime_last.minute
        index_total_people += 1
        if (index_total_people == (endTime - start_time) + 1):
            break

def sorting_data(list_number_people_in, list_number_people_out):
    people_id = 0
    number_people_out = 0
    number_people_in = 0
    total_list = list_number_people_in + list_number_people_out

    total_list.sort(key=lambda L: datetime.datetime.strptime(L[1], "%d/%m/%y %H:%M:%S"))
    for data_item in total_list:
        people_id += 1
        if data_item[0] == 'in':
            number_people_in += 1
            record_data(people_id = people_id ,total_people_in = number_people_in , time_people_in = data_item[1], total_people_out = number_people_out, time_people_out = 'null' )
        elif data_item[0] == 'out':
            number_people_out += 1
            record_data(people_id = people_id, total_people_in = number_people_in, time_people_in = 'null',
                        total_people_out = number_people_out, time_people_out = data_item[1])






list_total_peopple = [30, 450, 450, 50, 20]
list_total_peopple_out_scatted =[50, 700 , 30]
list_total_peopple_in_scatted = [500, 150, 50, 30, 20]

creating_data_in(7, 11, list_total_peopple)
creating_data_Out(9, 11, list_total_peopple_out_scatted)
creating_data_in(12, 16, list_total_peopple_in_scatted)
creating_data_Out(16, 20, list_total_peopple)
sorting_data(list_number_people_in, list_number_people_out)










