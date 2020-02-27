#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 09:48:34 2020

@author: todayfirst
"""

import pandas as pd

class peak_cut:
    def read_data(self, path, date, ess):
        self.ess = ess
        self.need_watt = pd.read_csv(path)
        self.need_watt = self.need_watt[56 * (date-1) : 56 * (date) ]
        self.left = 1000000000
        self.right = 0
        
        for each in self.need_watt:
            if each > self.right:
                self.right = each
            if each < self.left:
                self.left = each
        
    def check(self, val):
        surplus = 0
        ess_vol = self.ess.cap
        each = 0
        while each < len(self.need_watt):
            
            if self.need_watt[each]>val: 
                ess_vol = ess_vol - self.need_watt[each]
                if ess_vol <0 :
                    return False
                find_plus = each+1
                for_cut = 0
                while find_plus<len(self.need_watt):
                    if self.need_watt[find_plus]>val:
                        for_cut = val - self.need_watt[find_plus]
                        break
                    else:
                        find_plus = find_plus + 1
            

