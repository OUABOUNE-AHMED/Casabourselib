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

def ticker_2_CodeValeur(ticker):
  CodeValeur = {"ADH" : "9000" , "AFM" : "12200" , "AFI" : "11700" , "GAZ" : "7100" , "AGM" : "6700" , "ADI" : "11200" , "ALM" : "6600" , "ARD" : "27" , "ATL" : "10300" , "ATW" : "8200" , "ATH" : "3200" , "NEJ" : "7000" , "BAL" : "3300" , "BOA" : "1100" , "BCP" : "8000" , "BCI" : "5100" , "CRS" : "8900" , "CDM" : "3600" , "CDA" : "3900" , "CIH" : "3100" , "CMA" : "4000" , "CMT" : "11000" , "COL" : "9200" , "CSR" : "4100" , "CTM" : "2200" , "DRI" : "8500" , "DLM" : "10800" , "DHO" : "10900" , "DIS" : "4200" , "DWY" : "9700" , "NKL" : "11300" , "EQD" : "2300" , "FBR" : "9300" , "HPS" : "9600" , "IBC" : "7600" , "IMO" : "12" , "INV" : "9500" , "JET" : "11600" , "LBV" : "11100" , "LHM" : "3800" , "LES" : "4800" , "LYD" : "8600" , "M2M" : "10000" , "MOX" : "7200" , "MAB" : "1600" , "MNG" : "7300" , "MLE" : "2500" , "IAM" : "8001" , "MDP" : "6500" , "MIC" : "10600" , "MUT" : "21" , "NEX" : "7400" , "OUL" : "5200" , "PRO" : "9900" , "REB" : "5300" , "RDS" : "12000" , "RISMA" : "8700" , "S2M" : "11800" , "SAH" : "11400" , "SLF" : "10700" , "SAM" : "6800" , "SMI" : "1500" , "SNA" : "10500" , "SNP" : "9400" , "MSA" : "12300" , "SID" : "1300" , "SOT" : "9800" , "SRM" : "2000" , "SBM" : "10400" , "STR" : "11500" , "TQM" : "11900" , "TIM" : "10100" , "TMA" : "12100" , "UMR" : "7500" , "WAA" : "6400" , "ZDJ" : "5800"}
  return CodeValeur[ticker]

def ignore_weekends(df , from_date, to_date):
  while from_date not in df.index or to_date not in df.index :
    if to_date not in df.index:
          date = datetime.datetime.strptime(to_date, '%d/%m/%Y')
          date += datetime.timedelta(days=1)
          date1 = date.strftime("%d/%m/%Y")
          to_date = date1
    if from_date not in df.index:
          date = datetime.datetime.strptime(from_date, '%d/%m/%Y')
          date += datetime.timedelta(days=1)
          date1 = date.strftime("%d/%m/%Y")
          from_date = date1
  df1 = df[str(from_date) : str(to_date)]
  return df1
        
def get_one_stock_price(ticker_or_isin, from_date, to_date):
  if ticker_or_isin == 'MASI' :
    masi = get_masi('5y')
    df = ignore_weekends(masi , from_date, to_date)
    return df
  elif ticker_or_isin == 'MADEX' :
    madex = get_madex('5y')
    df = ignore_weekends(madex , from_date, to_date)
    return df
  else:
      from_date = from_date[6:]+'-'+from_date[3:5]+'-'+from_date[0:2]
      to_date = to_date[6:]+'-'+to_date[3:5]+'-'+to_date[0:2]
      if 'MA000' not in ticker_or_isin:
        isin = ticker_2_isin(ticker_or_isin)
      else:
        isin = ticker_or_isin
      try :
        url='https://www.leboursier.ma/api?method=getPriceHistory&ISIN='+str(isin)+'&format=json&from='+str(from_date)+'&to='+str(to_date)
        r = requests.get(url)
        data = json.loads(codecs.decode(r.text.encode(), 'utf-8-sig'))
        df = pd.json_normalize(data['result'])
        df = df.set_index('date')
        return df
      except:
        print("le ticker ou bien la date n'est pas ecrit correctement, svp de cosulter la liste des ticker en appellont la fct get_tickers() (sans arguments) ")
  
def get_madex(periode):
  if not sys.warnoptions:
    warnings.simplefilter("ignore")
  from pandas.core.common import SettingWithCopyWarning
  warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)
  # par exemple periode = '1m' , '1y' , '5y'
  url='https://www.leboursier.ma/api?method=getMadexHistory&periode='+str(periode)+'&format=json'
  r = requests.get(url)
  data = json.loads(codecs.decode(r.text.encode(), 'utf-8-sig'))
  df1 = pd.json_normalize(data['result'])
  df = pd.DataFrame(zip(df1.labels[0], df1.prices[0]),columns =['date','value'])
  for i in range(len(df.date)):
    df.date[i]= datetime.datetime.fromtimestamp(df.date[i]).strftime('%d/%m/%Y')
  df = df.set_index('date')
  return df

def get_masi(periode):
  if not sys.warnoptions:
    warnings.simplefilter("ignore")
  from pandas.core.common import SettingWithCopyWarning
  warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)
  # par exemple periode = '1m' , '1y' , '5y'
  url='https://www.leboursier.ma/api?method=getMasiHistory&periode='+str(periode)+'&format=json'
  r = requests.get(url)
  data = json.loads(codecs.decode(r.text.encode(), 'utf-8-sig'))
  df1 = pd.json_normalize(data['result'])
  df = pd.DataFrame(zip(df1.labels[0], df1.prices[0]),columns =['date','value'])
  for i in range(len(df.date)):
    df.date[i]= datetime.datetime.fromtimestamp(df.date[i]).strftime('%d/%m/%Y')
  df = df.set_index('date')
  return df
