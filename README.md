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

Note that there is no offical code for the evaluation and the repo only contains code untill the ranking step. 
This is a reason why there are some difference also with respect to the scaling of the scores. 

|  | ROUGE-L | BertScore | Bleurt |
| :--- | :---: | :---: | :---: |
| TimeTravel |  |  |  |
| Reported DeLorean | 40.73 | 63.36 | - |
| Replicated DeLorean (Non-Deprecated) | 31.19 | 0.886 | -.8552 |
| Art |  |  |  |
| Reported DeLorean | 18.94 | 42.86 | - |
| Replicated DeLorean (Non-Deprecated) | 17.89 | 0.874 | -0.970 |


# Text Summarizations

I report the ROGUE and BLEURT Scores for the models for the summarization. 
You can find the respective CSV with the results folder for the respective model.
When i write down BigBird, i refer to BigBird-Pegasus large of the respective fine tuned checkpoint.
The table reports the F1 measures

|  | ROUGE-1 | ROUGE-2 | ROUGE-L | Bleurt |
| :--- | :---: | :---: | :---: | :---: |
| Pubmed |  |  |  |  |
| Reported BigBird | 46.32 | 20.65 | 42.33 | - |
| Replicated BigBird | 43.94 | 19.60 | 26.90 | -0.448 |
| BigBird + Sampling | 43.93 | 19.62 | 26.91 | -0.159 |
| BigBird + Sampling + Repetition Penalty | 43.94 | 19.55 | 26.82 | -0.161 |
| Arxiv |  |  |  |  |
| Reported BigBird | 46.63 | 19.02 | 41.77 | - |
| Replicated BigBird | 43.50 | 17.74 | 25.77 | -0.4993 |
| BigBird + Sampling | 43.50 | 17.74 | 25.77 | -0.4993 |
| BigBird + Sampling + Repetition Penalty | 43.47 | 17.77 | 25.70 | -0.498 |
| Big Patent |  |  |  |  |
| Reported BigBird | 60.64 | 42.46 | 50.01 | - |
| Replicated BigBird | 37.88 | 15.11 | 26.12 | -0.473 |
| BigBird + Sampling | 37.88 | 15.11 | 26.12 | -0.473 |
| BigBird + Sampling + Repetition Penalty | 37.88 | 15.21 | 26.09 | -0.474 |
| billsum |  |  |  |  |
| BigBird Arxiv | 16.06 | 01.73 | 12.45 | -1.001 |
| BigBird Big Patent | 26.92 | 09.44 | 19.22 | -0.716 |
| BigBird Arxiv + Ngram-Penalty | 22.22 | 03.24 | 13.20 | -0.9698 |
| BigBird Big Patent + Sampling + Repetition Penalty | 26.47 | 09.38 | 18.94 | -0.724 |


I include a few notebooks i used.
To reproduce, Arxiv one needs to make some changes in the pubmed notebook. 
Instructions are provided in the notebook itself.
All the notesbokes heavily built on the pegasus_evaluation notebook which was published by the authors of bigbord. 
I also link that and many other reference notebooks in the bin folder. 

# Plots 

Code for the plots can be found in the  paper folder

# Bin 

This folder contains all reference notebooks i used.

# Further Direction 

I would love to apply this combined method of bidirectional decoding and long sequence summarization via sparse attention in further research and potentially apply it to a shared task such as laysumm2020.


