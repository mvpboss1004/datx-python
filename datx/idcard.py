# -*- coding: utf-8 -*- 
from .city_code import city_code2info
__all__ = ['idcard2info']

def idcard2info(id):
    id_ = id.strip()
    if not re.match('^[1-9]\d{5}(18|19|(2\d))\d{2}((0[1-9])|(1[0-2]))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]$', id_):
        raise ValueError
    info = city_code2info(id_[:6])
    if not info:
        return None
    else:
        info['year'] = int(id_[6:10])
        info['month'] = int(id_[10:12])
        info['day'] = int(id_[12:14])
        return info