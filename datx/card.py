# -*- coding: utf-8 -*- 
from .city_code import city_code2info
import os
import re
import pandas as pd

__all__ = ['card2info', 'cmb_debit2info']

df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'card_bin.csv'))
df['org_code'] = df.org_code.apply(lambda x: '%08d'%x)
df['bin'] = df.bin.apply(str)

card = {}
for card_len,g1 in df.groupby(['card_len']):
    card[card_len] = {}
    for bin_len, g2 in g1.groupby(['bin_len']):
        card[card_len][bin_len] = dict(zip(g2.bin, g2.to_dict('redords')))

df_ = pd.read_csv(os.path.join(os.path.dirname(__file__), 'cmb_branch.csv'))
df_['prefix'] = df_.prefix.apply(lambda x: '%03d'%x)
df_['city_code'] = df_.city_code.apply(str)
cmb_branch = dict(zip(df_.prefix, df_.to_dict('records')))

def cmb_debit2info(card):
    card_ = card.strip()
    if not re.match('^\d{16}$', card_):
        raise ValueError
    branch = cmb_branch.get(card_[6:9])
    if branch:
        branch['city'] = city_code2info(branch['city_code'])['city']
    return branch
    
def card2info(card__):
    card_ = card__.strip()
    if not re.match('^\d{14,19}$', card_):
        raise ValueError
    card_len = len(card_)
    for bin_len in sorted(card[card_len].keys(), reverse=True):
        if card_[:bin_len] in card[card_len][bin_len]:
            return card[card_len][bin_len][card_[:bin_len]]
    return None