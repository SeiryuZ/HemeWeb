# **Plan for HemelWeb (Tentative Name)**

## Important Dates
1. **15th April 2016**, Due date of Informatics Research Proposal
2. **31st March 2016**, Due date of AWS research grant


## Plan of Attack
From the discussion on 24th February 2016, basically these are the steps roughly we are going to take for this project:

### 1) Separate HemelB core into its own container
This is a straight-forward step. Whatever the implementation in the end, having HemelB on its own container, separately from the container which contains the whole workflow from setup step is better. We want to have a HemelB-core only clusters that do not need other part.

**Decision Point!**
a)  (Alan asked) Do we even need docker container? Yes, the purpose of having HemelB core packaged into its own container on dockerhub is that people can easily install HemelB core on their own. It's not a required step for this project to be successful, but it will benefit the community for easy distribution of HemelB core.

### 2) Orchestrate the deployment of HemelB cluster

We need tools to deploy HemelB core as a compute server in AWS easily. There are few possible tools:

1. CfnClusters, basically python CLI with boto lib, optimized for HPC, [doc](http://cfncluster.readthedocs.org/en/latest/hello_world.html)
2. Ansible, more general-purpose system automation, [Ansible-Docker](https://www.ansible.com/docker)
3. Chef [doc](https://www.chef.io/chef/)
4. Other deployment tools

**Decision Point!**
Decide which tools is more appropriate for the task of deploying the cluster

### 3) Decide on which implementation we are going to use

Depending on the time frame and the technical difficulties, we need to decide on which implementation we should aim for:

#### A) *HemelB core on the cloud, setup on desktop (Hybrid)*
* **Succes criteria**: The simulation is done in the cloud, while the setup process is still done in the user's own desktop:

1. User process the blood vessel microscopic image on their desktop
2. Upload the output from the setup tools (STL & Profile files) to the web interface
3. Simulation will be run with the input from step 2
4. User got an email that simulation is done
5. User can download the simulation result to be viewed on desktop



#### B) *The whole Blood Simulation running as a web service*
* **Success criteria**: The whole simulation workflow is done via web browser:

1. User upload the blood vessel microscopic image to the web interface
2. Web server build the blood vessels' 3d model from the uploaded image (utilizing a cluster of AWS GPU instances)
3. User got an email that tells them that their blood vessel model is ready
4. User then set inlet and outlet of blood for the models using web browser and set few parameters to be used for the simulation then click simulate
5. The setup tools will create few files (STL and profile files) for the HemelB core
6. The HemelB core clusters will run with input produced from step 5
7. User got an email that simulation is done
8. User can view the result on the simulation on browser, or download the file for desktop viewing

* **What I don't know currently**:
	* How to use AWS GPU instance, what makes it different
	* Paraview server configuration (Paraview Web is just a python webserver that communicate with paraview to provide data to javascript library in the browser)
	* How HemelB setup process use paraview
	* How the setup process model the blood vessel, can it be done in the AWS GPU instance?

* **Related Resources**:
  * [AWS GPU instance information](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using_cluster_computing.html)
  * [Paraview Web is just paraview with python server](http://www.paraview.org/ParaView3/Doc/Nightly/www/js-doc/index.html#!/guide/quick_start)


#### C) *Stream the whole simulation from AWS GPU instance*
* **Success criteria**: The whole simulation is packaged as a desktop enabled container and run on AWS GPU instance. User then stream the desktop environment on AWS to their own desktop

* **What I don't know currently**:
	* Streaming technology


* **Related Resources**:
	* Someone running Witcher 3 on AWS GPU Instance and stream the session to macbook http://lg.io/2015/07/05/revised-and-much-faster-run-your-own-highend-cloud-gaming-service-on-ec2.html


**Decision Point!**
Decide which approach we are going to take.  I don't really think
choosing which approach to take will merit its own literature review(?),
as it is only dependant on me being familiar with the tools and whether
my estimate of the workload of each approach fit the timeframe.


## Other related issues

### A) Intellectual Property issues with Indonesia Endowment Fund for Education(LPDP/ Indonesian Government)
I have to make sure that we are on the clear on the IP issues. HemelB is in LGPL3, so HemelWeb should also be LGPL3. Will the Indonesian Government be okay with having their name on the web interface and my dissertation report (Some kind of *"This project is supported/funded by the Indonesian Government"*)? Technically, as per license, they can not prevent somebody working on them.

**Status**
Still waiting for response from the IG



## Resources

* ✓ [Shifter Paper](https://www.nersc.gov/assets/Uploads/cug2015udi.pdf)
* ✓ [Shifter Press release](https://www.nersc.gov/news-publications/nersc-news/nersc-center-news/2015/shifter-makes-container-based-hpc-a-breeze/)
* [Nekkloud: A Software Environment for High-order
Finite Element Analysis on Clusters and Clouds](https://www.chriscantwell.co.uk/wp-content/uploads/2013/09/nekkloud.pdf)
* [Massively parallel fluid simulations on
Amazon’s HPC cloud](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=6123441)

---
* http://dl.acm.org/citation.cfm?id=2287045  << Down, at time of writing
* CFD Direct, [link](http://cfd.direct/cloud/) << Not sure what to do with this yet
	
