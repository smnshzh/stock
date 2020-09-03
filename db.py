from peewee import *
from datetime import datetime
db = MySQLDatabase('bours',user='root', password='saman@1400',
                         host='127.0.0.1', port=3306)
class Group(Model):
     
    name = CharField(unique=True)
    _id= CharField()
    class Meta():
        database=db

class Symbol(Model):
    _id=CharField(unique=True)
    name=CharField()
    group=ForeignKeyField(Group)
    namad=CharField()
    class Meta():
        database=db
        
class ShareData(Model):
    symbol=ForeignKeyField(Symbol)
    _date= DateField()
    _open=CharField(max_length=20)
    _hight= CharField(max_length=20)
    _low= CharField(max_length=20)
    _adjclose=CharField(max_length=20)
    _value = CharField(max_length=20)
    _volume= CharField(max_length=20)
    _count = CharField(max_length=20)
    _close = CharField(max_length=20)
    class Meta():
        database=db
           

# with data bse
# db.connect()
# symbol_select=Symbol.select().where(Symbol.id<6)
# share_data_selection= ShareData.select().where(ShareData.symbol<6)
# for item in share_data_selection:
#     if item.symbol.namad in data.keys() and item._date.year>2019 and item._date.month>6:
        
#         data[item.symbol.namad][item._date.strftime("%b %d")]=item._close
#     else:
#         if item._date.year>2019 and item._date.month>6:
#             data[item.symbol.namad]={item._date.strftime("%b %d"):item._close}  
        
# keyNumber = [key for key in data]

# print(keyNumber)
# for item in keyNumber:
#     x1=[date for date in data[item]]
#     y1=[float(price) for price in data[item].values()]
#     plt.plot(x1,y1,label=keyNumber[0])
#     plt.xlabel("Date")
#     plt.ylabel("Close Price")
#     plt.legend()
#     plt.show()
         
# db.close() 