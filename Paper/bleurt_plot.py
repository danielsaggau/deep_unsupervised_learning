import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv("/Users/danielsaggau/Downloads/billsum_bleurt_score_beam.csv")
data = pd.read_json("/Users/danielsaggau/Downloads/anlg/test-w-comet-preds.jsonl")
data = pd.DataFrame(data)


with open('/Users/danielsaggau/Downloads/anlg/test-w-comet-preds.jsonl', 'r') as json_file:
    json_list = list(json_file)

for json_str in json_list:
    result = json.loads(json_str)
    print(f"result: {result}")
    print(isinstance(result, dict))

with open('small_data_2.json', 'w') as fp:
    json.dump(result, fp)


plt.axvline(data['scores'][1:600].mean(), color='k', linestyle='dashed', linewidth=1)
quant = np.quantile(data['scores'], [0.05, 0.5, 0.95])

plt.hist(data['scores'], color = 'xkcd:azure')
plt.title('BLEURT score Distribution', fontdict=dict(size=14))
plt.gca().set(ylabel='BILLSUM Document Count', xlabel='Score')
plt.axvline(quant[0], linestyle='dashed', linewidth=1)
plt.axvline(quant[1], linestyle='dashed', linewidth=1)
plt.axvline(quant[2], linestyle='dashed', linewidth=1)
plt.show()

#Arxiv

data = pd.read_csv("/Users/danielsaggau/Downloads/arxiv_bleurt_result.csv")
quant = np.quantile(data['scores'], [0.05, 0.5, 0.95])
plt.hist(data['scores'], color = 'xkcd:azure')
plt.title('BLEURT score Distribution', fontdict=dict(size=14))
plt.gca().set(ylabel='ARXIV Document Count', xlabel='Score')
plt.axvline(quant[0], linestyle='dashed', linewidth=1)
plt.axvline(quant[1], linestyle='dashed', linewidth=1)
plt.axvline(quant[2], linestyle='dashed', linewidth=1)
plt.show()

data = pd.read_csv("/Users/danielsaggau/Downloads/arxiv_bleurt_score_beam.csv")
quant = np.quantile(data['scores'], [0.05, 0.5, 0.95])
plt.hist(data['scores'], color = 'xkcd:azure')
plt.title('BLEURT score Distribution', fontdict=dict(size=14))
plt.gca().set(ylabel='ARXIV Document Count', xlabel='Score')
plt.axvline(quant[0], linestyle='dashed', linewidth=1)
plt.axvline(quant[1], linestyle='dashed', linewidth=1)
plt.axvline(quant[2], linestyle='dashed', linewidth=1)
plt.show()

data = pd.read_csv("/Users/danielsaggau/Downloads/arxiv_bleurt_score_nopen.csv")
quant = np.quantile(data['scores'], [0.05, 0.5, 0.95])
plt.hist(data['scores'], color = 'xkcd:azure')
plt.title('BLEURT score Distribution', fontdict=dict(size=14))
plt.gca().set(ylabel='ARXIV Document Count', xlabel='Score')
plt.axvline(quant[0], linestyle='dashed', linewidth=1)
plt.axvline(quant[1], linestyle='dashed', linewidth=1)
plt.axvline(quant[2], linestyle='dashed', linewidth=1)
plt.show()

# BIGPATENT

data = pd.read_csv("/Users/danielsaggau/Downloads/bigpatent_bleurt_result.csv")
quant = np.quantile(data['scores'], [0.05, 0.5, 0.95])
plt.hist(data['scores'], color = 'xkcd:azure')
plt.title('BLEURT score Distribution', fontdict=dict(size=14))
plt.gca().set(ylabel='bigpatent Document Count', xlabel='Score')
plt.axvline(quant[0], linestyle='dashed', linewidth=1)
plt.axvline(quant[1], linestyle='dashed', linewidth=1)
plt.axvline(quant[2], linestyle='dashed', linewidth=1)
plt.show()

data = pd.read_csv("/Users/danielsaggau/Downloads/bigpatent_bleurt_result.csv")
quant = np.quantile(data['scores'], [0.05, 0.5, 0.95])
plt.hist(data['scores'], color = 'xkcd:azure')
plt.title('BLEURT score Distribution', fontdict=dict(size=14))
plt.gca().set(ylabel='bigpatent Document Count', xlabel='Score')
plt.axvline(quant[0], linestyle='dashed', linewidth=1)
plt.axvline(quant[1], linestyle='dashed', linewidth=1)
plt.axvline(quant[2], linestyle='dashed', linewidth=1)
plt.show()

