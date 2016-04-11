# HemeWeb: Container based high performance computing scenario for HemeLB


## Introduction

HemeLB is a fluid dynamic simulation software that is developed for the study of blood flow [1]. Researches in bioinformatic area have used HemeLB to help with their study. Some study use HemeLB to simulate blood vessel development in mouse [2] and its retina [3]. Another used HemeLB to study vascular blood flow abnormalities in human eye [4]. With these studies, it is clear that HemeLB is an important part of medical study. Furthermore, HemeLB is envisioned to be an integral part of medical decisions[5].

However, it is currently complex to configure and run simulations with it. HemeLB simulation comprises of many steps in the workflow that need a diverse set of tools to run. Scientists and doctors might not have the capabilities to configure these tools. Furthermore, resources needed to run these workflow also varies. One part of the workflow need normal consumer-grade computing resource. Yet, another part of the workflow need a highly-parallel computing resource like ARCHER supercomputer. Not only that, interface required on each workflow also differ from one another. All these reasons limits HemeLB users to few individuals currently.

In this project, I propose an alternative interface to HemeLB simulation workflow. This alternative will be in the form of web application called HemeWeb. HemeWeb will provide an alternative interface for user to run HemeLB blood flow simulations. Furthermore, it will also enable ease of reproduction and audit of the simulations. This is important to make simulation results more trustworthy in general.

In past few years many complex applications have been developed in the cloud. But, for our exact use case, none have been developed. I will try to highlight similar project to this proposed approach.

One similar project is Nekkloud [6]. Here, a web interface is developed as an alternative to their original workflow. This original workflow involves around many steps to run Nektar++ high-order finite element code. Besides being complex, acquiring resources are also hard. Nekkloud is developed to encapsulate all these difficulties while providing access to Nektar++ software. Using a web interface to provide a high level interface instead of using command line. This is parallel with how the proposed project can improve HemeLB.

Another project that is tackling similar space is Galaxy [7]. Galaxy, a web-based reproducible research platform, use cloud infrastructure to run its HPC application. In illustrating its use, the developer has developed a super-resolution spark (SRS) model. This model need a supercomputing resources to execute which cloud infrastructure could handle. These capabilities are also encapsulated in an easy to use web interface. Making it easy for scientists to run, and share simulations with the public.

Above examples illustrate that web application is a viable alternative interface for complex applications. It allows users without HPC expertise to easily run the needed applications. However, this implementation on the cloud also have negative impact. Raw performance are lower than dedicated HPC infrastructures as observed in [6][8][9].  Nekkloud project consider the performance penalty is acceptable and I tend to agree. HemeWeb will also provide web interface for HemeLB simulation workflow with necessary performance penalty.

Pros and cons of web interface for HPC applications are area that are often discussed.  But, rarely deployment scenario for these HPC application in cloud infrastructure are discussed. In this project I will also use containerization technology to deploy the HPC tools. This will be the novel approach that this project will take. Not only having a web interface, deployed HPC application will use containerization technology. 

It has to be noted that HemeWeb is not the first project to use containerization technology in cloud. Galaxy [10], has a docker integration that allow tools to be packaged with it. According to their publication [10], docker allow efficiency, isolation, and portability in  the tools. However, their main focus is how the web application will support reproducible research. The usage of containerization technology are rarely detailed. 


Containerization technology are often benchmarked in high performance computing area. These researches [11][12] have tried to discuss using container technology in HPC space. Also, shifter project [13] that try to unleash docker on HPC infrastructure. Yet, none have discussed the effect of containerization in running HPC application in cloud. This is where HemeWeb will try to put its focus on. How container technology will help HPC application to be more trustworthy. This is even more important when there are many push for open science. More specifically, the push for easy reproduction of complex computations [15][16]. This is also where containerization technology like docker, show its benefit [17].

In this project, I propose to create an extension to HemeLB workflow called HemeWeb. HemeWeb will be a web application that use containerization technology to deploy its tools. As argued before, HemeWeb will contribute to HemeLB project by providing an alternative interface. An interface that enable user without significant HPC training to run HemeLB simulations. On top of that, this project can contribute to the "HPC application in the cloud" area of research.



## Current HemeLB workflow


![alt text](../resources/images/HemeLB-workflow.png "HemeLB current workflow")

Image above illustrate the overview of the current HemeLB simulations workflow. Currently there are many steps requiring different interface and computing resources. Making it complex for a user to run simulation. In this section, I will attempt to elaborate on the each of the workflow steps. This is important, because it will be the basis of the implementation in the next section.

