import sys, json
from datetime import datetime
from collections import Counter

inputfile = sys.argv[1]

def count_items(listofitems):
    listofitems_counted = Counter()
    for d in listofitems:
        listofitems_counted[d] += 1
    return(listofitems_counted)

times = []
with open(inputfile,'r') as f:
    for i in f:
        i = i.strip()
        i = i.split(',')
        raw_dt = "{}".format(i[0]).split('.')[0]
        # 25-Jan-2018 11:51:10.956 would use '%d-%b-%Y %H:%M:%S'
        # 2017-10-25 03:01:42 would use '%Y-%m-%d %H:%M:%S'

        datetime_object = datetime.strptime(raw_dt, '%Y-%m-%d %H:%M:%S')
        # print(datetime_object)
        times.append(datetime_object)
        
tq = []
total_queries_count_of_stuff = count_items(times)
for key, value in total_queries_count_of_stuff.items():
    z = {'value':value,'date':str(key)} # Create Dataframe
    tq.append(z)

json.dump(tq, open('static/data/query_count.json','w'))