class CartStore:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(CartStore, cls).__new__(cls)
            cls.__instance.cart = {}
        return cls.__instance

    def add_plan_to_cart(self, plan_id):
        if plan_id not in self.cart:
            self.cart[plan_id] = 1
        else:
            self.cart[plan_id] += 1

    def remove_plan_from_cart(self, plan_id):
        if plan_id not in self.cart:
            return False
        if self.cart[plan_id] == 1:
            del self.cart[plan_id]
        else:
            self.cart[plan_id] -= 1
        return True

    def get_cart_contents(self):
        return self.cart
