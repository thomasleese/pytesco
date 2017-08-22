from tesco import Tesco


tesco = Tesco(api_key)

results = tesco.lookup(gtin=1285340390232)
