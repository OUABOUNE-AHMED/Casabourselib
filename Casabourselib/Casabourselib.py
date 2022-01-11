import requests 
import pandas as pd   
import codecs
import json
from bs4 import BeautifulSoup
import sys
import warnings
import datetime
import urllib
from ipywidgets import Image
from . import Casabourselib_utility as cblu

def get_tickers():
  data = """[
    {
      "Titre": "Addoha",
      "Ticker": "ADH"
    },
    {
      "Titre": "AFMA",
      "Ticker": "AFM"
    },
    {
      "Titre": "Afric Indus.",
      "Ticker": "AFI"
    },
    {
      "Titre": "Afriquia Gaz",
      "Ticker": "GAZ"
    },
    {
      "Titre": "Agma",
      "Ticker": "AGM"
    },
    {
      "Titre": "Alliances",
      "Ticker": "ADI"
    },
    {
      "Titre": "Aluminium Maroc",
      "Ticker": "ALM"
    },
    {
      "Titre": "Aradei Capital",
      "Ticker": "ARD"
    },
    {
      "Titre": "ATLANTASANAD",
      "Ticker": "ATL"
    },
    {
      "Titre": "AttijariwafaBk",
      "Ticker": "ATW"
    },
    {
      "Titre": "AutoHall",
      "Ticker": "ATH"
    },
    {
      "Titre": "Auto Nejma",
      "Ticker": "NEJ"
    },
    {
      "Titre": "BALIMA",
      "Ticker": "BAL"
    },
    {
      "Titre": "BANK OF AFRICA",
      "Ticker": "BOA"
    },
    {
      "Titre": "BCP",
      "Ticker": "BCP"
    },
    {
      "Titre": "BMCI",
      "Ticker": "BCI"
    },
    {
      "Titre": "Cartier Saada",
      "Ticker": "CRS"
    },
    {
      "Titre": "CDM",
      "Ticker": "CDM"
    },
    {
      "Titre": "Central Danone",
      "Ticker": "CDA"
    },
    {
      "Titre": "CIH",
      "Ticker": "CIH"
    },
    {
      "Titre": "Ciments Maroc",
      "Ticker": "CMA"
    },
    {
      "Titre": "CMT",
      "Ticker": "CMT"
    },
    {
      "Titre": "Colorado",
      "Ticker": "COL"
    },
    {
      "Titre": "COSUMAR",
      "Ticker": "CSR"
    },
    {
      "Titre": "CTM",
      "Ticker": "CTM"
    },
    {
      "Titre": "Dari Couspate",
      "Ticker": "DRI"
    },
    {
      "Titre": "DelattreLev.",
      "Ticker": "DLM"
    },
    {
      "Titre": "DeltaHolding",
      "Ticker": "DHO"
    },
    {
      "Titre": "DiacSalaf",
      "Ticker": "DIS"
    },
    {
      "Titre": "DISWAY",
      "Ticker": "DWY"
    },
    {
      "Titre": "EnnaklN",
      "Ticker": "NKL"
    },
    {
      "Titre": "EQDOM",
      "Ticker": "EQD"
    },
    {
      "Titre": "FENIE BROSSETTE",
      "Ticker": "FBR"
    },
    {
      "Titre": "HPS",
      "Ticker": "HPS"
    },
    {
      "Titre": "IBMaroc.com",
      "Ticker": "IBC"
    },
    {
      "Titre": "Immr Invest Br",
      "Ticker": "IMO"
    },
    {
      "Titre": "INVOLYS",
      "Ticker": "INV"
    },
    {
      "Titre": "Jet Contractors",
      "Ticker": "JET"
    },
    {
      "Titre": "LABEL VIE",
      "Ticker": "LBV"
    },
    {
      "Titre": "Lafarge Holcim",
      "Ticker": "LHM"
    },
    {
      "Titre": "Lesieur Cristal",
      "Ticker": "LES"
    },
    {
      "Titre": "Lydec",
      "Ticker": "LYD"
    },
    {
      "Titre": "M2M Group",
      "Ticker": "M2M"
    },
    {
      "Titre": "Maghreb Oxygene",
      "Ticker": "MOX"
    },
    {
      "Titre": "Maghrebail",
      "Ticker": "MAB"
    },
    {
      "Titre": "Managem",
      "Ticker": "MNG"
    },
    {
      "Titre": "Maroc Leasing",
      "Ticker": "MLE"
    },
    {
      "Titre": "Maroc Telecom",
      "Ticker": "IAM"
    },
    {
      "Titre": "MED PAPER",
      "Ticker": "MDP"
    },
    {
      "Titre": "MICRODATA",
      "Ticker": "MIC"
    },
    {
      "Titre": "MUTANDIS",
      "Ticker": "MUT"
    },
    {
      "Titre": "Nexans Maroc",
      "Ticker": "NEX"
    },
    {
      "Titre": "Oulmes",
      "Ticker": "OUL"
    },
    {
      "Titre": "PROMOPHARM",
      "Ticker": "PRO"
    },
    {
      "Titre": "Rebab Company",
      "Ticker": "REB"
    },
    {
      "Titre": "Res. Dar Saada",
      "Ticker": "RDS"
    },
    {
      "Titre": "Risma",
      "Ticker": "RISMA"
    },
    {
      "Titre": "S2M",
      "Ticker": "S2M"
    },
    {
      "Titre": "Saham Assurance",
      "Ticker": "SAH"
    },
    {
      "Titre": "SALAFIN",
      "Ticker": "SLF"
    },
    {
      "Titre": "SAMIR",
      "Ticker": "SAM"
    },
    {
      "Titre": "SMI",
      "Ticker": "SMI"
    },
    {
      "Titre": "SNEP",
      "Ticker": "SNA"
    },
    {
      "Titre": "REALISATIONS MECANIQUES",
      "Ticker": "SNP"
    },
    {
      "Titre": "SODEP-MarsaMaroc",
      "Ticker": "MSA"
    },
    {
      "Titre": "Sonasid",
      "Ticker": "SID"
    },
    {
      "Titre": "SOTHEMA",
      "Ticker": "SOT"
    },
    {
      "Titre": "Ste Boissons Maroc",
      "Ticker": "SRM"
    },
    {
      "Titre": "Stokvis Nord Afr.",
      "Ticker": "SBM"
    },
    {
      "Titre": "STROC Indus.",
      "Ticker": "STR"
    },
    {
      "Titre": "TAQA Morocco",
      "Ticker": "TQM"
    },
    {
      "Titre": "Timar",
      "Ticker": "TIM"
    },
    {
      "Titre": "TotalMaroc",
      "Ticker": "TMA"
    },
    {
      "Titre": "Unimer",
      "Ticker": "UMR"
    },
    {
      "Titre": "WAFA ASSURANCE",
      "Ticker": "WAA"
    },
    {
      "Titre": "Zellidja",
      "Ticker": "ZDJ"
    }
  ]"""
  df = pd.read_json(data)
  pd.set_option('display.max_rows', 76)
  return df

