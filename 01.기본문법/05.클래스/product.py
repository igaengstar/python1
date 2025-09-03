class Product:
    def __init__(self, code, name, price): 
        self.code = code
        self.name = name
        self.price = price

    def to_dict(self):
        return {'code': self.code, 'name': self.name, 'price': self.price}
    
if __name__ =='__main__':
    p = Product('P01', '냉장고', 250)
    print(p.to_dict())