1. **Geometrical model reconstruction**

  ![alt text](../resources/images/HemeLB-workflow-steps-1.png "Geometrical model reconstruction")

  This is the initial entry point for a user wanting to run a simulation with HemeLB. HemeLB simulation need a 3D model of blood vessel that is reconstructed from 2D image. A script will take 2D image of blood vessel  and construct its 3D model. This step is known as Geometrical model reconstruction and it outputs an .stl file. This process needs a highly-parallel computing resources that it usually run on supercomputers. This step, however, are outside the scope of this project.

2. **Domain definition**

  ![alt text](../resources/images/HemeLB-workflow-steps-2.png "Domain defiition")

  The next step in the pipeline is the domain definition step. In this step, users input about simulation parameters are needed. User need to configure simulation parameters like blood viscosity, inlet and outlet placements. These parameters are important because it will affect the simulation results. A graphical user interface have been developed for this purpose. This tools allow users to specify the parameters without using command line interface. Allowing doctors and users to use it easily on their own personal computer. These information are then encoded into a profile file that will be used in the next step.

3. **Geometry generation**

  ![alt text](../resources/images/HemeLB-workflow-steps-3.png "Geometry generation")

  In this step, the 3D model of blood vessel and the simulation parameters are converted. HemeLB are unable to parse the intermediate representation of data from domain definition step. Thus, conversion into a format that it can parse is necessary. This process is lightweight and done via a script. It can run easily on consumer-grade computing resources with a command line interface.

4. **HemeLB simulation**

  ![alt text](../resources/images/HemeLB-workflow-steps-4.png "HemeLB simulation")

  This step is where the bulk of the computations are done. Informations encoded from previous steps are used by HemeLB instances to run the simulation. This simulation usually run on a highly-parallel computing resources like ARCHER supercomputer. These input files are then shared to all instances by means of network attached file system. This process will output many files that encode information about the simulation results. These are .xtr files, .dat files, .txt , and a .xml file.

5. **Post processing**

  ![alt text](../resources/images/HemeLB-workflow-steps-5.png "Post processing")

  Simulation results from previous steps are encoded in a format that is not easily viewed. To view the simulation in a graphical way, further processing is needed. This is where post-processing steps will do its work. This step will convert the files into a format that can be viewed in GTK viewer. This process can run on consumer-grade hardware without problems.




## Implementation



  HemeWeb will be a web application that hides the complexity of running HemeLB simulations. Web application will enable users to interface with a HemeLB simulation via internet browser. Internet browser is such a standard tools that many people can use. Allowing doctors and scientists to run simulation without worry of configurations and complexity.

  Besides being a web application, HemeWeb will also use containerization technology. Allowing the web app to tie down simulation result with the tools used. Having this automatic record will enable easy reproduction and easy audit for interested parties. Furthermore, using container technology will allow HemeWeb to swap tools. Currently, to run simulation with different version of the tools, one should reconfigure everything. Container technology will allow HemeWeb to swap the tools easily. Allowing users to run simulation with different version of tools without worrying about configurations.

  ![alt text](../resources/images/HemeWeb-scope.png "HemeWeb scope")

  In a nutshell, HemeWeb will replace part of HemeLB simulation workflow like illustrated above. The first phase of the development will make sure one of the steps to run simulation can run in the cloud. With more and more integrations, more part of the workflow will run in the cloud. This will pave ways for making the simulation workflow run entirely on the browser. Making it even easier for users to run simulation.

  In the following section, I will outline how the development of HemeWeb will go. I have divided the development into 5 separate distinct steps. They are:

  1. **Separating HemeLB core into its own container**

      Currently, users need to compile HemeLB and other tools on their own computer before using it. These configurations are complex and need simplification. Hence, developer of HemeLB created a container image with complete tools inside, https://github.com/mobernabeu/docker-hemelb. However, for HemeWeb, this is not ideal. HemeWeb should use a cluster of HemeLB instances to run the simulation. These cluster should just contain HemeLB core instead of having the full tools available. This is why, separating this HemeLB core into its own container should be my first step for this project. I will take the currently available image as a basis, and remove all the unnecessary tools. HemeLB binary should be the only concern of the image.

  2. **Orchestrate HemeLB cluster deployment**

      Next, I plan to create a deployment script for HemeLB. I have select preliminary tools for deploying the HemeLB image into a cluster. However, further investigation in the project execution will be necessary. These tools will configure the cluster in an automatic fashion so that it is ready for use. I will be able to configure the cluster with a script at the end of this task.

  3. **Develop HemeWeb to do HemeLB simulation [Phase 1]**

      This is the first step that HemeWeb will be able to run HemeLB simulations. I will develop the prototype web interface that enable user to run simulation. User can upload their input files, wait for the simulation to finish, and download the result.  In this step, I will have developed a working prototype. This prototype have the smallest scope possible, but still allow simulations to run.  The system should look like the image below.

      ![alt text](../resources/images/HemeWeb-phase-1.png "Phase 1 of HemeWeb")

  4. **Extends HemeWeb to handle geometry generation step [Phase 2]**

      After finishing with the previous step, I will extend HemeWeb to handle more functions. This function is the geometry generation step. This step will not result in a different interface for the users, but it will expects different input. After this step is complete, HemeWeb will now work with extra functionalities. The system should look like the image below.

      ![alt text](../resources/images/HemeWeb-phase-2.png "Phase 2 of HemeWeb")

  5. **Extends HemeWeb to handle domain definition step or post-processing step [Phase 3]**

      At this point, there are two possible extensions available for HemeWeb. They are the domain definition step or post-processing step. Both of these steps need different technical expertise to complete the integration. I will decide on the project execution on which function I should tackle. This decision will depend on the difficulty, and remaining time for the project. However, it has to emphasized that even without this step, HemeWeb can still work just fine.


