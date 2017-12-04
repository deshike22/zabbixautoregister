import sys
from zabbixauth import zabbix_auth

server = 'http://192.168.99.100:32809/'
username = 'Admin'
password = 'zabbix'

zapi = zabbix_auth(server, username, password)

metadata = {"OS": "Linux", "APP": "Zabbix", "ENV": "TEST", "TYPE": "DB", "SW": ["APACHE", "MSSQL"]}
# print "metadata length", len(metadata)
hostname = 'zab-agent01'


# print "datatype :", type(metadata)


def gethostid(zapi, name):
    hostid = zapi.host.get({
        "name": name,
        "output": "extend"
    })[0]['hostid']
    return hostid


def gethostgroupids(zapi, groups):
    groupids = []
    for group in groups:
        print group
        try:
            groupid = zapi.hostgroup.get({
                "output": "extend",
                "filter": {
                    "name": [group]
                }
            })[0]['groupid']
            groupids.append(groupid)
            print "host groups already exists", groupid
        except:
            groupid = zapi.hostgroup.create({
                "name": group
            })['groupids']
            groupids.append(groupid)
            print "new group created", groupid
    print groupids
    return groupids


def getgroupnames(metadata):
    groupnames = []
    for k, v in metadata.iteritems():
        if type(v) is list:
            for i in v:
                # print i
                groupnames.append(i)
        else:
            # print v
            groupnames.append(v)
    return groupnames


def createnestedgroups(metadata):
    groupnames = []
    groupnames.append(metadata["APP"])
    groupnames.append(groupnames[-1] + "/" + metadata["ENV"])
    groupnames.append(groupnames[-1] + "/" + metadata["TYPE"])
    for i in metadata["SW"]:
        groupnames.append(groupnames[-1] + "/" + i)
    print groupnames
    return groupnames


def updatehost(zapi, metadata, hostid, groupids):
    zapi.host.update({
        "hostid": hostid,
        "groups": [{
            "groupid": groupids[len(groupids) - 1]}],
        "inventory": {
            "notes": str(metadata)
        }
    })
    return True


def addhosttogroups(zapi, groupids, hostid):
    for id in groupids:
        zapi.hostgroup.massadd({
            "groups": [{
                "groupid": id
            }],
            "hosts": [{
                "hostid": hostid
            }]
        })


hostid = gethostid(zapi, hostname)
# groupnames = getgroupnames(metadata)
groupnames = createnestedgroups(metadata)
groupids = gethostgroupids(zapi, groupnames)
updatehost(zapi, metadata, hostid, groupids)