data = pd.read_csv("/Users/danielsaggau/Downloads/bigpatent_beam_bleurt_score.csv")
quant = np.quantile(data['scores'], [0.05, 0.5, 0.95])
plt.hist(data['scores'], color = 'xkcd:azure')
plt.title('BLEURT score Distribution', fontdict=dict(size=14))
plt.gca().set(ylabel='bigpatent Document Count', xlabel='Score')
plt.axvline(quant[0], linestyle='dashed', linewidth=1)
plt.axvline(quant[1], linestyle='dashed', linewidth=1)
plt.axvline(quant[2], linestyle='dashed', linewidth=1)
plt.show()


data = pd.read_csv("/Users/danielsaggau/Downloads/bigpatent_nopen_bleurt_scor.csv")
quant = np.quantile(data['scores'], [0.05, 0.5, 0.95])
plt.hist(data['scores'], color = 'xkcd:azure')
plt.title('BLEURT score Distribution', fontdict=dict(size=14))
plt.gca().set(ylabel='Bigpatent Document Count', xlabel='Score')
plt.axvline(quant[0], linestyle='dashed', linewidth=1)
plt.axvline(quant[1], linestyle='dashed', linewidth=1)
plt.axvline(quant[2], linestyle='dashed', linewidth=1)
plt.show()

# BILLSUM

data = pd.read_csv("/Users/danielsaggau/Downloads/billsum_bleurt_score_beam.csv")
quant = np.quantile(data['scores'], [0.05, 0.5, 0.95])
plt.hist(data['scores'], color = 'xkcd:azure')
plt.title('Billsum score Distribution', fontdict=dict(size=14))
plt.gca().set(ylabel='Billsum Document Count', xlabel='Score')
plt.axvline(quant[0], linestyle='dashed', linewidth=1)
plt.axvline(quant[1], linestyle='dashed', linewidth=1)
plt.axvline(quant[2], linestyle='dashed', linewidth=1)
plt.show()



data = pd.read_csv("/Users/danielsaggau/Downloads/billsum_bleurt_score_beam_bigpatent.csv")
quant = np.quantile(data['scores'], [0.05, 0.5, 0.95])
plt.hist(data['scores'], color = 'xkcd:azure')
plt.title('Billsum score Distribution', fontdict=dict(size=14))
plt.gca().set(ylabel='Billsum Document Count', xlabel='Score')
plt.axvline(quant[0], linestyle='dashed', linewidth=1)
plt.axvline(quant[1], linestyle='dashed', linewidth=1)
plt.axvline(quant[2], linestyle='dashed', linewidth=1)
plt.show()


data = pd.read_csv("/Users/danielsaggau/Downloads/billsum_bleurt_score_all_bigpatent.csv")
quant = np.quantile(data['scores'], [0.05, 0.5, 0.95])
plt.hist(data['scores'], color = 'xkcd:azure')
plt.title('Billsum score Distribution', fontdict=dict(size=14))
plt.gca().set(ylabel='Billsum Document Count', xlabel='Score')
plt.axvline(quant[0], linestyle='dashed', linewidth=1)
plt.axvline(quant[1], linestyle='dashed', linewidth=1)
plt.axvline(quant[2], linestyle='dashed', linewidth=1)
plt.show()

#pubmed

data = pd.read_csv("/Users/danielsaggau/Downloads/bleurt_modified.csv")
quant = np.quantile(data['scores'], [0.05, 0.5, 0.95])
plt.hist(data['scores'], color = 'xkcd:azure')
plt.title('Pubmed score Distribution', fontdict=dict(size=14))
plt.gca().set(ylabel='Pubmed Document Count', xlabel='Score')
plt.axvline(quant[0], linestyle='dashed', linewidth=1)
plt.axvline(quant[1], linestyle='dashed', linewidth=1)
plt.axvline(quant[2], linestyle='dashed', linewidth=1)
plt.show()


data = pd.read_csv("/Users/danielsaggau/Downloads/bleurt_modified_pen.csv")
quant = np.quantile(data['scores'], [0.05, 0.5, 0.95])
plt.hist(data['scores'], color = 'xkcd:azure')
plt.title('Pubmed score Distribution', fontdict=dict(size=14))
plt.gca().set(ylabel='Pubmed Document Count', xlabel='Score')
plt.axvline(quant[0], linestyle='dashed', linewidth=1)
plt.axvline(quant[1], linestyle='dashed', linewidth=1)
plt.axvline(quant[2], linestyle='dashed', linewidth=1)
plt.show()