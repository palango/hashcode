class Order:
    def __init__(self, items, location):
        self.items = items
        self.location = location


def is_ready_at(warehouse):
    for idx, req_item in self.items.enumerate():
        if warehouse.stock[idx] >= req_item:
            return False
    return True
