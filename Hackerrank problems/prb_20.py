def deal(dealerships):
    tyres=[]
    for dealership in dealerships:
        car, bikes = dealership
        total_tyres = (car * 4) + (bikes * 2)
        tyres.append(total_tyres)
    return tyres

dealerships = [(4,2),(4,0),(1,2)]
tyre = deal(dealerships)
print(tyre)