def ticker_2_isin(ticker_or_isin):
  data =  { "ADH": "MA0000011512", "AFM": "MA0000012296", "AFI": "MA0000012114", "GAZ": "MA0000010951", "AGM": "MA0000010944", "ADI": "MA0000011819", "ALM": "MA0000010936",
    "ARD": "MA0000012460", "ATL": "MA0000011710", "ATW": "MA0000012445", "ATH": "MA0000010969", "NEJ": "MA0000011009", "BAL": "MA0000011991", "BOA": "MA0000012437",
    "BCP": "MA0000011884", "BCI": "MA0000010811", "CRS": "MA0000011868", "CDM": "MA0000010381", "CDA": "MA0000012049", "CIH": "MA0000011454", "CMA": "MA0000010506",
    "CMT": "MA0000011793", "COL": "MA0000011934", "CSR": "MA0000012247", "CTM": "MA0000010340", "DRI": "MA0000011421", "DLM": "MA0000011777", "DHO": "MA0000011850",
    "DIS": "MA0000010639", "DWY": "MA0000011637", "NKL": "MA0000011942", "EQD": "MA0000010357", "FBR": "MA0000011587", "HPS": "MA0000011611", "IBC": "MA0000011132",
    "IMO": "MA0000012387", "INV": 
    "MA0000011579", "JET": "MA0000012080", "LBV": "MA0000011801", "LHM": "MA0000012320", "LES": "MA0000012031", "LYD": "MA0000011439",
    "M2M": "MA0000011678", "MOX": "MA0000010985", "MAB": "MA0000011215", "MNG": "MA0000011058", "MLE": "MA0000010035", "IAM": "MA0000011488", "MDP": "MA0000011447",
    "MIC": "MA0000012163", "MUT": "MA0000012395", "NEX": "MA0000011140", "OUL": "MA0000010415", "PRO": "MA0000011660", "REB": "MA0000010993", "RDS": "MA0000012239",
    "RISMA": "MA0000011462", "S2M": "MA0000012106", "SAH": "MA0000012007", "SLF": "MA0000011744", "SAM": "MA0000010803", "SMI": "MA0000010068", "SNA": "MA0000011843",
    "SNP": "MA0000011728", "MSA": "MA0000012312", "SID": "MA0000010019", "SOT": "MA0000012502", "SRM": "MA0000011595", "SBM": "MA0000010365", "STR": "MA0000012056",
    "TQM": "MA0000012205", "TIM": "MA0000011686", "TMA": "MA0000012262", "UMR": "MA0000012023", "WAA": "MA0000010928", "ZDJ": "MA0000010571"  }
  if 'MA000' in ticker_or_isin:
    return list(data.keys())[list(data.values()).index(ticker_or_isin)]
  else:
    return data[ticker_or_isin]

