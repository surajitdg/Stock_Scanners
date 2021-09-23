import pandas as pd
import numpy as np
import nsepy as nse
import datetime as dt
from find_symbols import find_symbol_name

class SimpleRecommender():

    def __init__(self,category,equity_class,sector):
        '''
        :param category: nifty50,niftynext50,niftymidcap100
        :param equity_class: EQ-equity,FUT -futures, OPT -options
        :param sector: sector - None,IT,METAL,AUTO etc.
        '''
        self.category = category
        self.equity_class = equity_class
        self.sector = sector
        self.companies = find_symbol_name(category)
        if self.sector is not None:
            self.companies = self.companies[['Industry'] == self.sector]

    def calculate_ma(self,price_list,type_ma):
        '''

        :param price_list: price list of the symbol
        :param type_ma: type of moving average, simple,degree average,exponential
        :return: return moving average of the price list
        '''
        if (type_ma == "simple"):
            return (price_list.sum()/price_list.count())
        elif (type_ma == "exp"):
            ema = 0
            #Not Yet implemented
            return ema



    def less_than_dma(self,days):
        '''

        :param days: Check Moving average(MA) crossover for the no of days like 50,100,200
        :return: list of stocks less than MA
        '''

        



