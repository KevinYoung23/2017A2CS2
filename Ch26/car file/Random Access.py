# pickle.dump
# zhang chenyang Rex
import pickle
class CarRecord:
    def __init__(self,Name,Year,Price, Cylinder):
        self.Name = Name
        self.Year = Year
        self.Price = Price
        self.Cylinder = Cylinder
    def __repr__(self):
        return"(%s,%s,%s,%s)"%(self.Name, self.Year, self.Price, self.Cylinder)
def add():
    Name = ''; # name
    Year = ''; # year
    Price = '';
    Cylinder = ''# owner
    while Name == '' or len(Name) > 20:
        Name = input('name of car: ');
        if len(Name) > 20:
            print('maximum 20 characters');
    while Year == '' or len(Year) != 4:
        Year = input('year of purchase, must >= 2000');
        for i in Year:
            if i not in '1234567890':
                Year == '';
                print('incorrect format');
        if len(Year) != 4:
            print('please change a year');
    while Price == '' or len(Price) > 10:
        Price = input('price of car');
        if len(Price) > 10:
            print('maximum 10 characters');
    Cylinder = input('the numcer of Cylinder')

    return CarRecord(Name+(20-len(Name))*' ',int(Year),Price+(10-len(Price))*' ', Cylinder+(3-len(Cylinder))*' ');

def hashf(y):
    return y - 2000;

def save(car):
    file = open('Cars.dat','rb+');
    address = hashf(car.Year);
    address = address * 110 + 1;
    file.seek(address);
    pickle.dump(car,file);
    file.close();

def find(Year):
    file = open('Cars.dat','rb');
    address = hashf(Year) * 110 + 1;
    file.seek(address);
    c = pickle.load(file)
    print(c);
    file.close();

file = open('Cars.dat','wb');
file.close()
a = CarRecord('VW                  ',2002,'200000    ', '3  ');
b = CarRecord('Audi                ',2007,'350000    ', '4  ');
c = CarRecord('Mercedes            ',2006,'370000    ', '8  ');
d = CarRecord('BMW                 ',2015,'300000    ', '6  ');
e = CarRecord('Porsche             ',2012,'1200000   ', '12 ');
save(a);
save(b);
save(c);
save(d);
save(e);
find(2002);
find(2006);
find(2015);
find(2012);



