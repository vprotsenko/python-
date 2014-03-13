'''Should be istalled python-psutil'''

import os, sys, subprocess, psutil, smtplib, datetime, time
from time import gmtime, strftime


#email configuration
from_addr='test@gmail.com'
to_addr_list='test@gmail.com'
cc_addr_list='test@gmail.com'
subject='test_subject'

login='test'
password='test_pass'
smtpserver='smtp.gmail.com:587'

#configs
frequency=30 					#'''How often script check system (in seconds) '''
host = 'google.com'				#'''Nost for pinging  '''
TIMEFORMAT='%m%d %H:%M:%S'			#'''Time format in logs '''
cpu_threshold=80
memory_threshold=10
swap_threshold=40
disc_threshold=50
disc='/'
logStorage='/home/v/dev/utools/scrip_log.1'

#-------Code------------
e_message=[]
def time_in_log():
	return strftime(TIMEFORMAT, gmtime())
def mtr():
	output=subprocess.call('mtr '+ host +  ' -c 2 -r', 
		shell=True,
		stdout=open(logStorage, 'a'),
		stderr=subprocess.STDOUT)
def df():
	output=subprocess.call('df -h', 
		shell=True,
		stdout=open(logStorage, 'a'),
		stderr=subprocess.STDOUT)
def w():
	output=subprocess.call('w', 
		shell=True,
		stdout=open(logStorage, 'a'),
		stderr=subprocess.STDOUT)


def ping():
	output = subprocess.call('ping '+ host +  ' -c 2 |grep "time\|rtt"', 
		shell=True,
		stdout=open(logStorage, 'a'),
		stderr=subprocess.STDOUT)
	if output==0:
		e_message.append("No ping")

def cpu_total():
	output=psutil.cpu_percent(interval=3)
	f=open(logStorage, 'a')
	f.write(str(time_in_log())+"\t CPU usage total = "+str(output)+"\n")
	if output > float(cpu_threshold):
		cpu_total_message="CPU usage is critical="+str(output)
		e_message.append(cpu_total_message)
def cpu_per_core():
	output=psutil.cpu_percent(interval=3, percpu=True)
	f=open(logStorage, 'a')
	f.write(str(time_in_log())+"\t CPU usage per core = "+str(output)+"\n")
	for i in range(len(output)):
		if output[i] > float(cpu_threshold):
			cpu_per_core_message="CPU"+str(i)+" usage is critical="+str(output[i])
			e_message.append(cpu_per_core_message)
def memory():
	output=psutil.virtual_memory()[2]
	f=open(logStorage, 'a')
	f.write(str(time_in_log())+"\t Memory usage = "+str(output)+"\n")
	if output>memory_threshold:
		memory_message="Memory usage is critical ="+str(output)+ "%"
		e_message.append(memory_message)
def swap():
	output=psutil.swap_memory()[3]
	f=open(logStorage, 'a')
	f.write(str(time_in_log())+"\t SWAP usage = "+str(output)+"\n")
	if output>swap_threshold:
		swap_message=" SWAP usage is critical ="+str(output)+ "%"
		e_message.append(swap_message)
def disc():
	output=psutil.disk_usage('/')[3]
	f=open(logStorage, 'a')
	f.write(str(time_in_log())+"\t disc usage = "+str(output)+"\n")
	if output>disc_threshold:
		disc_message=" disc usage is critical ="+str(output)+ "%"
		e_message.append(disc_message)

def sendemail_client(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              login, password,
              smtpserver):
    header  = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message
 
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()


def exact_mail():	
	sendemail_client(from_addr, to_addr_list, cc_addr_list,subject,e_message,login, password,smtpserver)


while True:
	e_message=[]
	df()
	w()
	cpu_per_core()
	cpu_total()
	memory()
	swap()
	disc()
	ping()
	mtr()
	
	exact_mail() #- Sending email
	time.sleep(frequency)

	