## Goals of the project

As elaborated above, the project will consists of creating prototype of HemeWeb. HemeWeb will be an alternative interface to run HemeLB simulation than status quo. In an ideal scenario, HemeWeb will need to achieve feature parity with current approach. But, due to limited resources, it should fulfill set of functional requirements outlined below.

First of all, HemeWeb should be able to run HemeLB simulation in the cloud. At least, user should be able to upload input files, wait, and download results. These process will run on cloud, demonstrating that HemeLB can run on other infrastructure. Furthermore, the deployment of the HemeLB core clusters will use containerization technology. These technology is a novel approach in deploying HPC application.

Second, HemeWeb should then continue to integrate more steps of the workflow. In this step, HemeWeb should integrate the geometry generation of the workflow. By adding this step, one more workflow that has to be done in users' computer can run in the cloud.

Finally, HemeWeb should then integrate the domain definition step or the post processing step. These steps will need different skill-set to complete. However, similar with above, this functionality is chosen to offload more workflow to cloud. Making it even more easy to run HemeLB simulations.

It should be noted that I structure the project in a way that allow it to degrade gracefully. Even if HemeWeb does not meet the second or final criteria, it will still be a working prototype. Enabling scientists and doctors an alternative interface to run HemeLB simulation.






## Output


This project will create two outputs that HemeLB project will use. They are:

I will develop the prototype in three phases, divided based on the functionalities. In each phase, the prototype will work as a standalone application just fine. With each iteration, I will add more functions to the prototype. The next section, work plan, will add more details on how I will develop the prototype.

## Risks

As with all projects with limited time and budget, there are risks involved
 in this project. First is the chance of project execution not running as
 planned.  This is why, I structure this project to allow it to gracefully
 degrade. Meaning that the project will always have a working product at each
 checkpoints. This is to make sure that I always having working prototype at
 each iteration of the software. Preventing the chance of having nothing to
 show at the end of the project. Second, is the fact that I have to rely
 on external parties for evaluation. Part of the evaluation of the proposed
 system will consists of sending out questionnaires. I have to make sure that
 respondents complete the questionnaires on time. Thus, I structured the
 evaluation and the development part to run concurrently. Making sure I give
 enough time for respondents and for me to remind them.

## Work Plan

This final section will elaborate the work plan for the project. The project period starts from 2nd of June 2016 to 19th August 2016. In this period, I will work on 4 major tasks. They are the project preparation, execution, evaluation and dissertation writing. Each of these tasks can overlap with each other because of the limited time and many tasks to do. For example, project execution and evaluation will overlap from middle of July. This is intentional because these tasks can run in parallel. With this plan, I have determined that the scope of this project is doable in the duration given. Especially when I structure the project to allow graceful degradation.



![alt text](../resources/images/workplan.png "Work Plan")






















## References

<!--[1] Mazzeo, Marco D., and Peter V. Coveney. "HemeLB: A high performance parallel lattice-Boltzmann code for large scale fluid flow in complex geometries." Computer Physics Communications 178.12 (2008): 894-914.-->


