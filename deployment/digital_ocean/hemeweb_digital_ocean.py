#! /usr/bin/env python

import subprocess
import json


# Call the dynamic inventory file provided by ansible
result = subprocess.Popen("./digital_ocean.py", shell=True, stdout=subprocess.PIPE)

# convert json to dict
do_hosts = result.stdout.readlines()[0]
do_hosts = json.loads(do_hosts)


# Get relevant IP
all_hosts = do_hosts['all']['hosts']
master_host = do_hosts['master']


# Create the correct groups for worker
worker_nodes = set(all_hosts) - set([master_host])


# Update the hostfile
with open('hostsfile', 'w') as _file:
    _file.write("[master]\n")
    _file.write("%s ansible_user=root\n" % master_host)

    _file.write("\n[workers]\n")
    for worker in worker_nodes:
        _file.write("%s ansible_user=root\n" % worker)


print "Digital Ocean Hostfile writed successfully"
