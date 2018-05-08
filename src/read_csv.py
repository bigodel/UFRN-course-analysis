import pandas as pd

dis09 = pd.read_csv('res/discentes-2009.csv', sep=';', encoding='utf8')
dis10 = pd.read_csv('res/discentes-2010.csv', sep=';', encoding='utf8')
dis11 = pd.read_csv('res/discentes-2011.csv', sep=';', encoding='utf8')
dis12 = pd.read_csv('res/discentes-2012.csv', sep=';', encoding='utf8')
dis13 = pd.read_csv('res/discentes-2013.csv', sep=';', encoding='utf8')
dis14 = pd.read_csv('res/discentes-2014.csv', sep=';', encoding='utf8')
dis15 = pd.read_csv('res/discentes-2015.csv', sep=';', encoding='utf8')
dis16 = pd.read_csv('res/discentes-2016.csv', sep=';', encoding='utf8')
dis17 = pd.read_csv('res/discentes-2017.csv', sep=';', encoding='utf8')
dis18 = pd.read_csv('res/discentes-2018.csv', sep=';', encoding='utf8')

print(dis09.to_string())
