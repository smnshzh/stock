from stock import Bourse
from db import db,Symbol
from progress.bar import Bar
class UpdateSymbols:
    def __init__(self, *args, **kwargs):
        
        bours=Bourse()
        symbols= bours.get_symbol_info()
        db.connect()
        print("db connected")
        num=len(symbols)
        print("creation started,number of creation="+str(num))
        craetaionBar = Bar(f"Creation{num}",max=len(symbols))
        for symbol in symbols:
            counter = Symbol.select().where(Symbol._id==symbol["id"])
            selection=[item for item in counter]
            if len(selection):
                print(symbol["group"],symbol["name"])
                Symbol.create(
                _id=symbol["id"],
                name=symbol["name"],
                group=symbol["group"],
                namad=symbol["namad"]
                    )
                num-=1
                craetaionBar.next()    
            else:
                num-=1
                craetaionBar.next()    
                    
                
        db.close()        