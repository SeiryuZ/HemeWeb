
This is an ansible deployment script for the HemeWeb architecture
specific for Digital Ocean.




How to use

```bash


# Credentials stuff
export DO_API_TOKEN=<put access key>

# Disable host key check
export ANSIBLE_HOST_KEY_CHECKING=False


# Provision droplet instances
ansible-playbook provision.yml


# You can dynamically query hostfile with this script
./digital_ocean.py --list


# However, because we cannot put tags on the droplets, we have to do
# some post processing to the dynamic query script
./hemeweb_digital_ocean.py

# Script above will update / create hosts file to use for our deployment


# Configure all instances
ansible-playbook -i hostsfile  deploy.yml


# SSH to master node
ssh root@<ip of master>


# run HemeLB
mpirun.openmpi --mca btl_tcp_if_include eth0  -np 8  --host hemelb-node-1,hemelb-node-2 hemelb -in /shared/input.xml -out /shared/result/


```

