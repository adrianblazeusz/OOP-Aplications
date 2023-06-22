class Temperatuer:

    def __init__(self, country, city):
        self.country = country
        self.city = city

    def get(self):
        pass


temperature = Temperatuer(city="bialystok", country="poland")
print(temperature.get())
