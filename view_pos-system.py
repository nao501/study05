import desktop
import eel
import pos

app_name="html"
end_point="index.html"
size=(700,600)


@ eel.expose
def main(item_codes,order_counts):
    pos.main(item_codes,order_counts)

desktop.start(app_name,end_point,size)