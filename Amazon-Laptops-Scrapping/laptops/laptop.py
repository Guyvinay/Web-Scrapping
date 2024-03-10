class Laptop :
    def __init__(self, id, name, title, model , description, category, mrp, sellingPrice, discount, weight, brandName, imageUrl, specifications, rating, countryOfOrigin):
        self.id = id
        self.name = name
        self.title = title
        self.model = model
        self.description = description
        self.category = category
        self.mrp = mrp
        self.sellingPrice = sellingPrice
        self.discount = discount
        self.weight = weight
        self.brandName = brandName
        self.imageUrl = imageUrl
        self.specifications = specifications
        self.rating = rating
        self.countryOfOrigin = countryOfOrigin

class Product :
    def __init__(self, title, price,rating, description ):
        self.title = title
        self.description = description
        self.price = price
        self.rating= rating      