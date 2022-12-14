import xml.etree.ElementTree as ET
import pandas as pd
from tabulate import tabulate

xmlFile = open('response.xml')
tree = ET.parse(xmlFile)
root = tree.getroot()

l1 = []
l2 = []
for x in root.findall('.//'):
    l1.append(x.tag)
    l2.append(x.text)

l3 = []
for x in l1:
    l3.append(x.split('}', 1)[1])

df1 = pd.DataFrame({'Tags': l3,
                    'Data': l2})
print(tabulate(df1, showindex=False, headers=df1.columns))
df1.to_csv('final.csv', index=0)
