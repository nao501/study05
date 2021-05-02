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


order=Order(item_master,order_count,total_price)  

      
@ eel.expose
def main(order_codes,order_counts):
    order.add_item_order(order_codes,order_counts)
    for item_code,item_count in zip(order.item_order_list, order.order_count_list): 
        pos.main(item_code,item_count)

@ eel.expose   
def main2(item_money):
    pos.receipt(item_money)

        

desktop.start(app_name,end_point,size)