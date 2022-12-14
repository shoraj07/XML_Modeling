import xml.etree.ElementTree as ET
import pandas as pd

xmlFile = open('response.xml')
tree = ET.parse(xmlFile)
root = tree.getroot()
# ET.dump(tree)
l1 = []
l2 = []
for x in root.findall('.//'):
    l1.append(x.tag)
    l2.append(x.text)
    # print(x.tag, ': ', x.text)

# print(l1, '\n', l2)
df1 = pd.DataFrame({'Tags': l1,
                    'Data': l2})


# for x in root.findall('./item/'):
#     print(x.tag, ' ', x.text)

# ET.dump(tree)
# ET.register_namespace('f', 'fruit')
# ET.register_namespace('el', 'electronics')
# ET.dump(tree)

# for x in root.findall('.//',):
#     print(x.tag, ' ', x.text)

# for x in root.findall('.//{fruit}name'):
#     print(x.text)

a = root.iterfind(".//{http://schemas.ethicspoint.web/2013/12/6/DataContracts/}Id")
b = root.iterfind(".//{http://schemas.ethicspoint.web/2013/12/6/DataContracts/}Id")
for x, y in zip(a, b):
    print(x.tag, y.text)

# ns = {'f': 'fruit',
#       'el': 'electronics'}
# for x in root.findall('.//el:name', ns):
#     print(x.text)

# a = root.iterfind("./item/{*}name")
# b = root.iterfind("./item/{*}price")
# for x, y in zip(a, b):
#     print(x.text, y.text)