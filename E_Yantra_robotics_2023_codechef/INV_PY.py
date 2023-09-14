
def manage_inventory(initial_items, operations):
    inventory = {}

    for item in initial_items:
        item_name, item_quantity = item.split()
        inventory[item_name] = int(item_quantity)

    for operation in operations:
        operation_name, item_name, quantity = operation.split()
        if operation_name == "ADD":
            if item_name in inventory:
                print(f"UPDATED Item {item_name}")
                inventory[item_name] += int(quantity)
            else:
                print(f"ADDED Item {item_name}")
                inventory[item_name] = int(quantity)
        elif operation_name == "DELETE":
            if item_name not in inventory:
                print(f"Item {item_name} does not exist")
            elif inventory[item_name] < int(quantity):
                print(f"Item {item_name} could not be DELETED")
            else:
                print(f"DELETED Item {item_name}")
                inventory[item_name] -= int(quantity)

    total_quantity = sum(inventory.values())
    print(f"Total Items in Inventory: {total_quantity}")

# Main function
if __name__ == "__main__":
    T = int(input()) 

    for _ in range(T):
        N = int(input()) 
        initial_items = [input() for _ in range(N)]

        M = int(input())  
        operations = [input() for _ in range(M)]

      
        manage_inventory(initial_items, operations)