def get_price(tickers_list, from_date, to_date):
    data=[]
    if type(tickers_list) == type(data):
        for ticker in tickers_list:
          temp = cblu.get_one_stock_price(ticker, from_date , to_date)
          row = temp["value"]
          data.append(row)
        data=pd.concat(data,axis=1,sort="False").reindex(data[0].index)
        data.columns = tickers_list
        return data
    else:
        df1 = cblu.get_one_stock_price(tickers_list, from_date, to_date)
        return df1

def get_indicators(ticker):
  url = "https://www.casablanca-bourse.com/bourseweb/Societe-Cote.aspx?codeValeur="+str(cblu.ticker_2_CodeValeur(ticker))+"&cat=7"
  req = requests.get(url)
  soup = BeautifulSoup(req.text, "html.parser")
  view_state = soup.find("input", {"id": "__VIEWSTATE"})['value']
  view_state_generator = soup.find("input", {"id": "__VIEWSTATEGENERATOR"})['value']

  payload = {
    'TopControl1$ScriptManager1': 'SocieteCotee1$UpdatePanel1|SocieteCotee1$LBFicheTech',
    '__EVENTTARGET': 'SocieteCotee1$LBFicheTech',
    '__EVENTARGUMENT': '',
    '__LASTFOCUS': '',
    '__VIEWSTATE': view_state,
    '__VIEWSTATEGENERATOR': view_state_generator,
  }

  r = requests.post(url, data=payload)
  soup = BeautifulSoup(r.text, 'html.parser')
  soup
  result = []
  for i in range(3, 7):
      table_id = 'table'+str(i)
      result.append(soup.find('table', {'id': table_id}))

  df = pd.read_html(str(result[3]), decimal=',', thousands='.')[0]
  df
  df = df.drop('Unnamed: 0', axis=1)
  df = df.drop('Chiffres clés (1)', axis=1)
  df = df.drop(7, axis=0)
  df = df.rename(columns={'Chiffres clés (1).1': 'Chiffres'})
  df = df.drop(8, axis=0)
  df = pd.DataFrame(df).set_index('Chiffres')

  return df

