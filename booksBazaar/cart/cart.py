from decimal import Decimal
from django.conf import settings
from app1.models import Book



class Cart(object):

    def __init__(self, request):
       
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
    
        self.coupon_id = self.session.get('coupon_id')

    def __len__(self):
     
        return sum(item['quantity'] for item in self.cart.values())

    def __iter__(self):
  
        book_ids = self.cart.keys()
        
        books = Book.objects.filter(id__in=book_ids)
        for book in books:
            self.cart[str(book.id)]['book'] = book

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def add(self, book, quantity=1, update_quantity=False):
  
        book_id = str(book.id)
        if book_id not in self.cart:
            self.cart[book_id] = {'quantity': 0,
                                      'price': str(book.price)}
        if update_quantity:
            self.cart[book_id]['quantity'] = quantity
        else:
            self.cart[book_id]['quantity'] += quantity
        self.save()

    def remove(self, book):
       
        book_id = str(book.id)
        if book_id in self.cart:
            del self.cart[book_id]
            self.save()

    def save(self):
       
        self.session[settings.CART_SESSION_ID] = self.cart
       
        self.session.modified = True

    def clear(self):
        
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True

    @property
    def coupon(self):
        if self.coupon_id:
            return Coupon.objects.get(id=self.coupon_id)
        return None

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def get_discount(self):
        if self.coupon:
            return (self.coupon.discount / Decimal('100')) * self.get_total_price()
        return Decimal('0')

    def get_total_price_after_discount(self):
        return self.get_total_price() - self.get_discount()
