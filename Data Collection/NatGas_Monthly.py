#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 06:19:29 2020

@author: Antonio Hickey
"""
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import pandas as pd
import csv
#############################################################################
###### Data Mining
url =  'https://www.eia.gov/dnav/ng/ng_sum_lsum_dcu_nus_m.htm'
uClient = uReq(url)
page_soup = soup(uClient.read(), "html.parser")
uClient.close()

test = page_soup.findAll("td", {"class": "DataB"})
###########################################################################
####################### *****Data Cleaning***** #############################
######### Prices

### Imports 
prices_imports = test[5:10]
# By Pipeline
prices_i_bp = test[10:15]
# As Liquified Natural Gas (LNG)
prices_i_lng = test[15:20]

### Exports
prices_e_exports = test[20:25]
# By Pipeline
prices_e_bp = test[25:30]
# As Liquified Natural Gas
prices_e_lng = test[30:35]

### Citygate
prices_citygate = test[35:40]

### Residential
prices_resid = test[40:45]

### Commercial
prices_commer = test[45:50]

### Industrial
prices_indust = test[50:55]

### Electric Power
prices_elec_pow = test[55:60]

######### Production (Mcf)

### Gross Withdrawals
prod_gw = test[60:65]

### Marketed Production
prod_mp = test[100:105]

### NGPL Production
prod_ngpl = test[105:110]

### Dry Production
prod_dry = test[110:115]

######### Imports/Exports (Mcf)

### Imports Volume
vol_i_imports = test[115:120]
# By Pipeline
vol_i_bp = test[120:125]
# As Liquified Natural Gas
vol_i_lng = test[125:130]

### Exports Volume
vol_e_exports = test[130:135]
# By Pipeline
vol_e_bp = test[135:140]
# As Liquified Natural Gas
vol_e_lng = test[140:145]

######### Underground Storage (Mcf)

### Total Capacity 
stor_tc = test[145:150]

### Gas in Storage
stor_gs = test[150:155]
# Base Gas 
stor_bg = test[155:160]
# Working Gas
stor_wg = test[160:165]

### Injections
stor_Injec = test[165:170]

### Withdrawals
stor_Withd = test[170:175]

### Net Withdrawals
stor_nw = test[175:180] 

######### Consumption (Mcf)

### Total Consumption
consump_tc = test[180:185]
# Lease and Plant Fuel
consump_lpf = test[185:190]
# Pipeline & Distribution Use
consump_pdu = test[190:195]
# Delivered to Consumers
consump_d2c = test[195:200]
# Residential
consump_resid = test[200:205]
# Commercial
consump_commer = test[205:210]
# Industrial
consump_indust = test[210:215]
# Vehicle Fuel
consump_vf = test[215:220]
# Electric Power
consump_ep = test[220:225]
#########################################################################
####################### *****Data Manipulation***** #############################
#### Converting the html data to text

# Inserting Prices Categ
Prices = []
prices_imports_filtered = (prices_imports[0].text, prices_imports[1].text, prices_imports[2].text, prices_imports[3].text, prices_imports[4].text)
prices_i_bp_filtered = (prices_i_bp[0].text, prices_i_bp[1].text, prices_i_bp[2].text, prices_i_bp[3].text, prices_i_bp[4].text)
prices_i_lng_filtered = (prices_i_lng[0].text, prices_i_lng[1].text, prices_i_lng[3].text, prices_i_lng[4].text)
prices_e_exports_filtered = (prices_e_exports[0].text, prices_e_exports[1].text, prices_e_exports[2].text, prices_e_exports[3].text, prices_e_exports[4].text)
prices_e_bp_filtered = (prices_e_bp[0].text, prices_e_bp[1].text, prices_e_bp[2].text, prices_e_bp[3].text, prices_e_bp[4].text)
prices_e_lng_filtered = (prices_e_lng[0].text, prices_e_lng[1].text, prices_e_lng[2].text, prices_e_lng[3].text, prices_e_lng[4].text)
prices_citygate_filtered = (prices_citygate[0].text, prices_citygate[1].text, prices_citygate[2].text, prices_citygate[3].text, prices_citygate[4].text)
prices_resid_filtered = (prices_resid[0].text, prices_resid[1].text, prices_resid[2].text, prices_resid[3].text, prices_resid[4].text)
prices_commer_filtered = (prices_commer[0].text, prices_commer[1].text, prices_commer[2].text, prices_commer[3].text, prices_commer[4].text)
prices_indust_filtered = (prices_indust[0].text, prices_indust[1].text, prices_indust[2].text, prices_indust[3].text, prices_indust[4].text)
prices_elec_pow_filtered = (prices_elec_pow[0].text, prices_elec_pow[1].text, prices_elec_pow[2].text, prices_elec_pow[3].text, prices_elec_pow[4].text) 
# Inserting Production Categ
Production = []
prod_gw_filtered = (prod_gw[0].text, prod_gw[1].text, prod_gw[2].text, prod_gw[3].text, prod_gw[4].text)
prod_mp_filtered = (prod_mp[0].text, prod_mp[1].text, prod_mp[2].text, prod_mp[3].text, prod_mp[4].text)
prod_ngpl_filtered = (prod_ngpl[0].text, prod_ngpl[1].text, prod_ngpl[2].text, prod_ngpl[3].text, prod_ngpl[4].text) 
prod_dry_filtered = (prod_dry[0].text, prod_dry[1].text, prod_dry[2].text, prod_dry[3].text, prod_dry[4].text)
# Inserting Volume Categ
Volume = []
vol_i_imports_filtered = (vol_i_imports[0].text, vol_i_imports[1].text, vol_i_imports[2].text, vol_i_imports[3].text, vol_i_imports[4].text) 
vol_i_bp_filtered = (vol_i_bp[0].text, vol_i_bp[1].text, vol_i_bp[2].text, vol_i_bp[3].text, vol_i_bp[4].text)
vol_i_lng_filtered = (vol_i_lng[0].text, vol_i_lng[1].text, vol_i_lng[2].text, vol_i_lng[3].text, vol_i_lng[4].text)
vol_e_exports_filtered = (vol_e_exports[0].text, vol_e_exports[1].text, vol_e_exports[2].text, vol_e_exports[3].text, vol_e_exports[4].text)
vol_e_bp_filtered = (vol_e_bp[0].text, vol_e_bp[1].text, vol_e_bp[2].text, vol_e_bp[3].text, vol_e_bp[4].text)
vol_e_lng_filtered = (vol_e_lng[0].text, vol_e_lng[1].text, vol_e_lng[2].text, vol_e_lng[3].text, vol_e_lng[4].text)
# Inserting Storing Categ
Storage = []
stor_tc_filtered = (stor_tc[0].text, stor_tc[1].text, stor_tc[3].text, stor_tc[3].text, stor_tc[4].text)
stor_gs_filtered = (stor_gs[0].text, stor_gs[1].text, stor_gs[2].text, stor_gs[3].text, stor_gs[4].text)
stor_bg_filtered = (stor_bg[0].text, stor_bg[1].text, stor_bg[2].text, stor_bg[3].text, stor_bg[4].text)
stor_wg_filtered = (stor_wg[0].text, stor_wg[1].text, stor_wg[2].text, stor_wg[3].text, stor_wg[4].text)
stor_Injec_filtered = (stor_Injec[0].text, stor_Injec[1].text, stor_Injec[2].text, stor_Injec[3].text, stor_Injec[4].text)
stor_Withd_filtered = (stor_Withd[0].text, stor_Withd[1].text, stor_Withd[2].text, stor_Withd[3].text, stor_Withd[4].text)
stor_nw_filtered = (stor_nw[0].text, stor_nw[1].text, stor_nw[2].text, stor_nw[3].text, stor_nw[4].text)
# Inserting Consumption Categ
Consumption = []
consump_tc_filtered =  (consump_tc[0].text, consump_tc[1].text, consump_tc[2].text, consump_tc[3].text, consump_tc[4].text,)
consump_lpf_filtered = (consump_lpf[0].text, consump_lpf[1].text, consump_lpf[2].text, consump_lpf[3].text, consump_lpf[4].text)
consump_pdu_filtered = (consump_pdu[0].text, consump_pdu[1].text, consump_pdu[2].text, consump_pdu[3].text, consump_pdu[4].text)
consump_d2c_filtered = (consump_d2c[0].text, consump_d2c[1].text, consump_d2c[2].text, consump_d2c[3].text, consump_d2c[4].text,)
consump_resid_filtered = (consump_resid[0].text, consump_resid[0].text, consump_resid[2].text, consump_resid[3].text, consump_resid[4].text)
consump_commer_filtered = (consump_commer[0].text, consump_commer[1].text, consump_commer[2].text, consump_commer[3].text, consump_commer[4].text)
consump_indust_filtered = (consump_indust[0].text, consump_indust[1].text, consump_indust[2].text, consump_indust[3].text, consump_indust[4].text)
consump_vf_filtered = (consump_vf[0].text, consump_vf[1].text, consump_vf[2].text, consump_vf[3].text, consump_vf[4].text,)
consump_ep_filtered = (consump_ep[0].text, consump_ep[1].text, consump_ep[2].text, consump_ep[3].text, consump_ep[4].text)


#### Creating an Index Names
dates = ('Sep-2019', 'Oct-2019', 'Nov-2019', 'Dec-2019', 'Feb-2020')

#### Creating Columns Names
idex = ('Prices', 'Import Prices', 'Import Prices By Pipeline', 'Import Prices As Liquified NatGas', 'Export Prices', 'Export Prices By Pipeline', 'Export Prices As Liquified NatGas',
     'Citygate Prices', 'Residential Prices', 'Commercial Prices', 'Industrial Prices', 'Electric Power Prices', 'Production', 'Gross Withdrawals', 'Marketed Production', 'NGPL Production', 
     'Dry Production', 'Volume',  'Import Volume(Mcf)', 'Import Volume By Pipeline', 'Import Volume As LNG', 'Export Volume(Mcf)', 'Export Volume By Pipeline', 'Export Volume As LNG', 
     'Storage', 'Total Capacity', 'Gas in Storage', 'Base Gas', 'Working Gas', 'Injections', 'Withdrawals', 'Net Withdrawals', 'Consumption', 'Total Consumption', 'Lean & Plant Fuel', 'Pipeline & Distribution Use',
     'Delivered to Consumers', 'Residential', 'Commercial', 'Industrial', 'Vehicle Fuel', 'Electric Power')

#### Creating DataFrame  
data = (Prices, prices_imports_filtered, prices_i_bp_filtered, prices_i_lng_filtered, prices_e_exports_filtered, prices_e_bp_filtered, 
        prices_e_lng_filtered, prices_citygate_filtered, prices_resid_filtered, prices_commer_filtered, prices_indust_filtered, 
        prices_elec_pow_filtered, Production, prod_gw_filtered, prod_mp_filtered, prod_ngpl_filtered, prod_dry_filtered, Volume, vol_i_imports_filtered, 
        vol_i_bp_filtered, vol_i_lng_filtered, vol_e_exports_filtered, vol_e_bp_filtered, vol_e_lng_filtered, Storage, stor_tc_filtered, stor_gs_filtered, 
        stor_bg_filtered, stor_wg_filtered, stor_Injec_filtered, stor_Withd_filtered, stor_nw_filtered, Consumption, consump_tc_filtered, consump_lpf_filtered,
        consump_pdu_filtered, consump_d2c_filtered, consump_resid_filtered, consump_commer_filtered, consump_indust_filtered, 
        consump_vf_filtered, consump_ep_filtered)
df = pd.DataFrame(data, index=idex, columns=dates)

# Exporting to .csv file
df.to_csv('natgas_data.csv')
############################################################################################
#################### ********* END ********* ###################################