def get_dividends(ticker):
  ticker_2_CodeValeur = {"ADH" : "9000" , "AFM" : "12200" , "AFI" : "11700" , "GAZ" : "7100" , "AGM" : "6700" , "ADI" : "11200" , "ALM" : "6600" , "ARD" : "27" , "ATL" : "10300" , "ATW" : "8200" , "ATH" : "3200" , "NEJ" : "7000" , "BAL" : "3300" , "BOA" : "1100" , "BCP" : "8000" , "BCI" : "5100" , "CRS" : "8900" , "CDM" : "3600" , "CDA" : "3900" , "CIH" : "3100" , "CMA" : "4000" , "CMT" : "11000" , "COL" : "9200" , "CSR" : "4100" , "CTM" : "2200" , "DRI" : "8500" , "DLM" : "10800" , "DHO" : "10900" , "DIS" : "4200" , "DWY" : "9700" , "NKL" : "11300" , "EQD" : "2300" , "FBR" : "9300" , "HPS" : "9600" , "IBC" : "7600" , "IMO" : "12" , "INV" : "9500" , "JET" : "11600" , "LBV" : "11100" , "LHM" : "3800" , "LES" : "4800" , "LYD" : "8600" , "M2M" : "10000" , "MOX" : "7200" , "MAB" : "1600" , "MNG" : "7300" , "MLE" : "2500" , "IAM" : "8001" , "MDP" : "6500" , "MIC" : "10600" , "MUT" : "21" , "NEX" : "7400" , "OUL" : "5200" , "PRO" : "9900" , "REB" : "5300" , "RDS" : "12000" , "RISMA" : "8700" , "S2M" : "11800" , "SAH" : "11400" , "SLF" : "10700" , "SAM" : "6800" , "SMI" : "1500" , "SNA" : "10500" , "SNP" : "9400" , "MSA" : "12300" , "SID" : "1300" , "SOT" : "9800" , "SRM" : "2000" , "SBM" : "10400" , "STR" : "11500" , "TQM" : "11900" , "TIM" : "10100" , "TMA" : "12100" , "UMR" : "7500" , "WAA" : "6400" , "ZDJ" : "5800"}
  url = "https://www.casablanca-bourse.com/bourseweb/Societe-Cote.aspx?codeValeur="+str(ticker_2_CodeValeur[ticker])+"&cat=7"
  req = requests.get(url)

  soup = BeautifulSoup(req.text, "html.parser")

  view_state = soup.find("input", {"id": "__VIEWSTATE"})['value']
  view_state_generator = soup.find("input", {"id": "__VIEWSTATEGENERATOR"})['value']

  payload = {
    'TopControl1$ScriptManager1': 'SocieteCotee1$UpdatePanel1|SocieteCotee1$LBFicheTech',
    '__EVENTTARGET': 'SocieteCotee1$LBDividende',
    '__EVENTARGUMENT': '',
    '__LASTFOCUS': '',
    '__VIEWSTATE': view_state,
    '__VIEWSTATEGENERATOR': view_state_generator,
  }

  r = requests.post(url, data=payload)
  soup = BeautifulSoup(r.text, 'html.parser')
  divs = soup.find_all('div')
  df = pd.read_html(str(divs[242]), decimal=',', thousands='.')[6]
  df = df.set_index('Année')
  df = df.drop('Unnamed: 0', axis= 1 )
  return df

def get_stock_logo(ticker):                                                             
  url = "https://www.casablanca-bourse.com/bourseweb/Societe-Cote.aspx?codeValeur="+str(cblu.ticker_2_CodeValeur(ticker))+"&cat=7"
  req = requests.get(url)
  soup = BeautifulSoup(req.text, "html.parser")
  logo_path = soup.find("input", {"id": "SocieteCotee1_imgLogo"})['src']
  logo_url = 'https://www.casablanca-bourse.com/bourseweb/' + logo_path
  return Image(value=requests.get(logo_url).content)

