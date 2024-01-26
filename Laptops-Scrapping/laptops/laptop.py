class Laptop :
    def __init__(self, id, name, title, description, category, mrp, sellingPrice, discount, weight, brandName, imageUrl, specifications):
        self.id = id
        self.name = name
        self.title = title
        self.description = description
        self.category = category
        self.mrp = mrp
        self.sellingPrice = sellingPrice
        self.discount = discount
        self.weight = weight
        self.brandName = brandName
        self.imageUrl = imageUrl
        self.specifications = specifications

class Product :
    def __init__(self, title, price,rating, description ):
        self.title = title
        self.description = description
        self.price = price
        self.rating= rating      