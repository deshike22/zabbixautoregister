import sys
from zabbix_api import ZabbixAPI


# Function to authenticate Zabbix using the credentials provided
def zabbix_auth(server, username, password):
    try:
        zapi = ZabbixAPI(server)
        zapi.login(username, password)
        return zapi
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise
