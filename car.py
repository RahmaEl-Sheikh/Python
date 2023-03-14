class Car:
    make=""
    model=""
    year=2005
    mileage=0
    def __init__(self,make,model,year,mileage):
        self.make=make
        self.model=model
        self.year=year
        self.mileage=mileage
        
    def drive(self,perc):
        mile=(self.mileage)+perc
        print("your mile age increased by value = %.2f and your total mileage is = %.2f" %(perc,mile))
        
c1=Car("daweo","lanos",2010,20)
c1.drive(10)