class SelfDrivingCar:
    id = None
    name = None

    def __init__(self,id,name) -> None:
        self.id = id
        self.name = name

    def __repr__(self) -> str:
        return "SelfDrivingCar(%d,%s)" % (self.id,self.name)


vehicles =[SelfDrivingCar(i,"sdc #%d" % i) for i in range(1,10)]
print(vehicles)
s = sorted(vehicles, key=lambda v: -v.id)
print(s)


