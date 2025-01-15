class Asset:
    """Base class"""

    def __init__(self, name, address, revenue):
        self.name = name
        self.address = address
        self.revenue = revenue

class Villa(Asset):

    def __init__(self, name, address, rent, maintenance):
        super().__init__(name, address, 0)
        self.rent = rent
        self.maintenance = maintenance
    """Displays revenue and whether or not the property made money"""

    def r(self):
        self.revenue = self.rent - self.maintenance
        if self.revenue > 1:
            print(f"Total Revenue: {self.revenue}")
        else:
            print("Property generated no revenue")
    """Displays detail about the property"""

    def display(self):
        print(f"\nName of Property: {self.name}\nAddress: {self.address}"
              f"\nRent: {self.rent}\nMaintenance Fees: {self.maintenance}")


class Apartment:

    def __init__(self, rent, maintenance):
        self.rent = rent
        self.maintenance = maintenance


class Building(Asset):

    def __init__(self, name, address, a_rent, a_maintenance, amount):
        super().__init__(name, address, 0)
        self.a_rent = a_rent
        self.a_maintenance = a_maintenance
        self.amount = amount
    """Displays revenue and whether or not the property made money"""

    def r(self):
        self.revenue = self.a_rent - self.a_maintenance
        if self.revenue > 1:
            print(f"Total Revenue: {self.revenue}")
        else:
            print("Property generated no revenue")
    """Displays detail about the property"""

    def display(self):
        print(f"\nName of Property: {self.name}\nAddress: {self.address}"
              f"\nRent: {self.a_rent}\nMaintenance Fees: {self.a_maintenance}"
              f" \nTotal apartments {self.amount}")


apartment = Apartment(3000, 1500)
building = Building('Soleste Spring Garden',
                    '1005 Spring Garden Rd',
                    apartment.rent, apartment.maintenance, 20)
villa1 = Villa('Sunset Retreat','5415 Harrison St',4500,
               2250)
villa2 = Villa('Starlight Villa','2345 SW 1st St', 6900,
               3450)
villa3 = Villa('Serenity Cove','3750 S Dixie Hwy', 2000,
               3450)


building.display()
building.r()
villa1.display()
villa1.r()
villa2.display()
villa2.r()
villa3.display()
villa3.r()
