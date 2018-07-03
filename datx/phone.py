# -*- coding: utf-8 -*- 
import pandas as pd

__all__ = ['phone2info']

phone = pd.read_csv(os.path.join(os.path.dirname(__file__), 'phone-qqzeng.csv'))
zphone = dict(zip(phone.phone.apply(str), phone.to_dict('records')))
def phone2info(ph):
    phone_ = ph.strip()
    if not re.match('^\d{7,11}$', phone_):
        raise ValueError
    return zphone.get(phone_[:7])