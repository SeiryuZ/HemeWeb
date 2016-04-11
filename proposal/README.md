# HemeWeb: Container based high performance computing scenario for HemeLB


## Introduction


HemeLB is a fluid dynamic simulation software that is developed for the study
of blood flow [1]. Part of the software construct a 3D model of blood vessels
from a CT scan or microscopic image of them. This 3D blood vessels allow HemeLB to
simulate the flow of fluid, like blood, inside it. Thus, allowing scientists
and doctors to learn how a blood will flow in a given vessels.
Developers of HemeLB envision that it will be an integral part of medical decisions
in the future [9].

Currently, HemeLB usage is complex and hard. It comprises of many steps in the
workflow that need a diverse set of tools to run. Scientists and doctors need
to configure these tools, which need various technical skills. Time and
difficulty for this configuration limits HemeLB users to few individuals.

Furthermore, HemeLB needs to improve the trustworthiness of its simulation.
This trust, on top of HemeLB being usable, is important to make it a part of
 any medical decision. Simulation results should be easy to audit and easy to
 reproduce. These characteristics allow peers to review the simulation and
 confirm the result. Currently, there are measures for HemeLB for easy
 reproduction and audit. Its' source code are available for public on github,
 making it easy to audit the software. Furthermore, researchers have taken a
 manual record of simulation configurations, executions, and results. These
steps allow peers to build the software and replicate a simulation, albeit
 in a manual way.


HemeLB project can further improve its trustworthiness. Simulation record
automation can make it even easier to reproduce and audit a simulation. Recent
 pushes for open science and reproducible computing research [2-7] also
justifies these steps. Allowing the project to stand in a better light
 and in general, more trustworthy.

For reasons above, I propose to create an extension to HemeLB called HemeWeb.
  HemeWeb is a web application that will hide complexity of configuration from
 its users. Also, it will allow automatic record of simulations, making it
 easy to reproduce simulations. I will use cloud infrastructure and
 containerization technology to help address the issues outlined. In brief,
 this proposal will make HemeLB simulations usable and more trustworthy.




## Current HemeLB workflow

To develop the extension with proper functions, I need to elaborate some
 information. These are about the current HemeLB workflow.


**HemeLB Workflow**




![alt text](../resources/images/HemeLB-workflow.png "HemeLB current workflow")

Image above illustrate the current workflow of HemeLB.
Currently, HemeLB need many steps to run simulation.
First, a geometrical model reconstruction step
 will construct a 3D model of the blood vessel from 2D image. Next, user will give simulation parameter
 in the domain definition step. Next, a script will convert these information
 into a format that HemeLB understand. After all this step, one can finally
 run HemeLB simulation. This simulation will output a file that needs further
 pre-processing. This pre-processing steps will then output a file that a
 graphical software like VTK can view.


<!--Currently HemeLB workflow is complex-->
On  top of understanding the above workflow, users also need to configure
 tools needed. These configurations are both complex and time-consuming.
 Making the use case not ideal for scientists and doctors. A better situation
 is where simulations can run without worrying about all these configurations.
 Domain experts should only care about their input to the simulations and the outputs.


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

<!--[2] Goecks et al.: Galaxy: a comprehensive approach for supporting accessible, reproducible, and transparent computational research in the life sciences. Genome Biology 2010 11:R86.-->

<!--[3] Docker - http://www.docker.com/-->


<!--[5] Cloud Computing and Grid Computing 360-Degree Compared  - I. Foster, Y. Zhao, I. Raicu and S. Lu, "Cloud Computing and Grid Computing 360-Degree Compared," Grid Computing Environments Workshop, 2008. GCE '08, Austin, TX, 2008, pp. 1-10.  doi: 10.1109/GCE.2008.4738445-->


<!--[7] Hey, Tony, and Anne E. Trefethen. "Cyberinfrastructure for e-Science." Science 308.5723 (2005): 817-821.-->

<!--[8] Larson, Stefan M., et al. "Folding@ Home and Genome@ Home: Using distributed computing to tackle previously intractable problems in computational biology." arXiv preprint arXiv:0901.0866 (2009).-->




<!--[15] Marwick, Ben. "Computational Reproducibility in Archaeological Research: Basic Principles and a Case Study of Their Implementation." Journal of Archaeological Method and Theory (2016): 1-27.-->


[1] Itani, M. A., Schiller, U. D., Schmieschek, S., Hetherington, J., Bernabeu, M. O., Chandrashekar, H., ... & Groen, D. (2015). An automated multiscale ensemble simulation approach for vascular blood flow. Journal of Computational Science, 9, 150-155.

[2] Donoho, D. L. (2010). An invitation to reproducible computational research. Biostatistics, 11(3), 385-388.

[3] Sandve, G. K., Nekrutenko, A., Taylor, J., & Hovig, E. (2013). Ten simple rules for reproducible computational research. PLoS Comput Biol, 9(10), e1003285.

[4] Peng, R. D. (2011). Reproducible research in computational science. Science (New York, Ny), 334(6060), 1226.

[5] Bailey, D. H., & Borwein, J. M. (2013, July 2). Set the Default to "Open": Reproducible Science in the Computer Age. Retrieved April 4, 2016, from http://www.huffingtonpost.com/david-h-bailey/set-the-default-to-open-r_b_2635850.html

[6] eScience Institute - Reproducibility and Open Science. (n.d.). Retrieved April 4, 2016, from http://escience.washington.edu/about-us/working-groups/reproducibility-and-open-science/

