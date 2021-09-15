# deep_unsupervised_learning

Note that this code is pre-dominately based on existing reposities:

For the BigBird Model I use pegasus_evaluation.ipynb which i added in the bin repo and for the counterfactual reasoning i use the official repo: https://github.com/qkaren/unsup_gen_for_cms_reasoning.

# Data

Abductive Reasoning Datasource:
http://abductivecommonsense.xyz

Counterfactual Data: 

https://paperswithcode.com/dataset/timetravel

# Commonsense Reasoning 

Delorean entails code for the two tasks namely abductive reasoning. 
The main delorean decoding notebook can be found in the DeLorean.ipynb file. 
Code can be found in the commonsense folder.

# Results 

I report the ROGUE and BLEURT Scores for the models for the summarization. 
You can find the respective CSV with the results folder for the respective model.

# Text Summarizations

I include a few notebooks i used.
To reproduce, Arxiv one needs to make some changes in the pubmed notebook. 
Instructions are provided in the notebook itself.
All the notesbokes beavily built on the pegasus_evaluation notebook which was published by the authors of bigbord. 
I also link that and many other reference notebooks in the bin folder. 

# Plots 

Code for the plots can be found in the  paper folder

# Bin 

This folder contains all reference notebooks i used.

# Further Direction 

I would love to apply this combined method of bidirectional decoding and long sequence summarization via sparse attention in further research and potentially apply it to a shared task such as laysumm2020.


