import json


class SelfDrivingCarDto:
    id: int = None
    licence_plate: str = None
    type: int = None

    def __init__(self,id : int,licence_plate : str,type : int) -> None:
        self.id = id
        self.licence_plate = licence_plate
        self.type = type



car1 = SelfDrivingCarDto(1,'aaaa',0)
car2 = SelfDrivingCarDto(2,'bbb',0)

as_json = json.dumps([car1,car2], default = lambda x: x.__dict__)
print(as_json)