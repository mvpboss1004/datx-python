# -*- coding: utf-8 -*- 
from collections import OrderedDict
import pandas as pd

__all__ = ['mac2info']

oui = OrderedDict()
oui[9] = os.path.join(os.path.dirname(__file__), 'oui36.csv')
oui[7] = os.path.join(os.path.dirname(__file__), 'mam.csv')
oui[6] = os.path.join(os.path.dirname(__file__), 'oui.csv')
for key in oui:
    df = pd.read_csv(oui[key])
    oui[key] = dict(zip(df.Assignment, df.to_dict('records')))
    
def mac2info(mac):
    mac_ = mac.strip().upper().replace(':','').replace('-','')
    if not re.match('^[0-9A-F]{0,12}$', mac_):
        raise ValueError
    for key in oui:
        if len(mac_) >= key and mac_[:key] in oui[key]:
            return oui[key][mac_[:key]]
    return None