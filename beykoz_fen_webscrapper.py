from bs4 import BeautifulSoup
import requests
import pandas as pd


URL = "https://www.sorubak.com/teogrobot/mektep/14388/beykoz-fen-lisesi"

new_header = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
header_dict= {"User-Agent":new_header}
data = requests.get(URL, headers=header_dict)

soup = BeautifulSoup(data.content, "html.parser")


beykoz_fen_list = []
beykoz_fen_keys=[]
beykoz_fen_values=[]
for section in soup.find_all("section",attrs={"class":"cmtx_comment_section mt-10 font-15 text-left"}):
    id = section.b.text
    comment = section.p.text
    beykoz_fen_list.append(
        {id:comment}
    )
    beykoz_fen_keys.append(id)
    beykoz_fen_values.append(comment)
    

#for j in beykoz_fen_list:
#    for key, value in j.items():
#         print(key)
#         print(value)  
#         print("\n")
  
# for e in soup.findAll("tr",limit=9):
#     print(e.td.text)  

# for link in soup.find_all("link"):
#    print(link["href"])
    



df = pd.DataFrame()
df["ID"] = beykoz_fen_keys
df["Yorumlar"] = beykoz_fen_values
print(df.head())

df.to_excel(excel_writer="Output.xlsx",header=False,index=False )
    