def get_masi_data():
  url='https://www.casablanca-bourse.com/bourseweb/indice-ponderation.aspx?Cat=22&IdLink=298'
  html = urllib.request.urlopen(url).read()

  soup = BeautifulSoup(html,'lxml')
  table = soup.find('table')

  row=list()
  i=0
  table_rows = table.find_all('tr')
  for tr in table_rows:
    td = tr.find_all('td')
    row.append([i.text for i in td])

  df = pd.DataFrame( columns = row[358] )  

  data=list()
  x=0
  for i in range(360,434):
      df = df.append(pd.Series(row[i], index=row[358]), ignore_index=True)
    #df = df.append(pd.Series(['d', 'e'], index=['col1','col2']), ignore_index=True) 

    #data.append(row[i])
    #df.loc[x]=row[i]


  #df = df.append(pd.Series(row[433], index=row[358]), ignore_index=True)
  df = df.append(pd.Series(['',
 '',
 '',
 'Total',
 '',
 row[434][5],
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 row[434][13],
 '',
 '',
 ''], index=row[358]), ignore_index=True) 


  #cleaning of data row1
  df_Instrument= df['Instrument'].str.split('\n\n')
  df_name=list()
  for i in range(74):
      #df.Instrument.iloc[i]=df_Instrument[i][1]
      df_name.append(df_Instrument[i][1])
  df_name.append("Total")    
  df.Instrument=df_name
  #cleaning of data row2
  df_name=list()
  for i in range(75):
      df_titres=df['Nombre de titres'][i].split('Â\xa0')
      df_name.append(' '.join(df_titres))
   
  #x=[df['Nombre de titres'][38].split('Â\xa0')[0].replace("\xa0", " "),df['Nombre de titres'][38].split('Â\xa0')[1],df['Nombre de titres'][38].split('Â\xa0')[2],df['Nombre de titres'][38].split('Â\xa0')[3]]

  #df_name.append(' '.join(x))
  df["Nombre de titres"]=df_name

  #cleaning of data row3
  df_name=list()
  for i in range(74):
      df_titres=df.Cours[i].split('Â\xa0')
      df_name.append(''.join(df_titres))
  df_name.append('')
  df.Cours=df_name

  #cleaning of data row4

  df_name=list()
  df.columns = df.columns.str.strip()
  for i in range(75):
      df_titres=df['Capitalisation flottante'][i].split('Â\xa0')
      df_name.append(' '.join(df_titres))
    
  df['Capitalisation flottante']=df_name 
    
  return df
  
