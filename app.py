from flask import Flask, render_template 
import pandas as pd
import requests
from bs4 import BeautifulSoup 
from io import BytesIO
import base64
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')


app = Flask(__name__) #don't change this code

def scrap(url):
    #This is fuction for scrapping
    url_get = requests.get(url)
    soup = BeautifulSoup(url_get.content,"html.parser")
    table = soup.find("div",{"class":"lister-list"})
    div = table.find_all("div",{"class":"lister-item-content"})
    
    temp = [] #initiating a tuple
    
    for i in div:
        judul_film = i.find('a').get_text() 
    
        #get rating imdb
        rating = i.find('strong').get_text()
        rating = rating.strip()
    
        #mencari meta score imdb
        if(i.find('span',{'class':'metascore'})):
            meta_score = i.find('span',{'class':'metascore'}).get_text()
            meta_score = meta_score.strip()
        else:
            #jika meta score (blank) akan diisi dengan nilai 0
            meta_score='0'
    
        #get total votes
        if(i.find('span',{'name':'nv'})):
            votes = i.find('span',{'name':'nv'}).get_text()
            votes = votes.strip()
        else :
            #jika votes (blank) akan diisi dengan nilai 0
            votes = '0'
        
        temp.append((judul_film,rating,meta_score,votes))
   
        #temp = temp[::-1] #remove the header

    df = pd.DataFrame(temp, columns=('Judul','Rating','Meta_Score','Votes')) #creating the dataframe
        
    #data wranggling -  try to change the data type to right data type
    df['Rating'] = df['Rating'].astype('float64')
    df['Meta_Score'] = df['Meta_Score'].astype('int')
    df['Votes'] = df['Votes'].apply(lambda x: x.replace(',','')) #menghilangkan karakter koma (,)
    df['Votes'] = df['Votes'].astype('int')
    #end of data wranggling
    df_plot = df.set_index('Judul').copy()

    return df_plot

@app.route("/")
def index():
    start_date = '2019-01-01'
    end_date   = '2019-12-31'
    url_1 = f'https://www.imdb.com/search/title/?release_date={start_date},{end_date}'
    df    = scrap(url_1) #insert url here

    #This part for rendering matplotlib
    fig = plt.figure(figsize=(8,10),dpi=300)
    plt.style.use('seaborn')
    #plt.style.use('seaborn-bright')
    #plt.xticks(fontsize=2)
    df.head(7).plot()
    
    #Do not change this part
    plt.savefig('plot1',bbox_inches="tight") 
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())
    result = str(figdata_png)[2:-1]
    #This part for rendering matplotlib

    #this is for rendering the table
    df = df.head(7).to_html(classes=["table table-bordered table-striped table-dark table-condensed"])

    return render_template("index.html", table=df, result=result)


if __name__ == "__main__": 
    app.run()
