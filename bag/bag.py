from django.conf import settings


class Bag(object):
    def __init__(self, request):
        self.session = request.session
        bag = self.session.get(settings.BAG_SESSION_ID)

        if not bag:
            bag = self.session[settings.BAG_SESSION_ID] = {}
        
        self.bag = bag
    
    def __iter__(self):
        item_ids = self.bag.keys()        
        item_ids_clean_ids = []

        for i in item_ids:
            item_clean_ids.append(p)

            self.bag[str(p)]['item'] = Item.objects.get(pk=p)

        for item in self.bag.values():
            item['total_price'] = float(item['price']) * int(item['quantity'])

            yield item
        

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        price = product.price

        print('Product_id:', product_id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': price, 'id': product_id}
        
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] = self.cart[product_id]['quantity'] + 1
        
        self.save()
    
    
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
    
    