import pandas as pd
import os
import urllib3

def index_to_urls(index):
    '''

    :param index: index of NSE
    :return: url for list of index constituents
    '''
    url = {
        "nifty50":'https://www1.nseindia.com/content/indices/ind_nifty50list.csv',
        "niftynext50":'https://www1.nseindia.com/content/indices/ind_niftynext50list.csv',
        "niftymidcap150":'https://www1.nseindia.com/content/indices/ind_niftymidcap150list.csv',
        "niftysmallcap100":'https://www1.nseindia.com/content/indices/ind_niftysmallcap100list.csv'
    }
    return url.get(index)

def find_symbol_name(index):
    '''

    :param index: find symbols for constituent index
    :return: symbols :  list of company symbols
    '''
    data  = pd.read_csv(index_to_urls(index))
    symbols = data[['Symbol','Industry']]
    return symbols






