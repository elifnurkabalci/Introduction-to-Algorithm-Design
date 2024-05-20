class Store:
    def __init__(self, name, discount):
        self.name = name
        self.discount = discount

def calc_discount(stores):
    return sum(store.discount for store in stores)

def max_discount(stores, current_set=[], best_set=[], best_discount=0):
    # Base case: no more stores to visit
    if not stores:
        current_discount = calc_discount(current_set)
        # If the current set of stores gives a higher discount, update best_set and best_discount
        if current_discount > best_discount:
            return current_set, current_discount
        else:
            return best_set, best_discount

    # Recursive case: for each store, choose to visit or not visit
    for i in range(len(stores)):
        store = stores[i]
        remaining_stores = stores[i+1:]
        # Choose to visit the store
        new_set = current_set + [store]
        best_set, best_discount = max_discount(remaining_stores, new_set, best_set, best_discount)
        # Choose not to visit the store
        best_set, best_discount = max_discount(remaining_stores, current_set, best_set, best_discount)

    return best_set, best_discount

def main():
    stores = [Store('Store A', 10), Store('Store B', 20), Store('Store C', 30)]
    best_set, best_discount = max_discount(stores)
    print(f'The best set of stores to visit is: {[store.name for store in best_set]} with a total discount of {best_discount}')

if __name__ == "__main__":
    main()
