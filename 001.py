class Kettle(object):

    power_source = "Electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)


kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)

print("{} = {}    {} = {} ".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))

print("{0.make} = {0.price}    {1.make} = {1.price} ".format(kenwood, hamilton))

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)


print(kenwood.on)
kenwood.switch_on()

print("*" * 80)

kenwood.power = 1.5

print(kenwood.power)
#print(hamilton.power)

print("Switch to atomic power")
Kettle.power_source = "atomic"
print(Kettle.power_source)
print("Switch kenwood to gas")
kenwood.power_source = "Gas"
print(kenwood.power_source)
print("Switch Hamilton to water")
hamilton.power_source = "water"
print(hamilton.power_source)
print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)