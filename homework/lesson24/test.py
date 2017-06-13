
import sys
import json

def select_interval(log_path):

    log=open('large.log', 'r').readlines()

    parsed_log=[]

    for line in log:
        splited_line=line.split(" ")[2].split(':')
        minutes=int(splited_line[2])
        if minutes < 40:
            parsed_log.append(str(splited_line[0])+' '+str(splited_line[1]))


    stats=[]
    for i in set(parsed_log):
        date=str(i).split(' ')[0]
        seq=str(parsed_log.count(i))
        hour=str(i).split(' ')[1]


        stats.append("{0} {1}".format(seq, hour))

    sorted_stats=sorted(stats)[0]
    print(sorted(stats))
    #hour_interval=sorted_stats.split(' ')[2]
    #result=[hour_interval+':00',hour_interval+':40']
    #print(result)
    #return result



input_file=open('input', 'r')

log_path=json.load(input_file)['log_path']

select_interval(log_path)

