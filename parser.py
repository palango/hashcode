from models import *
from logger import Logger
import math
import copy

log = Logger()

def getDistance(location1, location2):
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
    #freeDronesIdx = []
    availableOrders = easyOrders(orderList,warehouseList)
    for iDrone in xrange(nDrones):
        if droneList[iDrone].finishedAt == iStep:
            warehouseDistances = [(getDistance(droneList[iDrone].location, warehouseList[i].location),i) for i in range(nWarehouses)]
            warehouseDistances = warehouseDistances.sort()
            #Find order idx for drone, starting by looking at the closest warehouse
            for i in xrange(nWarehouses):
                preferredWarehouseIdx = warehouseDistances[i][1]
                orderIdx = None
                for availableOrder in availableOrders:
                    if(availableOrder[1]==preferredWarehouseIdx):
                        orderIdx = availableOrder[0]
                        break
                if orderIdx is not None:
                    break
            #Handle order for drone
            currentOrder = orderList[orderIdx]
            for itemIdx in xrange(len(currentOrder.items)):
                itemcount = currentOrder.items[itemIdx]
                if itemcount > 0:
                    droneList[iDrone].load(itemcount, itemIdx, warehouseList[preferredWarehouseIdx])
                    #TODO create command in logger
                    commandDict = {
                        'name' : 'load',
                        'drone_id' : iDrone,
                        'warehouse_id' : preferredWarehouseIdx,
                        'prod_id' : itemIdx,
                        'prod_count' : itemcount
                    }
                    log.append_command(droneList[iDrone].finishedAt, commandDict)
            for itemIdx in xrange(len(currentOrder.items)):
                itemcount = currentOrder.items[itemIdx]
                if itemcount > 0:
                    droneList[iDrone].deliver(itemcount, itemIdx, order[orderIdx])
                    #TODO create command in logger
                    commandDict = {
                        'name' : 'deliver',
                        'drone_id' : iDrone,
                        'order_id' : orderIdx,
                        'prod_id' : itemIdx,
                        'prod_count' : itemcount
                    }
                    log.append_command(droneList[iDrone].finishedAt, commandDict)

            #update available orders
            #availableOrders = easyOrders(orderList,warehouseList)

def orderWeight(order):
    sum = 0
    for i in range(len(order.items)):
        sum += order.items[i] * productWeights[i]
    return sum
    
def easyOrders(orders,warehouses):
    easy = []
    wh = copy.deepcopy(warehouses)
    for oidx, order in orders.enumerate():
        if orderWeight(order) < maxLoad:
            for widx in order.warehouseDistances:
                if order.is_ready_at(wh[widx]):
                    easy.append((oidx, widx))
                    for i in range(len(wh[widx].stock)):
                        wh[widx].stock[i] -= order.items[i]
                    break
