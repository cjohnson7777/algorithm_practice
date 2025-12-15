from abc import ABC, abstractmethod

# PAYMENT STRATEGY
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self):
        pass

# PayPal Strategy
class PayPalStrategy(PaymentStrategy):
    def pay(self, price):
        print(f"Using PayPal for payment of {price}")

# Credit Card Strategy
class CreditCardStrategy(PaymentStrategy):
    def pay(self, price):
        print(f"Using Credit Card for payment of {price}")

# Cash Strategy
class CashStrategy(PaymentStrategy):
    def pay(self, price):
        print(f"Using Cash for payment of {price}")

# CONTEXT

class CheckOut:
    def __init__(self, price, paymentStrategy):
        self.price = price
        self.paymentStrategy = paymentStrategy
    
    def checkout(self):
        self.paymentStrategy.pay(self.price)

order = CheckOut(3, PayPalStrategy())
order.checkout()