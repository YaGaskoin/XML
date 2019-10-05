import xml.etree.ElementTree as ET
import re

file = open("workers.txt","r")
text = file.readlines()

root = ET.Element("root")
sections = ET.Element("Работники")
root.append(sections)
cnt = 0
ln = ""
for line in text:
        cnt+=1
        worker = ET.SubElement(sections,"Работник"+str(cnt))
        ln = line.strip()
        worker.text=ln
file.close()
file = open('workers.xml',"w",encoding="utf_8")
tree = ET.tostring(root,encoding = "unicode")
counter = 0
for symb in range(0,len(tree)):
    symb+=counter
    if tree[symb] == ">" and tree[symb-1] != "\n":
          tmp=""
          tmp = tree[:symb+1] +"\n" +tree[symb+1:]
          tree = tmp
          tmp = ""
          symb+=1
    elif tree[symb] == "<" and tree[symb+1] == "/" and tree[symb-1] != "\n" :
          tmp = ""
          tmp =tree[:symb] +"\n" +tree[symb:]
          tree=tmp
          tmp=""
          counter+=2

file.writelines(tree)
print(tree)
