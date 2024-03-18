class Home:
    def __init__(self, header_name, area, price_for_m2):
        self.header_name = header_name
        self.area = area
        self.price = round(float(price_for_m2) * float(area), 2)
        self.price_for_m2 = price_for_m2
        print(str(price_for_m2) + " " + str(self.price))
