![University of Edinburgh logo](../resources/images/edinburgh-logo.png "University of Edinburgh logo")

## Introduction

Hi there,

I, Steven, am writing my MSc dissertation titled "HemeWeb: Blood flow simulation on the cloud". Today, I will be conducting a usability testing for the project's evaluation with your help.

In this evaluation, I will ask you to run a blood flow simulation using two different approach. Following each simulation, few questions will be asked to measure your experience in using said interface. Also, during the session, your screen will be recorded for evaluation purposes. It is to be noted that there are no right or wrong in running this simulation, so you do not have to worry. If in any of the process, you become uncomfortable, we will stop the session and you are free to leave. This session should last around 20-30 minutes.

Once again, thank you for helping me with my work.


Steven


## About the blood flow simulation

You will run a blood flow simulation using tools called HemeLB.
The software will take sets of input and run
simulation to produce desired outputs from it.


We will compare the usability aspect of the simulation process using two
different interface; command line interface and web interface. You will
be given instruction on how to do use both approaches. But first, some
questions to know you better



## Demographic questions

1. Age
  ... Years old

2. Gender
  * [ ] Male
  * [ ] Female

3. Career stage
  * [ ] MSc student
  * [ ] PhD student
  * [ ] PDRA
  * [ ] Lecturer
  * [ ] Professor

4. Discipline
  * [ ] Informatics / CS
  * [ ] Computational Scientist
  * [ ] Biological Scientist
  * [ ] Clinician
  * [ ] Other ..................

6. Your level of familiarity with installing software from source code ?
  * [ ] Not at all familiar
  * [ ] Slightly familiar
  * [ ] Somewhat familiar
  * [ ] Moderately familiar
  * [ ] Extremely familiar

7. Your level of familiarity with  web browser (Chrome / Safari / IE / Opera)?
  * [ ] Not at all familiar
  * [ ] Slightly familiar
  * [ ] Somewhat familiar
  * [ ] Moderately familiar
  * [ ] Extremely familiar

8. Your level of familiarity with containerization technology like docker?
  * [ ] Not at all familiar
  * [ ] Slightly familiar
  * [ ] Somewhat familiar
  * [ ] Moderately familiar
  * [ ] Extremely familiar

9. Your level of familiarity with computational fluid dynamic tools like HemeLB ?
  * [ ] Not at all familiar
  * [ ] Slightly familiar
  * [ ] Somewhat familiar
  * [ ] Moderately familiar
  * [ ] Extremely familiar




## Running a simulation job using HemeWeb - Instructions

In this section, you will start a blood flow simulation using HemeWeb.

1. With the provided browser, safari, go to http://53.12.13.14 (Ignore
   the address on the image)
  ![Browser](../resources/images/evaluation/browser.png "Browser")

2. Click on add new job
  ![New job](../resources/images/evaluation/new_job.png "New Job")

3. I have prepared two input files to be used. They are in the desktop
   folder.
  ```
  \Users\steven\Desktop\input.xml
  \Users\steven\Desktop\input.gmy
  ```

4. Use the provided input files above for "New job config" form
  ![New job form](../resources/images/evaluation/new_job_form.png "New Job Form")

5. Click "Submit"

6. Configure the simulation with these parameters

   ```
      HemeLB config: No change
      Container Image: SeiryuZ/hemelb-core:0.0.2
      Image type: 8 core
      Instance count: 2
   ```
7. In the "HemeLB config" click on next step
  ![HemeLB config](../resources/images/evaluation/hemelb_config.png "HemeLB Config")

8. In the "Job config" change the job configuration as specified in step 7 and click save
  ![Job config](../resources/images/evaluation/job_config.png "Job Config")

9. In the overview tab and review the parameters one final time

10. Scroll to the bottom and click on "All good! Queue job"


### Questions

1. How difficult do you find the interface to use?
  * [ ] Very difficult
  * [ ] Difficult
  * [ ] Neutral
  * [ ] Easy
  * [ ] Very easy

2. Did the interface give a clear direction / hint on what you should do next?
  * [ ] Very unclear
  * [ ] Unclear
  * [ ] Neutral
  * [ ] Clear
  * [ ] Very clear


