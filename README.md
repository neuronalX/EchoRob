# EchoRob
Recurrent Neural Network for Syntax Learning with Flexible Representations for Robotic Architectures

## Intro on Reservoir Computing
Reservoir Computing (RC) is a type of Recurrent Neural Network used in this EchoRob project. Namely we use an instance of RC called Echo State Networks (ESN).

[Romain Pastureau](https://github.com/RomainPastureau) (intern in our Mnemosyne team; summer 2016) did great iPython Notebook tutorials:

https://github.com/neuronalX/Reservoir-Jupyter

Click on the "launch Binder" button, and then run either:
- in English: [Minimal ESN - EN.ipynb](https://github.com/RomainPastureau/Reservoir-Jupyter/blob/master/Minimal%20ESN%20-%20EN.ipynb)
- en Français: [Minimal ESN - FR.ipynb](https://github.com/RomainPastureau/Reservoir-Jupyter/blob/master/Minimal%20ESN%20-%20FR.ipynb)

## Corpora
### 15 languages corpora is available here:
[2017_TCDS_15languages.txt](/corpora/2017_TCDS_15languages.txt)

### Older corpora (for PLoS ONE 2013 paper) used with different versions of the model are available here:
[xavierhinaut.com/downloads](http://www.xavierhinaut.com/downloads)

## Source code
### ROS module
(soon here ...)

### PLoS ONE (2013)
[xavierhinaut.com/downloads](http://www.xavierhinaut.com/downloads)

### (Other codes available soon ...)

## Videos
- iCub understanding a sentence and performing some actions
http://youtube.com/watch?v=3ZePCuvygi0
- "Humanoidly Speaking": Interaction with Nao (IJCAI 2015 video)
https://www.youtube.com/watch?v=FpYDco3ZgkU

## References
More information about the syntax learning model and related papers
### Hinaut & Dominey (2013) _PLoS ONE_
Most detailed about general model features and background of the approach.
[Paper open access](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0052946)

### Hinaut et al. (2015) _Frontiers in NeuroRobotics_
Implementation of the model in the iCub humanoid robot and data collection with naive users. Presentation of the "reverse" version of the model producing sentences based on meaning representation.
[Paper open access](http://journal.frontiersin.org/article/10.3389/fnbot.2014.00016/full)

### Hinaut et al. (2015) _CoCo @ NIPS workshop_
Syntax model generalize on English and French at the same time using the same random reservoir (hidden layer).
Model enhanced with the ability to process "unwkown/infrequent words".
[Paper on ResearchGate](https://www.researchgate.net/publication/284691419_A_Recurrent_Neural_Network_for_Multiple_Language_Acquisition_Starting_with_English_and_French)

### Twiefel, Hinaut, Wermter (2016) _RO-MAN_
Integration of the syntax model in an HRI experiment using the Nao humanoid robot
[Paper on ResearchGate](https://www.researchgate.net/publication/303976819_Using_Natural_Language_Feedback_in_a_Neuro-inspired_Integrated_Multimodal_Robotic_Architecture)

### Twiefel et al. (2016) _ESANN_
Adaptation of the syntax model to a crowdsourced (noisy) corpus data of robot arm commands
[Paper on ResearchGate](https://www.researchgate.net/publication/303978525_Semantic_Role_Labelling_for_Robot_Instructions_using_Echo_State_Networks)
