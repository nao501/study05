import desktop
import eel
import pos

app_name="html"
end_point="index.html"
size=(700,600)

class Order:
    def __init__(self,order_code,order_count):
        self.order_code = order_code
        self.item_order_list=[]

        self.order_count = order_count
        self.order_count_list = []

    def add_item_order(self,order_code,order_count):
        self.item_order_list.append(order_code)
        self.order_count_list.append(order_count)

      
@ eel.expose
def main(order_codes,order_counts,item_money):
    order=Order(order_codes,order_counts)
    order.add_item_order(order_codes,order_counts)
    
    for item_code,item_count in zip(order.item_order_list, order.order_count_list): 
        pos.main(item_code,item_count,item_money)
        

desktop.start(app_name,end_point,size)