## Simulation Command Line

In this section, you will start a blood flow simulation using a command
line interface. You are free to ask for help from the observer, me, and skip
this section if you find it too difficult.

1. Tell me that you are about to start. I will start the screen
   recording software

2. Open terminal (cmd shift t)

3. Your screen should look like this
  ![Terminal](../resources/images/evaluation/terminal.png "Terminal")

4. First, we are going to start two container running hemelb cores
   ```
  docker run -i -d -v ~/Desktop/hemeweb/:/data  -t seiryuz/hemelb-core:0.0.3
  docker run -i -d -v ~/Desktop/hemeweb/:/data  -t seiryuz/hemelb-core:0.0.3
   ```
  *Lines above are intended to be entered twice*

5. Find out the CONTAINER ID of created containers
   ```
  docker ps
   ```
  ![docker ps](../resources/images/evaluation/docker_ps.png "docker ps")

6. Find out the IP of both containers
   ```
  docker inspect --format="{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}" <CONTAINER_ID_1>
  docker inspect --format="{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}" <CONTAINER_ID_2>
   ```
  ![docker inspect](../resources/images/evaluation/docker_inspect.png "docker inspect")

7. Run HemeLB simulation on both containers using this command
   ```
   docker exec <CONTAINER_ID_1> openmpi.mpirun --mca btl_tcp_if_include eth0 \
   -np 4 --host <CONTAINER_IP_1>,<CONTAINER_IP_2> \
   hemelb -in $HEMELB_INPUT -out $HEMELB_OUTPUT 1> $LOG_FILE 2>&1
   ```

8. Tell me, or the person observing you, that you are finished. I will
   stop the screen recording software


## Simulation Command Line - Evaluations

1. How difficult do you find the interface to use?
  * [ ] Very difficult
  * [ ] Difficult
  * [ ] Neutral
  * [ ] Easy
  * [ ] Very easy

2. Did the interface give a clear direction / hint on what you should do next?
  * [ ] Very unclear
  * [ ] Unclear
  * [ ] Neutral
  * [ ] Clear
  * [ ] Very clear




## Overall Evaluation

1. How flexible is the web browser compared to the command line
   interface?
  * [ ] Much worse
  * [ ] Somewhat worse
  * [ ] About the same
  * [ ] Somewhat better
  * [ ] Much better

2. How complex is the web browser compared to the command line
   interface?
  * [ ] Much worse (More complex)
  * [ ] Somewhat worse
  * [ ] About the same
  * [ ] Somewhat better
  * [ ] Much better (Less complex)

3. Overall, which interface do you prefer to use?
  * [ ] Web interface
  * [ ] Command line interface


4. Below are a screenshot of the homepage of the interface and the
   overview of one of the previous simulation.

  Homepage
  ![Homepage](../resources/images/evaluation/homepage.png "Homepage")

  Previous simulation's configuration are preserved
  ![Overview1](../resources/images/evaluation/overview1.png "Overview-1")
  ![Overview2](../resources/images/evaluation/overview2.png "Overview-2")

   Do you think this provide clear information of pasts simulation ?
  * [ ] Very unclear
  * [ ] Unclear
  * [ ] Clear
  * [ ] Very Clear

5. Another goal of the web interface is to easily allow people to
   inspect, reproduce and replicate simulation instances.
   The way the web interface allow these feture is by allowing job to come from
   previous job or other people's experiment file.

  Reproduce previous simulation

  ![Previous simulation](../resources/images/evaluation/reproduce_previous.png "Previous Simulation")

  or Reproduce other people's simulation

  ![Other people's simulation](../resources/images/evaluation/reproduce_other.png "Other people's Simulation")

  The specified previous or other people's simulation's parameter are
preserved and can be modified in the next screen like how we
configure the simulation parameters.

  ![Modify configuration](../resources/images/evaluation/reproduce_conf1.png "Modify configuration")
  ![Modify configuration](../resources/images/evaluation/reproduce_conf2.png "Modify configuration")

   Do you think this web interface allow you to inspect, reproduce and replicate other's simulation easily?
  * [ ] Strongly disagree
  * [ ] Disagree
  * [ ] Agree
  * [ ] Strongly agree
