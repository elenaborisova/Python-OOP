from movie_world_02.project.customer import Customer
from movie_world_02.project.dvd import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers: list = []
        self.dvds: list = []

    @staticmethod
    def dvd_capacity():
        DVD_CAPACITY = 15
        return DVD_CAPACITY

    @staticmethod
    def customer_capacity():
        CUSTOMER_CAPACITY = 10
        return CUSTOMER_CAPACITY

    def exceed_customer_capacity(self):
        return len(self.customers) >= self.customer_capacity()

    def exceed_dvd_capacity(self):
        return len(self.dvds) >= self.dvd_capacity()

    def find_dvd_by_id(self, dvd_id: int):
        return [dvd for dvd in self.dvds if dvd.id == dvd_id][0]

    def find_customer_by_id(self, customer_id: int):
        return [customer for customer in self.customers if customer.id == customer_id][0]

    def add_customer(self, customer: Customer):
        if not self.exceed_customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if not self.exceed_dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        dvd = self.find_dvd_by_id(dvd_id)
        customer = self.find_customer_by_id(customer_id)

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"
        if dvd.is_rented:
            return "DVD is already rented"
        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int):
        dvd = self.find_dvd_by_id(dvd_id)
        customer = self.find_customer_by_id(customer_id)

        if dvd not in customer.rented_dvds:
            return f"{customer.name} does not have that DVD"

        customer.rented_dvds.remove(dvd)
        dvd.is_rented = False
        return f"{customer.name} has successfully returned {dvd.name}"

    def __repr__(self):
        result = ""
        customers = "\n".join(str(customer) for customer in self.customers)
        dvds = "\n".join(str(dvd) for dvd in self.dvds)
        result += f"{customers}\n{dvds}"
        return result


c1 = Customer("John", 18, 1)
c2 = Customer("Anna", 55, 2)

d1 = DVD("Black Widow", 1, 2020, "April", 18)
d2 = DVD.from_date(2, "The Croods 2", "23.12.2020", 3)

movie_world = MovieWorld("The Best Movie Shop")

movie_world.add_customer(c1)
movie_world.add_customer(c2)
movie_world.add_dvd(d1)
movie_world.add_dvd(d2)

print(movie_world.rent_dvd(1, 1))
print(movie_world.rent_dvd(2, 1))
print(movie_world.rent_dvd(1, 2))
print(movie_world)
