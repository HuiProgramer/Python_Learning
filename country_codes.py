from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    """根据指定的国家名字寻找编码"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    #如果没找到就返回None
    return None