<!--[3] Docker - http://www.docker.com/-->


<!--[5] Cloud Computing and Grid Computing 360-Degree Compared  - I. Foster, Y. Zhao, I. Raicu and S. Lu, "Cloud Computing and Grid Computing 360-Degree Compared," Grid Computing Environments Workshop, 2008. GCE '08, Austin, TX, 2008, pp. 1-10.  doi: 10.1109/GCE.2008.4738445-->


<!--[7] Hey, Tony, and Anne E. Trefethen. "Cyberinfrastructure for e-Science." Science 308.5723 (2005): 817-821.-->

<!--[8] Larson, Stefan M., et al. "Folding@ Home and Genome@ Home: Using distributed computing to tackle previously intractable problems in computational biology." arXiv preprint arXiv:0901.0866 (2009).-->




<!--[15] Marwick, Ben. "Computational Reproducibility in Archaeological Research: Basic Principles and a Case Study of Their Implementation." Journal of Archaeological Method and Theory (2016): 1-27.-->


[1] Itani, M. A., Schiller, U. D., Schmieschek, S., Hetherington, J., Bernabeu, M. O., Chandrashekar, H., ... & Groen, D. (2015). An automated multiscale ensemble simulation approach for vascular blood flow. Journal of Computational Science, 9, 150-155.

[2] Franco, C. A., Jones, M. L., Bernabeu, M. O., Vion, A. C., Barbacena, P., Fan, J., ... & Coveney, P. V. (2016). Non-canonical Wnt signalling modulates the endothelial shear stress flow sensor in vascular remodelling. Elife, 5, e07727.

[3] Franco, C. A., Jones, M. L., Bernabeu, M. O., Geudens, I., Mathivet, T., Rosa, A., ... & Phng, L. K. (2015). Dynamic endothelial cell rearrangements drive developmental vessel regression. PLoS Biol, 13(4), e1002125.

[4] Bernabeu, M. O., Lu, Y., Lammer, J., Aiello, L. P., Coveney, P. V., & Sun, J. K. (2015, August). Characterization of parafoveal hemodynamics associated with diabetic retinopathy with adaptive optics scanning laser ophthalmoscopy and computational fluid dynamics. In Engineering in Medicine and Biology Society (EMBC), 2015 37th Annual International Conference of the IEEE (pp. 8070-8073). IEEE.

[5] Green, C. (2014, June 14). Computer simulation could become 'integral' in the diagnosis, treatment, or prevention of disease by the end of the century | Science | News | The Independent. Retrieved April 4, 2016, from http://www.independent.co.uk/news/science/computer-simulation-could-become-integral-in-the-diagnosis-treatment-or-prevention-of-disease-by-the-9537730.html

[6] Cohen, Johanne, et al. "Nekkloud: A software environment for high-order finite element analysis on clusters and clouds." Cluster Computing (CLUSTER), 2013 IEEE International Conference on. IEEE, 2013.

[7] Walker, M. A., Madduri, R., Rodriguez, A., Greenstein, J. L., & Winslow, R. L. (2016). Models and Simulations as a Service: Exploring the Use of Galaxy for Delivering Computational Models. Biophysical journal, 110(5), 1038-1043.

[8] Mehrotra, Piyush, et al. "Performance evaluation of Amazon EC2 for NASA HPC applications." Proceedings of the 3rd workshop on Scientific Cloud Computing Date. ACM, 2012.

[9] He, Qiming, et al. "Case study for running HPC applications in public clouds." Proceedings of the 19th ACM International Symposium on High Performance Distributed Computing. ACM, 2010.

[10] Moreews, F., Sallou, O., & Bras, Y. L. (2015, July). A curated Domain centric shared Docker registry linked to the Galaxy toolshed. In Galaxy Community Conference 2015.

[11] Higgins, J., Holmes, V., & Venters, C. (2015, July). Orchestrating Docker Containers in the HPC Environment. In High Performance Computing (pp. 506-513). Springer International Publishing.

[12] Yu, H. E., & Huang, W. (2015). Building a Virtual HPC Cluster with Auto Scaling by the Docker. arXiv preprint arXiv:1509.08231.

[13] Jacobsen, D. M., & Canon, R. S. Contain This, Unleashing Docker for HPC.

[14] Donoho, D. L. (2010). An invitation to reproducible computational research. Biostatistics, 11(3), 385-388.