[7] Haines, R. (2016, March 29). Reproducible Research: Citing your execution environment using Docker and a DOI | Software Sustainability Institute. Retrieved April 4, 2016, from http://www.software.ac.uk/blog/2016-03-29-reproducible-research-citing-your-execution-environment-using-docker-and-doi

[8] Huerta, M., Downing, G., Haseltine, F., Seto, B., & Liu, Y. (2000). NIH working definition of bioinformatics and computational biology. US National Institute of Health.

[9] Green, C. (2014, June 14). Computer simulation could become 'integral' in the diagnosis, treatment, or prevention of disease by the end of the century | Science | News | The Independent. Retrieved April 4, 2016, from http://www.independent.co.uk/news/science/computer-simulation-could-become-integral-in-the-diagnosis-treatment-or-prevention-of-disease-by-the-9537730.html

[10] Merkel, D. (2014). Docker: lightweight linux containers for consistent development and deployment. Linux Journal, 2014(239), 2.

[11] Boettiger, C. (2015). An introduction to Docker for reproducible research. ACM SIGOPS Operating Systems Review, 49(1), 71-79.

[12] Berman, Fran, Geoffrey Fox, and Anthony JG Hey. Grid computing: making the global infrastructure a reality. Vol. 2. John Wiley and sons, 2003.

[13] ARCHER » Getting Access to ARCHER. (n.d.). Retrieved April 4, 2016, from http://www.archer.ac.uk/access/

[14] PRACE Research Infrastructure. (n.d.). Retrieved April 4, 2016, from http://www.prace-project.eu/

[15] Foster, I., & Kesselman, C. (Eds.). (2003). The Grid 2: Blueprint for a new computing infrastructure. Elsevier.

[16] Foster, I., Zhao, Y., Raicu, I., & Lu, S. (2008, November). Cloud computing and grid computing 360-degree compared. In Grid Computing Environments Workshop, 2008. GCE'08 (pp. 1-10). Ieee.

[17] Extreme Science and Engineering Discovery Environment. (n.d.). XSEDE | TeraGrid Archives. Retrieved April 4, 2016, from https://www.xsede.org/tg-archives

[18] FSN ~ Outsourcing ~ The economy is flat so why are financials Cloud vendors growing at more than 90 percent per annum?. (2013, March 5). Retrieved April 4, 2016, from http://www.fsn.co.uk/channel_outsourcing/the_economy_is_flat_so_why_are_financials_cloud_vendors_growing_at_more_than_90_percent_per_annum#.UbmtsPlJPGA/

[19] Barr, J. (2014, March 26). AWS Price Reduction #42 – EC2, S3, RDS, ElastiCache, and Elastic MapReduce | AWS Blog. Retrieved April 4, 2016, from https://aws.amazon.com/blogs/aws/aws-price-reduction-42-ec2-s3-rds-elasticache-and-elastic-mapreduce/

[20] Martin, S. (2014, January 24). Announcing Reduced Pricing on Storage | Blog | Microsoft Azure. Retrieved April 4, 2016, from https://azure.microsoft.com/en-us/blog/storage-price-match/

[21] Lardinois, F. (2014, March 25). Google Announces Massive Price Drops For Its Cloud Computing Services And Storage, Introduces Sustained-Use Discounts. Retrieved April 4, 2016, from http://techcrunch.com/2014/03/25/google-drops-prices-for-compute-and-app-engine-by-over-30-cloud-storage-by-68-introduces-sustained-use-discounts/

[22] Whitepaper: An Introduction to High Performance Computing on AWS. (2015, August). Retrieved April 4, 2016, from  https://d0.awsstatic.com/whitepapers/Intro_to_HPC_on_AWS.pdf

[23] Cohen, Johanne, et al. "Nekkloud: A software environment for high-order finite element analysis on clusters and clouds." Cluster Computing (CLUSTER), 2013 IEEE International Conference on. IEEE, 2013.

[24] Mehrotra, Piyush, et al. "Performance evaluation of Amazon EC2 for NASA HPC applications." Proceedings of the 3rd workshop on Scientific Cloud Computing Date. ACM, 2012.

[25] He, Qiming, et al. "Case study for running HPC applications in public clouds." Proceedings of the 19th ACM International Symposium on High Performance Distributed Computing. ACM, 2010.

[26] Sharp, H., Jenny, P., & Rogers, Y. (2007). Interaction design:: beyond human-computer interaction.

[27] Franco, C. A., Jones, M. L., Bernabeu, M. O., Vion, A. C., Barbacena, P., Fan, J., ... & Coveney, P. V. (2016). Non-canonical Wnt signalling modulates the endothelial shear stress flow sensor in vascular remodelling. Elife, 5, e07727.

[28] Franco, C. A., Jones, M. L., Bernabeu, M. O., Geudens, I., Mathivet, T., Rosa, A., ... & Phng, L. K. (2015). Dynamic endothelial cell rearrangements drive developmental vessel regression. PLoS Biol, 13(4), e1002125.

[29] Bernabeu, M. O., Lu, Y., Lammer, J., Aiello, L. P., Coveney, P. V., & Sun, J. K. (2015, August). Characterization of parafoveal hemodynamics associated with diabetic retinopathy with adaptive optics scanning laser ophthalmoscopy and computational fluid dynamics. In Engineering in Medicine and Biology Society (EMBC), 2015 37th Annual International Conference of the IEEE (pp. 8070-8073). IEEE.
