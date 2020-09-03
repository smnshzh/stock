import pytse_client as tse
import matplotlib.pyplot as plt
import numpy as np
import requests
from datetime import datetime,timedelta
from progress.bar import Bar
from stock import SymbolsTse
import jdatetime
#matlabing tse online

class OnlineMatlabingByEntryNamad:
    def __init__(self, *args, **kwargs):
        def daterange(date1, date2):
            for n in range(int ((date2 - date1).days)+1):
                yield date1 + timedelta(n) 
        EnterNamad=input("نماد را وارد کنید")
        try:# Establish connection to tsetc
            requests.get("http://www.tsetmc.com/Loader.aspx?ParTree=15")
        except:
             print("conection to http://www.tsetmc.com/Loader.aspx?ParTree=15 can not establish")
             asking=input("press q for quit and any key for replay:   ")
             if asking != 'q':
                 OnlineMatlabingByEntryNamad() 
             else:
                exit()        
        try:
            tse.download(symbols=EnterNamad, write_to_csv=True, include_jdate=True)
            ticker = tse.Ticker(EnterNamad)
            history = ticker.history
            df = history.values.tolist()
            
            
            startDate = input(f"Enter Start date(yyyy-mm-dd) between"+ df[0][-1]
                               +" and "+
                                df[-1][-1]
                                +" ")
            endDate = input("Enter End date(yyyy-mm-dd)between"+ startDate +" and "+
                             df[-1][-1]
                             + " ")
            
            if bool(startDate):
                startDate=jdatetime.date(int(startDate[:4]),int(startDate[5:7]),int(startDate[8:])).togregorian()
                startDate=startDate.strftime("%Y-%m-%d")
            else: 
                startDate=(datetime.now()-timedelta(days=30)).strftime("%Y-%m-%d")    
            print(startDate)
            if not bool(endDate):
                endDateNow=datetime.now()
                endDate=endDateNow.strftime("%Y-%m-%d")
                print(endDate)
            else:
                endDate=jdatetime.date(int(endDate[:4]),int(endDate[5:7]),int(endDate[8:])).togregorian()
                print(endDate)    
                   
            x= [item[-1] for item in df if datetime.strptime(item[0],"%Y-%m-%d") >= datetime.strptime(startDate,"%Y-%m-%d") and datetime.strptime(item[0],"%Y-%m-%d")< datetime.strptime(endDate,"%Y-%m-%d")]
            o= [item[1]/10 for item in df if datetime.strptime(item[0],"%Y-%m-%d") >= datetime.strptime(startDate,"%Y-%m-%d") and datetime.strptime(item[0],"%Y-%m-%d")< datetime.strptime(endDate,"%Y-%m-%d")]
            y= [item[8]/10 for item in df if datetime.strptime(item[0],"%Y-%m-%d") >= datetime.strptime(startDate,"%Y-%m-%d") and datetime.strptime(item[0],"%Y-%m-%d")< datetime.strptime(endDate,"%Y-%m-%d")]
            plt.plot(x,y,color="red",label="close",marker="8")
            plt.plot(x,o,color="blue",label="open",marker="8")
            plt.title(EnterNamad)
            plt.xlabel("Date")
            plt.xticks(rotation='vertical',fontsize=5)
            plt.ylabel("Close Price(تومان)")
            plt.legend()
            plt.show()
            plt.savefig(EnterNamad)
            continue_or_not = input("Entar any key if you want matlabing again press q for quit")
            
            if continue_or_not != "q":
                OnlineMatlabingByEntryNamad()
            else:
                exit()    

            
                   
        except Exception:
            print("worng namad")
            OnlineMatlabingByEntryNamad()
 # THIS CLASS FINDS SHARES THAT HAS DEFFRENCES           
class FindShare:
    def __init__(self, *args, **kwargs):
        
        self.tickers =SymbolsTse().get_all_symbols() 
        
    def diffrence(self,num):
        symbols_list=[]
        progress=Bar("Progress",max=len(self.tickers))
        for item in self.tickers:
            try:
                tse.download(symbols=item, write_to_csv=True, include_jdate=True)
                ticker = tse.Ticker(item)
                history_geter=ticker.history
                hight_prices=[price[2] for price in history_geter.values.tolist()]
                last_price=ticker.last_price
                higt_price=max(hight_prices)
                diff=(higt_price-last_price)/last_price*100
                if diff > num:
                    log=open("share.log","a+",encoding="utf-8")
                    log.write(f"{datetime.now()}{item}\n")
                    log.close()
                    symbols_list.append(item)
                    progress.next()    
            except:
                errorLog=open("Error_log.log","a+",encoding="utf-8")
                errorLog.write(f"{datetime.now()}{item} not find\n ")
                errorLog.close()
                progress.next()
        return symbols_list
    #BY DEFAULT THIS CLASS MAKES PLOT OF ONE MONTH , BUT WITH CHENGING IN START AND END DATE YOU
    #CAN CHANG DURATION OF PLOT, VOlUME CAN BE DISPLAYED IF SET IT TRUE AND YOU CAN DEVIDE IT BUY SET
    #DEVIDED.
    def MatlabingNamad(self,namad,
                       startDate=(datetime.now()-timedelta(days=30)).strftime("%Y-%m-%d"),
                       endDate=datetime.now().strftime("%Y-%m-%d"),
                       volume=False,devide=100):
       
            ticker = tse.Ticker(namad)
            history_ticker = ticker.history
            df = history_ticker.values.tolist()

            x= [item[-1] for item in df if datetime.strptime(item[0],"%Y-%m-%d") >= datetime.strptime(startDate,"%Y-%m-%d") and datetime.strptime(item[0],"%Y-%m-%d")<= datetime.strptime(endDate,"%Y-%m-%d")]
            y= [item[8]/10 for item in df if datetime.strptime(item[0],"%Y-%m-%d") >= datetime.strptime(startDate,"%Y-%m-%d") and datetime.strptime(item[0],"%Y-%m-%d")<= datetime.strptime(endDate,"%Y-%m-%d")]
            plt.plot(x,y,label=namad)
            
            if volume == True:
                z= [(item[6])/100 for item in df if datetime.strptime(item[0],"%Y-%m-%d") >= datetime.strptime(startDate,"%Y-%m-%d") and datetime.strptime(item[0],"%Y-%m-%d")<= datetime.strptime(endDate,"%Y-%m-%d")]
                plt.bar(x,z,label="حجم",color="green")
            plt.xlabel("Date")
            plt.xticks(rotation='vertical',fontsize=5)
            plt.ylabel("Close price (تومان)")
            plt.legend()
            plt.show()      
   
            