# EchoRob
Recurrent Neural Network for Syntax Learning with Flexible Representations for Robotic Architectures

## Want to be updated?
Drop me an email if you want to be updated by new features, corpa or versions of the model are available:
xavier dot hinaut at inria dot fr

## Intro on Reservoir Computing
Reservoir Computing (RC) is a type of Recurrent Neural Network used in this EchoRob project. Namely we use an instance of RC called Echo State Networks (ESN).

Here you can find the [ReservoirPy](https://github.com/neuronalX/reservoirpy) repository with a simple ESN class that can be easily used for many applications.

[Romain Pastureau](https://github.com/RomainPastureau) (intern in our Mnemosyne team; summer 2016) did great iPython Notebook tutorials:

https://github.com/neuronalX/Reservoir-Jupyter

Click on the "launch Binder" button, and then run either:
- in English: [Minimal ESN - EN.ipynb](https://github.com/RomainPastureau/Reservoir-Jupyter/blob/master/Minimal%20ESN%20-%20EN.ipynb)
- en Français: [Minimal ESN - FR.ipynb](https://github.com/RomainPastureau/Reservoir-Jupyter/blob/master/Minimal%20ESN%20-%20FR.ipynb)

## Corpora
Most copora are available in the folder [/corpora](/corpora).

### 15 languages corpora is available here:
[2019_TCDS_15languages.txt](/corpora/2019_TCDS_15languages.txt)

### Bilingual corpus on English and French obtain by asking 5 users of each language to give command instructions to robots:
These corpora were used in the _CoCo (Cogitive Computation) @ NIPS 2015 workshop_:
- English: [2015_English_5subjects_robot_instructions](/corpora/2015_English_5subjects_robot_instructions.csv)
- French: [2015_French_5subjects_robot_instructions](/corpora/2015_French_5subjects_robot_instructions.csv)

Subjects were asked to provide sentences in English or in French for each of the 38 videos provided. The [videos are available here](/corpora/Hinaut2014_videos/.).

### Older corpora (for PLoS ONE 2013 paper) used with different versions of the model are available here:
- 462 constructions corpus (to test generalization of the model on all possible combinaison of 2 to 6 semantic words):
  - [2013_PLoS_ONE_corpus-462_journal.pone.0052946.s007.txt](/corpora/2013_PLoS_ONE_corpus-462_journal.pone.0052946.s007.txt)
- 90.000 constructions corpus (English plausible sentence)
  - [2013_PLoS_ONE_Corpus_90k.zip](/corpora/2013_PLoS_ONE_Corpus_90k.zip)
- Other downloads for this PLoS ONE 2013 paper:
  - [xavierhinaut.com/downloads](https://sites.google.com/site/xavierhinaut/downloads)

## Source code
### ROS module
(soon here ...)

### PLoS ONE (2013)
[xavierhinaut.com/downloads](https://sites.google.com/site/xavierhinaut/downloads)

### (Other codes available soon ...)

## Videos
- iCub understanding a sentence and performing some actions
http://youtube.com/watch?v=3ZePCuvygi0
- "Humanoidly Speaking": Interaction with Nao (IJCAI 2015 video)
  - https://www.youtube.com/watch?v=FpYDco3ZgkU
  - [Description of the video](https://www.researchgate.net/publication/281590370_Humanoidly_Speaking_-_How_the_Nao_humanoid_robot_can_learn_the_name_of_objects_and_interact_with_them_through_common_speech?ev=prf_ov_fet_res&_iepl%5BviewId%5D=V5HeUWGFjNnWE8Q8ovSIKJ1UEcBXo9F0QThK&_iepl%5Bcontexts%5D%5B0%5D=prfhpi&_iepl%5Bdata%5D%5BstandardItemCount%5D=4&_iepl%5Bdata%5D%5BuserSelectedItemCount%5D=5&_iepl%5Bdata%5D%5BtopHighlightCount%5D=2&_iepl%5Bdata%5D%5BtopHighlightIndex%5D=1&_iepl%5Bdata%5D%5BfeaturedItem1of2%5D=1&_iepl%5BtargetEntityId%5D=PB%3A281590370&_iepl%5BinteractionType%5D=publicationTitle)

## References
More information about the syntax learning model and related papers.
Most recent papers could be seen on my [Research Gate](https://www.researchgate.net/profile/Xavier_Hinaut) or [Google Scholar](https://scholar.google.com/citations?user=pNW4eZAAAAAJ) profiles.

### Hinaut & Dominey (2013) _PLoS ONE_
Most detailed about general model features and background of the approach.
[Paper open access](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0052946)

### Hinaut et al. (2014) _Frontiers in NeuroRobotics_
Implementation of the model in the iCub humanoid robot and data collection with naive users. Presentation of the "reverse" version of the model producing sentences based on meaning representation.
[Paper open access](http://journal.frontiersin.org/article/10.3389/fnbot.2014.00016/full)

### Hinaut et al. (2015) _CoCo (Cognitive Computation) @ NIPS workshop_
Syntax model generalize on English and French at the same time using the same random reservoir (hidden layer).
Model enhanced with the ability to process "unwkown/infrequent words".
[Paper on ResearchGate](https://www.researchgate.net/publication/284691419_A_Recurrent_Neural_Network_for_Multiple_Language_Acquisition_Starting_with_English_and_French)

### Twiefel, Hinaut, Wermter (2016) _RO-MAN_
Integration of the syntax model in an HRI experiment using the Nao humanoid robot
[Paper on ResearchGate](https://www.researchgate.net/publication/303976819_Using_Natural_Language_Feedback_in_a_Neuro-inspired_Integrated_Multimodal_Robotic_Architecture)

### Twiefel et al. (2016) _ESANN_
Adaptation of the syntax model to a crowdsourced (noisy) corpus data of robot arm commands
[Paper on ResearchGate](https://www.researchgate.net/publication/303978525_Semantic_Role_Labelling_for_Robot_Instructions_using_Echo_State_Networks)
