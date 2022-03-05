import car
from saveservice import SaveService
from collectionservice import CollectionService

def main():
    
    #create
    marka=input("podaj markę pojazdu: ")
    rok=int(input("podaj rocznik pojazdu: "))
    przebieg=int(input("podaj przebieg pojazdu: "))

    c1=car.Car(marka, rok, przebieg)
    c2 = car.Car("volkswagen",2020,50000)

    cs = CollectionService()
    cs.Add(c1)
    cs.Add(c2)

    #save
    SaveService.save("data.txt",c1)
    SaveService.save("data.txt",c2)

    #read
    x = SaveService.deserialize("data.txt")
    print(x.marka)
    print(x.rok)
    print(x.przebieg)

    #delete
    cs.Delete(c1)
    cs.Show()


if __name__=="__main__":
    main()