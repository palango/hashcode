f = open("busy_day.in","r")
commandList = []
#Parameters of simulation
[nRows,nCols,nDrones,deadlineOfSimulation,maxLoad]=[int(i) for i in f.readline().split()]

#weights of the products available for orders
nProducts=int(f.readline())
productWeights = [int(i) for i in f.readline().split()]

#warehouses and availability of individual product types 
nWarehouses=int(f.readline())
warehouseList = []
for iWarehouse in xrange(nWarehouses):
	location = (int(i) for i in f.readline().split())
	items = [int(i) for i in f.readline().split()]
	#TODO create a warehouse and put in list
	warehouse = [location, items]
	warehouseList.append(warehouse)


#customer orders
nOrders=int(f.readline())
orderList = []
for iWarehouse in xrange(nWarehouses):
	location = (int(i) for i in f.readline().split())
	nOrderedProducts = nOrders=int(f.readline())
	items = [int(i) for i in f.readline().split()]
	#TODO create a warehouse and put in list
	order = [location, items]
	orderList.append(order)

