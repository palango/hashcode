from models import *
import math

def getDistance(location1,location2):
    euclidDist = math.sqrt((location1[0]-location2[0])**2+(location1[1]-location2[1])**2)
    return math.ceil(euclidDist)

f = open("example.in","r")
commandList = []
#Parameters of simulation
[nRows,nCols,nDrones,maxSteps,maxLoad]=[int(i) for i in f.readline().split()]

#weights of the products available for orders
nTypes=int(f.readline())
productWeights = [int(i) for i in f.readline().split()]

#warehouses and availability of individual product types 
nWarehouses=int(f.readline())
warehouseList = []
for iWarehouse in xrange(nWarehouses):
    location = (int(i) for i in f.readline().split())
    items = [int(i) for i in f.readline().split()]
    warehouse = Warehouse(items,location)
    warehouseList.append(warehouse)

#customer orders
nOrders=int(f.readline())
orderList = []
for iWarehouse in xrange(nWarehouses):
    location = (int(i) for i in f.readline().split())
    nOrderedProducts = int(f.readline())
    items = [int(i) for i in f.readline().split()]
    warehouseDistances = [(getDistance(location, warehouseList[i].location),i) for iWarehouse in range(nWarehouses)]
    warehouseDistances = warehouseDistances.sort() 
    order = Order(items,location,warehouseDistances)
    orderList.append(order)

#Create drones
droneList = [Drone(warehouseList[0].location, maxLoad, nTypes) for i in range(nDrones)]

#World
for iStep in xrange(maxSteps):
    #do all jobs pending and find free drones
    freeDronesIdx = []
    for iDrone in xrange(nDrones):
        if droneList[iDrone].finishedAt == iStep+1:
            print("Do job")
        elif droneList[iDrone].finishedAt == iStep:
            freeDronesIdx.append(iDrone)
    #assign jobs to free drones
    



def easyOrders(orders,warehouses):
        for order in orders:
                return