def get_madex_data():
    
    url = "https://www.casablanca-bourse.com/bourseweb/indice-ponderation.aspx?Cat=22&IdLink=298"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    view_state = soup.find("input", {"id": "__VIEWSTATE"})['value']
    view_state_generator = soup.find("input", {"id": "__VIEWSTATEGENERATOR"})['value']
    payload = {
  'TopControl1$ScriptManager1': 'Ponderation1$UpdatePanel1|Ponderation1$ImageButton1',
  '__EVENTTARGET': '',
  '__EVENTARGUMENT': '',
  '__LASTFOCUS': '',
  '__VIEWSTATE': view_state,
  '__VIEWSTATEGENERATOR': view_state_generator,
  'TopControl1$TxtRecherche' : '',
  'TopControl1$txtValeur' : '',
  'Ponderation1$Marche' : 'RBMadex',
  'Ponderation1$DateTimeControl1$TBCalendar' : '04/11/2021',
  'Ponderation1$DateTimeControl2$TBCalendar' : '',
  'Ponderation1$DateTimeControl3$TBCalendar' : '',
  'hiddenInputToUpdateATBuffer_CommonToolkitScripts' : '1',
  '__AjaxControlToolkitCalendarCssLoaded' : '',
  'Ponderation1$ImageButton1.x' : '3',
  'Ponderation1$ImageButton1.y' : '17',
}
    r = requests.post(url, data=payload)
    soup = BeautifulSoup(r.text, 'html.parser')
    table = soup.find_all('table')
    

    #constuction de nested list pour le sin 
    result =list()
    for i in range(1, 10):
        table_id = 'Ponderation1_RPTLPonderation_ctl0'+str(i)+'_LBCIsin'
        id_= 'Ponderation1_RPTLPonderation_ctl0'+str(i)+'_LBCIsin1'
        if soup.find('span', attrs={'id': table_id})!= None:
            result.append([soup.find('span', attrs={'id': table_id})])
        else:
            result.append([soup.find('span', attrs={'id': id_})])

    for i in range(10, 56):
        table_id = 'Ponderation1_RPTLPonderation_ctl'+str(i)+'_LBCIsin'
        id_= 'Ponderation1_RPTLPonderation_ctl'+str(i)+'_LBCIsin1'
        if soup.find('span', attrs={'id': table_id})!= None:
            result.append([soup.find('span', attrs={'id': table_id})])
        else:
            result.append([soup.find('span', attrs={'id': id_})])

    #l'ajoutement des libelles pour chaque sin                        
    x=0
    for i in range(1, 10):
        table_id = 'Ponderation1_RPTLPonderation_ctl0'+str(i)+'_LBLibelle'
        id_= 'Ponderation1_RPTLPonderation_ctl0'+str(i)+'_LBLibelle1'
        if soup.find('span', attrs={'id': table_id})!= None:
            result[x].append(soup.find('span', attrs={'id': table_id}))  
            x=x+1
        else:
            result[x].append(soup.find('span', attrs={'id': id_}))
            x=x+1

    for i in range(10, 56):
        table_id = 'Ponderation1_RPTLPonderation_ctl'+str(i)+'_LBLibelle'
        id_= 'Ponderation1_RPTLPonderation_ctl'+str(i)+'_LBLibelle1'
        if soup.find('span', attrs={'id': table_id})!= None:
            result[x].append(soup.find('span', attrs={'id': table_id}))
            x=x+1
        else:
            result[x].append(soup.find('span', attrs={'id': id_}))
            x=x+1

    #l'ajoutement des titres
    x=0
    for i in range(1, 10):
        table_id = 'Ponderation1_RPTLPonderation_ctl0'+str(i)+'_LBNbreTitre'
        id_= 'Ponderation1_RPTLPonderation_ctl0'+str(i)+'_LBNbreTitre1'
        if soup.find('span', attrs={'id': table_id})!= None:
            result[x].append(soup.find('span', attrs={'id': table_id}))  
            x=x+1
        else:
            result[x].append(soup.find('span', attrs={'id': id_}))
            x=x+1

    for i in range(10, 56):
        table_id = 'Ponderation1_RPTLPonderation_ctl'+str(i)+'_LBNbreTitre'
        id_= 'Ponderation1_RPTLPonderation_ctl'+str(i)+'_LBNbreTitre1'
        if soup.find('span', attrs={'id': table_id})!= None:
            result[x].append(soup.find('span', attrs={'id': table_id}))
            x=x+1
        else:
            result[x].append(soup.find('span', attrs={'id': id_}))
            x=x+1
    #l'ajoutement des Cours
    x=0
    for i in range(1, 10):
        table_id = 'Ponderation1_RPTLPonderation_ctl0'+str(i)+'_LBCours'
        id_= 'Ponderation1_RPTLPonderation_ctl0'+str(i)+'_LBCours1'
        if soup.find('span', attrs={'id': table_id})!= None:
            result[x].append(soup.find('span', attrs={'id': table_id}))  
            x=x+1
        else:
            result[x].append(soup.find('span', attrs={'id': id_}))
            x=x+1

    for i in range(10, 56):
        table_id = 'Ponderation1_RPTLPonderation_ctl'+str(i)+'_LBCours'
        id_= 'Ponderation1_RPTLPonderation_ctl'+str(i)+'_LBCours1'
        if soup.find('span', attrs={'id': table_id})!= None:
            result[x].append(soup.find('span', attrs={'id': table_id}))
            x=x+1
        else:
            result[x].append(soup.find('span', attrs={'id': id_}))
            x=x+1

    #l'ajoutement de facteur flottant
    x=0
    for i in range(1, 10):
        table_id = 'Ponderation1_RPTLPonderation_ctl0'+str(i)+'_LBFactFlot'
        id_= 'Ponderation1_RPTLPonderation_ctl0'+str(i)+'_LBFactFlot1'
        if soup.find('span', attrs={'id': table_id})!= None:
            result[x].append(soup.find('span', attrs={'id': table_id}))  
            x=x+1
        else:
            result[x].append(soup.find('span', attrs={'id': id_}))
            x=x+1

    for i in range(10, 56):
        table_id = 'Ponderation1_RPTLPonderation_ctl'+str(i)+'_LBFactFlot'
        id_= 'Ponderation1_RPTLPonderation_ctl'+str(i)+'_LBFactFlot1'
        if soup.find('span', attrs={'id': table_id})!= None:
            result[x].append(soup.find('span', attrs={'id': table_id}))
            x=x+1
        else:
            result[x].append(soup.find('span', attrs={'id': id_}))
            x=x+1

    #l'ajoutement de Facteur de plafonnement
    x=0
    for i in range(1, 10):
        table_id = 'Ponderation1_RPTLPonderation_ctl0'+str(i)+'_LBFactPlaf'
        id_= 'Ponderation1_RPTLPonderation_ctl0'+str(i)+'_LBFactPlaf1'
        if soup.find('span', attrs={'id': table_id})!= None:
            result[x].append(soup.find('span', attrs={'id': table_id}))  
            x=x+1
        else:
            result[x].append(soup.find('span', attrs={'id': id_}))
            x=x+1

    for i in range(10, 56):
        table_id = 'Ponderation1_RPTLPonderation_ctl'+str(i)+'_LBFactPlaf'
        id_= 'Ponderation1_RPTLPonderation_ctl'+str(i)+'_LBFactPlaf1'
        if soup.find('span', attrs={'id': table_id})!= None:
            result[x].append(soup.find('span', attrs={'id': table_id}))
            x=x+1
        else:
            result[x].append(soup.find('span', attrs={'id': id_}))
            x=x+1

    #l'ajoutement de Capitalisation flottante
    x=0
    for i in range(1, 10):
        table_id = 'Ponderation1_RPTLPonderation_ctl0'+str(i)+'_LBCapitFlot'
        id_= 'Ponderation1_RPTLPonderation_ctl0'+str(i)+'_LBCapitFlot1'
        if soup.find('span', attrs={'id': table_id})!= None:
            result[x].append(soup.find('span', attrs={'id': table_id}))  
            x=x+1
        else:
            result[x].append(soup.find('span', attrs={'id': id_}))
            x=x+1

    for i in range(10, 56):
        table_id = 'Ponderation1_RPTLPonderation_ctl'+str(i)+'_LBCapitFlot'
        id_= 'Ponderation1_RPTLPonderation_ctl'+str(i)+'_LBCapitFlot1'
        if soup.find('span', attrs={'id': table_id})!= None:
            result[x].append(soup.find('span', attrs={'id': table_id}))
            x=x+1
        else:
            result[x].append(soup.find('span', attrs={'id': id_}))
            x=x+1

    #l'ajoutement des Poids
    x=0
    for i in range(1, 10):
        table_id = 'Ponderation1_RPTLPonderation_ctl0'+str(i)+'_LBPoids'
        id_= 'Ponderation1_RPTLPonderation_ctl0'+str(i)+'_LBPoids1'
        if soup.find('span', attrs={'id': table_id})!= None:
            result[x].append(soup.find('span', attrs={'id': table_id}))  
            x=x+1
        else:
            result[x].append(soup.find('span', attrs={'id': id_}))
            x=x+1

    for i in range(10, 56):
        table_id = 'Ponderation1_RPTLPonderation_ctl'+str(i)+'_LBPoids'
        id_= 'Ponderation1_RPTLPonderation_ctl'+str(i)+'_LBPoids1'
        if soup.find('span', attrs={'id': table_id})!= None:
            result[x].append(soup.find('span', attrs={'id': table_id}))
            x=x+1
        else:
            result[x].append(soup.find('span', attrs={'id': id_}))
            x=x+1


    code=list()       
    for span in result:
        #print(span[1].text)
        code.append([span[0].text,span[1].text,span[2].text,span[3].text,span[4].text,span[5].text,span[6].text,span[7].text]) 

    #x = soup.find('span', attrs={'id': 'Ponderation1_RPTLPonderation_ctl56_LBTotalTitre'})      
    code.append([" ","Total ",soup.find('span', attrs={'id': 'Ponderation1_RPTLPonderation_ctl56_LBTotalTitre'}).text," "," "," ",soup.find('span', attrs={'id':"Ponderation1_RPTLPonderation_ctl56_LBTotalCapitalisation"}).text," "])        
    columns_=['Code Isin','Instrument','Nombre de titres','Cours','Facteur flottant','Facteur de plafonnement','Capitalisation flottante','Poids']    

    df = pd.DataFrame( columns = columns_ )  

    for i in range(len(code)):
        df = df.append(pd.Series(code[i], index=columns_), ignore_index=True)
    #soup.find('span', attrs={'id': 'Ponderation1_RPTLPonderation_ctl56_LBTotalTitre'}).text

    return df
    


 