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
frequency=30
host = 'google.com'
TIMEFORMAT='%m%d %H:%M:%S'
cpu_threshold=80
memory_threshold=80
swap_threshold=40
disc_threshold=50
disc='/'


def time_in_log():
	return strftime(TIMEFORMAT, gmtime())
def mtr():
	output=subprocess.call('mtr '+ host +  ' -c 2 -r', 
		shell=True,
		stdout=open('/home/v/dev/utools/scrip_log.1', 'a'),
		stderr=subprocess.STDOUT)
def df():
	output=subprocess.call('dh -h', 
		shell=True,
		stdout=open('/home/v/dev/utools/scrip_log.1', 'a'),
		stderr=subprocess.STDOUT)
def w():
	output=subprocess.call('w', 
		shell=True,
		stdout=open('/home/v/dev/utools/scrip_log.1', 'a'),
		stderr=subprocess.STDOUT)


def ping():
	output = subprocess.call('ping '+ host +  ' -c 2 |grep "time\|rtt"', 
		shell=True,
		stdout=open('/home/v/dev/utools/scrip_log.1', 'a'),
		stderr=subprocess.STDOUT)
	if output==0:
		exact_mail("No ping")

def cpu_total():
	output=psutil.cpu_percent(interval=3)
	f=open('/home/v/dev/utools/scrip_log.1', 'a')
	f.write(str(time_in_log())+"\t CPU usage total = "+str(output)+"\n")
	if output > float(cpu_threshold):
		cpu_total_message="CPU usage is critical="+str(output)
		exact_mail(cpu_total_message)
def cpu_per_core():
	output=psutil.cpu_percent(interval=3, percpu=True)
	f=open('/home/v/dev/utools/scrip_log.1', 'a')
	f.write(str(time_in_log())+"\t CPU usage per core = "+str(output)+"\n")
	for i in range(len(output)):
		if output[i] > float(cpu_threshold):
			cpu_per_core_message="CPU"+str(i)+" usage is critical="+str(output[i])
			exact_mail(cpu_per_core_message)
def memory():
	output=psutil.virtual_memory()[2]
	f=open('/home/v/dev/utools/scrip_log.1', 'a')
	f.write(str(time_in_log())+"\t Memory usage = "+str(output)+"\n")
	if output>memory_threshold:
		memory_message="Memory usage is critical ="+str(output)+ "%"
		exact_mail(memory_message)
def swap():
	output=psutil.swap_memory()[3]
	f=open('/home/v/dev/utools/scrip_log.1', 'a')
	f.write(str(time_in_log())+"\t SWAP usage = "+str(output)+"\n")
	if output>swap_threshold:
		swap_message=" SWAP usage is critical ="+str(output)+ "%"
		exact_mail(swap_message)
def disc():
	output=psutil.disk_usage('/')[3]
	f=open('/home/v/dev/utools/scrip_log.1', 'a')
	f.write(str(time_in_log())+"\t disc usage = "+str(output)+"\n")
	if output>disc_threshold:
		disc_message=" disc usage is critical ="+str(output)+ "%"
		exact_mail(disc_message)

def sendemail(from_addr, to_addr_list, cc_addr_list,
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


def exact_mail(message):	
	sendemail(from_addr, to_addr_list, cc_addr_list,subject,message,login, password,smtpserver)

while True:
	
	ping()
	mtr()
	df()
	w()
	disc()
	cpu_per_core()
	cpu_total()
	memory()
	swap()
	time.sleep(frequency)
	
