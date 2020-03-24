#!/usr/bin/python3


#Import
import time
import sys
from easysnmp import Session
from easysnmp import snmp_get, snmp_walk, snmp_set

###########################################################

print('*****************************************')
print()
print('Script information :')
print('using localhost as hostname')
print('using public as community')
print('using v2 as version of snmp')
print()
print('*****************************************')

###########################################################
#Parameters
hostname = 'localhost'
community = 'public'
version = 2


###########################################################
#Create an SNMP session used for the queries 
session = Session(hostname=hostname, community=community, version=version )
starttime=time.time()

###########################################################
print()
print('Polling cpu usage and memory usage over five seconds')
print()
try:
#Retrieve cpu usage and memory usage, then print it and wait for five seconds
	while True :
		cpu_usage=session.get('ssCpuUser.0')
		mem_total=session.get('memTotalReal.0')
		mem_unused=session.get('memAvailReal.0')
		mem_usage=int(mem_total.value) - int(mem_unused.value)
		print('CPU usage: '+ cpu_usage.value + ' %')
		print('Memory usage : ' + str(mem_usage) +' KB')
		time.sleep(5.0 - ((time.time() - starttime) % 5.0))

#Capture Ctrl-C signal from the keyboard to stop the program
except KeyboardInterrupt:
	print()
	print('*****************************************')
	sys.exit()



