# Manager for memory and cpu usage using snmp 


# Prerequisites 
    edit /etc/snmp/snmpd.conf with this line:  
# view   systemonly  included   .1.3.6.1.4.1.8072
    so you can use UCD-SNMP-MIB which includes memory and cpu sensors
# install python3
# install esysnmp library for python3
    pip3 install easysnmp

# ---------

# Description
    Monitor the cpu usage and the memory load every 5 seconds using snmp agent.
    Takes no input. 
    Parameters are bind to :
        hostname=localhost
        community=public
        version=2
    Stop it typing ctrl-c