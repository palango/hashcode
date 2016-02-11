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
    location = tuple([int(i) for i in f.readline().split()])
    items = [int(i) for i in f.readline().split()]
    warehouse = Warehouse(items,location)
    warehouseList.append(warehouse)

#customer orders
nOrders=int(f.readline())
orderList = []
for iOrder in xrange(nOrders):
    location = tuple([int(i) for i in f.readline().split()])
    nOrderedProducts = int(f.readline())
    tmpItems = [int(i) for i in f.readline().split()]
    items = [tmpItems.count(i) for i in range(nTypes)]
    warehouseDistances = [(getDistance(location, warehouseList[i].location),i) for i in range(nWarehouses)]
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

def orderWeight(order):
    sum = 0
    for i in range(len(order.items)):
        sum += order.items[i] * productWeights[i]
    return sum
    
def easyOrders(orders,warehouses):
    easy = []
    for oidx, order in orders.enumerate():
        if orderWeight(order) < maxLoad:
            for widx, warehouse in warehouses.enumerate():
                if order.is_ready_at(warehouse):
                    easy.append((oidx, widx))
                    break
