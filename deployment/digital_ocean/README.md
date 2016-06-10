
This is an ansible deployment script for the HemeWeb architecture
specific for Digital Ocean.



How to use

```bash


# Credentials stuff
export DO_API_TOKEN=<put access key>

# Disable host key check
export ANSIBLE_HOST_KEY_CHECKING=False


# Provision EC2 instances
ansible-playbook provision.yml


# You can dynamically query hostfile with this script
./ec2.py --list


# Configure all instances
ansible-playbook -i ./ec2.py --private-key=<path to private key>  -u ubuntu deploy.yml


# SSH to manager node
ssh -i <path to private key> ubuntu@<public-dns-ip-of-manager-node>


# run HemeLB
mpirun.openmpi --mca btl_tcp_if_include eth0  -np 8  --host hemelb-node-1,hemelb-node-2 hemelb -in /shared/input.xml -out /shared/result/


```

