class  Biblio:
    books=0

    def __init__(self,category,title,price):
        self.category = category
        self.title = title
        self.price = price
        Biblio.num_books+=1

    def display_data(self):
        print('Category: ',self.category)
        print('Title: ',self.title)
        print('Price: ',self.price'EUR')

    def apply_discount(self,discount_percent):
        self.price*=(1-discount_percent/100)

books=[
    Biblio("Ξενόγλωσσο","Dexter","20.0")
    Biblio("Ξενόγλωσσο","Fight Club","15.0")
    Biblio()


]

    

