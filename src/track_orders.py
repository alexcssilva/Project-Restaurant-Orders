from collections import Counter


class TrackOrders:
    def __init__(self):
        self._queue = []
    # aqui deve expor a quantidade de estoque

    def __len__(self):
        return len(self._queue)

    def add_new_order(self, customer, order, day):
        self._queue.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        orders_list = []
        for custom, order, day in self._queue:
            if custom == customer:
                orders_list.append(order)

        orders_statistics = Counter(orders_list)
        most_order = orders_statistics.most_common()

        return most_order[0][0]

    def get_never_ordered_per_customer(self, customer):
        list_orders = set()
        total_orders = set()

        for custom, order, day in self._queue:
            total_orders.add(order)
            if custom == customer:
                list_orders.add(order)
        result = total_orders - list_orders

        return result

    def get_days_never_visited_per_customer(self, customer):
        list_days = set()
        total_days = set()

        for custom, order, day in self._queue:
            total_days.add(day)
            if custom == customer:
                list_days.add(day)
        result = total_days - list_days

        return result

    def get_busiest_day(self):
        list_days = []

        for customer, order, day in self._queue:
            if customer == customer:
                list_days.append(day)

        return max(list_days, key=list_days.count)

    def get_least_busy_day(self):
        list_days = []

        for customer, order, day in self._queue:
            if customer == customer:
                list_days.append(day)

        return min(list_days, key=list_days.count)
