import pandas as pd
import datetime
import csv
import eel


### 商品クラス
class Item:
    def __init__(self,item_code,item_name,price):
        self.item_code=item_code
        self.item_name=item_name
        self.price=price
    
    def get_price(self):
        return self.price


### オーダークラス
class Order:
    def __init__(self,item_master,order_count,total_price):
        self.item_order_list=[]

        self.order_count = order_count
        self.order_count_list = []

        self.item_master=item_master
        self.buy_item_list=[]

        self.total_price = total_price

    def add_item_order(self,item_code,order_count):
        self.item_order_list.append(item_code)
        self.order_count_list.append(order_count)
       
    
    def add_buy_order(self,buy_item):
        self.buy_item_list.append(buy_item)

    def search_master(self,total_price):
        self.total_price=total_price
        for item in self.item_master:
            for item_order,order_count in zip(self.item_order_list,self.order_count_list):
                if item.item_code == item_order:
                    print(f"商品コード{item.item_code}:{item.item_name}￥{item.price}円/{order_count}個")
                    eel.view_log_js(f"商品コード{item.item_code}:{item.item_name}￥{item.price}円/{order_count}個")
                    buy_item =f"{item.item_name} ￥{item.price}円 /{order_count}個\n"
                    self.add_buy_order(buy_item)
                    order_price = int(item.price)*int(order_count)
                    self.total_price = order_price +self.total_price
            else:
                pass
        print(f"\n合計金額は{self.total_price}円")
        eel.view_log_js(f"\n合計金額は{self.total_price}円")
    
    def receipt(self,item_money):
        dt_now = datetime.datetime.now()
        return_money = item_money-self.total_price
        res1=''.join(''.join(map(str,x))for x in self.buy_item_list)
        res2 = f"{dt_now}\n{res1}\n合計金額{self.total_price}円\nお預かり{item_money}円\nおつり{return_money}円 "

        with open("レシート.txt",mode='w') as f:
            f.write(res2)
        print(res2)
        eel.view_log_js(res2)
         

### メイン処理
def main(item_code,item_count):
    
    # マスタ登録
    item_master=[]
    order_count=[]
    total_price=0
    #商品マスター.csvからデータを読み込み
    with open("商品マスター.csv",'r') as f:
        header =next(csv.reader(f))
        reader = csv.reader(f)
        access_log = [row for row in reader]
   
    item_code_list = []
    item_name_list = []
    price_list = []
    

    for row in access_log:
        item_code_list.append(row[0])
        item_name_list.append(row[1])
        price_list.append(row[2])
    
    #各リストをItem()に入れていく
    for item_code, item_name, price in zip(item_code_list,item_name_list,price_list):
        item_master.append(Item(item_code, item_name, price))
    
    # オーダー登録
    order=Order(item_master,order_count,total_price)

    while True:
        if item_code == "000":
            #customer_money =eel.view_log_js(int(input("支払い金額を入力してください：")))
            break
        else:
            order.add_item_order(item_code,item_count)
            
    order.search_master(total_price)
  
    # マスター検索      
    
