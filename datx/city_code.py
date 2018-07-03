# -*- coding: utf-8 -*- 
import pandas as pd

__all__ = ['zcity_code', 'city_code2info']

city_code = pd.read_csv(os.path.join(os.path.dirname(__file__), 'china_city_code.csv'))
zcity_code = dict(zip(city_code.code.apply(str), city_code.to_dict('records')))
def city_code2info(code):
    code_ = code.strip()
    if not re.match('^\d{6}$', code_):
        raise ValueError
    return zcity_code.get(code_[:4]+'00')