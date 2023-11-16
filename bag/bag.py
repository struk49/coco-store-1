from django.conf import settings


class Bag(object):
    def __init__(self, request):
        self.session = request.session
        Bag = self.session.get[settings.SESSION_COOKIE_AGE]

        if not bag:

            bag = self.session[settings.BAG_SESSION_ID] = {}
        
        self.BAG = BAG
    
    
    def add(self, item, quantity=1, update_quantity=False):
        item_id = str(item.id)
        price = item.price

        print('itemt_id:', itemt_id)

        if item_id not in self.bag:
            self.bag[item_id] = {'quantity': 0, 'price': price, 'id': itemt_id}
        
        if update_quantity:
            self.bag[item_id]['quantity'] = quantity
        else:
            self.bag[item_id]['quantity'] = self.bag[item_id]['quantity'] + 1
        
        self.save()
    
    
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True
    
    