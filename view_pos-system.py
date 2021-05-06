import desktop
import eel
import pos
from pos import Order


app_name="html"
end_point="index.html"
size=(700,600)

item_master=[]
order_count=[]
total_price=0


order=pos.main()

      
@ eel.expose
def main(order_codes,order_counts):
    order.add_item_order(order_codes,order_counts)
    order.search_master(total_price)
    
   
@ eel.expose   
def main2(item_money):
    order.receipt(item_money)
    order.clear_list()

    
@ eel.expose
def items_append (items_code,items_name,items_price):
    PASS=r"商品マスター.csv"
    with open(PASS) as f:
         Item_name = f.readlines()
         Item_deta =[ deta.strip() for deta in Item_name ]
         for  deta in Item_name:
            print(deta.strip())   

    list_append =f'{items_code},{items_name},{items_price}'
    Item_deta.append(list_append)
    eel.view_log_js2(f"{list_append}追加しました")
    
    PASS=r'商品マスター.csv'
    with open(PASS,mode='w') as f:
        f.writelines("\n".join(Item_deta))
    
    
        

desktop.start(app_name,end_point,size)