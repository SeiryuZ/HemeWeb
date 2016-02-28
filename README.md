# **Plan for HemelWeb (Tentative)**

---
## Important Dates
1. **15th April 2016**, Due date of Informatics Research Proposal
2. **31st March 2016**, Due date of AWS research grant


## Plan of Attack
From the discussion on 24th February 2016, basically we agreed that there are 3 possible approach for this project:

#### A) HemelB core on the cloud, setup on desktop (Hybrid)
* **Succes criteria**: Web interface for the HemelB core take input of STL and profile file from the setup process on desktop and produce the simulation result correctly for download on the web
* **What I don't know**: 
	* HemelB core installation procedure, dependencies.
	* Orchestrating HemelB core deployment to AWS
	* We need a web interface to communicate with HemelB core clusters

#### B) The whole Blood Simulation running as a web service
* **Success criteria**: The whole simulation workflow is done via web browser:
1. User upload the blood vessel microscopic image to the web interface
2. Web server build the blood vessels' 3d model from the uploaded image (utilizing a cluster of AWS GPU instances)
3. User got an email that tells them that their blood vessel model is ready
4. User then set inlet and outlet of blood for the models using web browser and set few parameters to be used for the simulation then click simulate
5. The setup tools will create few files (STL and profile files) for the HemelB core
6. The HemelB core clusters will run with input produced from step 5
7. User got an email that simulation is done
8. User can view the result on the simulation on browser, or download the file for desktop viewing

* **What I don't know**: 

* **Resources**:
  * a

#### C) Stream the whole simulation from AWS GPU instance
* **Success criteria**: The whole simulation is packaged as a desktop enabled container and run on AWS EC2, streamed to the user

* **What I don't know**: 


* **Resources**:
	* Someone running Witcher 3 on AWS GPU Instance and stream the session to macbook http://lg.io/2015/07/05/revised-and-much-faster-run-your-own-highend-cloud-gaming-service-on-ec2.html
	  

## Outstanding issues 

### A) Intellectual Property issues with Indonesian Government