[15] Sandve, G. K., Nekrutenko, A., Taylor, J., & Hovig, E. (2013). Ten simple rules for reproducible computational research. PLoS Comput Biol, 9(10), e1003285.

[16] Peng, R. D. (2011). Reproducible research in computational science. Science (New York, Ny), 334(6060), 1226.

[17] Boettiger, C. (2015). An introduction to Docker for reproducible research. ACM SIGOPS Operating Systems Review, 49(1), 71-79.

<!--[5] Bailey, D. H., & Borwein, J. M. (2013, July 2). Set the Default to "Open": Reproducible Science in the Computer Age. Retrieved April 4, 2016, from http://www.huffingtonpost.com/david-h-bailey/set-the-default-to-open-r_b_2635850.html-->

<!--[6] eScience Institute - Reproducibility and Open Science. (n.d.). Retrieved April 4, 2016, from http://escience.washington.edu/about-us/working-groups/reproducibility-and-open-science/-->

<!--[7] Haines, R. (2016, March 29). Reproducible Research: Citing your execution environment using Docker and a DOI | Software Sustainability Institute. Retrieved April 4, 2016, from http://www.software.ac.uk/blog/2016-03-29-reproducible-research-citing-your-execution-environment-using-docker-and-doi-->

<!--[8] Huerta, M., Downing, G., Haseltine, F., Seto, B., & Liu, Y. (2000). NIH working definition of bioinformatics and computational biology. US National Institute of Health.-->


<!--[10] Merkel, D. (2014). Docker: lightweight linux containers for consistent development and deployment. Linux Journal, 2014(239), 2.-->


<!--[12] Berman, Fran, Geoffrey Fox, and Anthony JG Hey. Grid computing: making the global infrastructure a reality. Vol. 2. John Wiley and sons, 2003.-->

<!--[13] ARCHER » Getting Access to ARCHER. (n.d.). Retrieved April 4, 2016, from http://www.archer.ac.uk/access/-->

<!--[14] PRACE Research Infrastructure. (n.d.). Retrieved April 4, 2016, from http://www.prace-project.eu/-->

<!--[15] Foster, I., & Kesselman, C. (Eds.). (2003). The Grid 2: Blueprint for a new computing infrastructure. Elsevier.-->

<!--[16] Foster, I., Zhao, Y., Raicu, I., & Lu, S. (2008, November). Cloud computing and grid computing 360-degree compared. In Grid Computing Environments Workshop, 2008. GCE'08 (pp. 1-10). Ieee.-->

<!--[17] Extreme Science and Engineering Discovery Environment. (n.d.). XSEDE | TeraGrid Archives. Retrieved April 4, 2016, from https://www.xsede.org/tg-archives-->

<!--[18] FSN ~ Outsourcing ~ The economy is flat so why are financials Cloud vendors growing at more than 90 percent per annum?. (2013, March 5). Retrieved April 4, 2016, from http://www.fsn.co.uk/channel_outsourcing/the_economy_is_flat_so_why_are_financials_cloud_vendors_growing_at_more_than_90_percent_per_annum#.UbmtsPlJPGA/-->

<!--[19] Barr, J. (2014, March 26). AWS Price Reduction #42 – EC2, S3, RDS, ElastiCache, and Elastic MapReduce | AWS Blog. Retrieved April 4, 2016, from https://aws.amazon.com/blogs/aws/aws-price-reduction-42-ec2-s3-rds-elasticache-and-elastic-mapreduce/-->

<!--[20] Martin, S. (2014, January 24). Announcing Reduced Pricing on Storage | Blog | Microsoft Azure. Retrieved April 4, 2016, from https://azure.microsoft.com/en-us/blog/storage-price-match/-->

<!--[21] Lardinois, F. (2014, March 25). Google Announces Massive Price Drops For Its Cloud Computing Services And Storage, Introduces Sustained-Use Discounts. Retrieved April 4, 2016, from http://techcrunch.com/2014/03/25/google-drops-prices-for-compute-and-app-engine-by-over-30-cloud-storage-by-68-introduces-sustained-use-discounts/-->

<!--[22] Whitepaper: An Introduction to High Performance Computing on AWS. (2015, August). Retrieved April 4, 2016, from  https://d0.awsstatic.com/whitepapers/Intro_to_HPC_on_AWS.pdf-->




<!--[26] Sharp, H., Jenny, P., & Rogers, Y. (2007). Interaction design:: beyond human-computer interaction.-->

