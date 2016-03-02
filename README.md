# **Plan for HemeWeb (Tentative Name)**

## Important Dates

1. **31st March 2016**, Due date of AWS research grant
2. **15th April 2016**, Due date of Informatics Research Proposal
3. **2nd June 2016**, Official start of work on the projects
4. **Early July**, Presentation of project progress to peer
5. **19th August 2016**, Noon, deadline for dissertation submission


## Plan of Attack
These are the steps we are going to take for this project:

### 1) Separate HemeLB core into its own container
This is a straight-forward step. Whatever the implementation in the end, having HemeLB on its own container, separately from the container which contains the whole workflow from setup step is better. We want to have a HemeLB-core only clusters that do not need other part.

**Decision Point!**
a)  (Adam asked) Do we even need docker container? Yes, the purpose of having HemeLB core packaged into its own container on dockerhub is that people can easily install HemeLB core on their own. It's not a required step for this project to be successful, but it will benefit the community for easy distribution of HemeLB core.

### 2) Orchestrate the deployment of HemeLB cluster

We need tools to deploy HemeLB core as a compute server in AWS easily. There are few possible tools:

1. CfnClusters, basically python CLI with boto lib, optimized for HPC, [doc](http://cfncluster.readthedocs.org/en/latest/hello_world.html)
2. Ansible, more general-purpose system automation, [Ansible-Docker](https://www.ansible.com/docker)
3. Chef [doc](https://www.chef.io/chef/)
4. Other deployment tools

**Decision Point!**
Decide which tools is more appropriate for the task of deploying the cluster

### 3) Develop web interface to accept user input

This web interface should receive two files(.xml + .gmy) that will be
fed to the HemeLB core clusters. After simulation is done, an .xpf file
will be available for download to the user.




## Other related issues

### A) Intellectual Property issues with Indonesia Endowment Fund for Education(LPDP/ Indonesian Government)
I have to make sure that we are on the clear on the IP issues. HemeLB is in LGPL3, so HemeWeb should also be LGPL3. Will the Indonesian Government be okay with having their name on the web interface and my dissertation report (Some kind of *"This project is supported/funded by the Indonesian Government"*)? Technically, as per license, they can not prevent somebody working on them in the future.

**Status**
Still waiting for response from the IG



## Resources

* ✓ [Shifter Paper](https://www.nersc.gov/assets/Uploads/cug2015udi.pdf)
* ✓ [Shifter Press release](https://www.nersc.gov/news-publications/nersc-news/nersc-center-news/2015/shifter-makes-container-based-hpc-a-breeze/)
* ✓ [Nekkloud: A Software Environment for High-order
Finite Element Analysis on Clusters and Clouds](https://www.chriscantwell.co.uk/wp-content/uploads/2013/09/nekkloud.pdf)
* [Massively parallel fluid simulations on
Amazon’s HPC cloud](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=6123441)

---
* http://dl.acm.org/citation.cfm?id=2287045  << Down, at time of writing
* CFD Direct, [link](http://cfd.direct/cloud/) << Not sure what to do with this yet
	
