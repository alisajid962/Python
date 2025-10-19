from abc import ABC,abstractmethod
class Payment(ABC):
    @abstractmethod
    def process_payment(self,amount):
        pass
    def display_details(self):
        print(f"Proceeding your payment....")
class CreditCardPayment(Payment):
       def __init__(self,__cardnumber,__cardHolder):
            self.__cardnumber=__cardnumber
            self.__cardHolder=__cardHolder
            
       def getCardNumber(self):
            return self.__cardnumber[-4:]
       def setCardNumber(self,cardnumber):
            if len(cardnumber)==5:
                 self.__cardnumber=cardnumber
            else:
                 print("Suspicious Activity Detecetd...Contact Bank Your Account is Frozen...............")
       def process_payment(self, amount):
            print(f"Payment of {amount} made through Credit Card of {self.__cardHolder} ending with {self.getCardNumber()}.")
        
       

        
       
class PayPalPayment(Payment):
       def __init__(self,cardnumber,cardHolder):
            self.__cardnumber=cardnumber
            self.__cardHolder=cardHolder
            
       def process_payment(self, amount):
            print(f"Payment of {amount} made through PayPal of MR. {self.__cardHolder} using card {self.getCardNumber()} .")
        
       def getCardNumber(self):
            return self.__cardnumber
       
       def setCardNumber(self,cardnumber):
            if len(cardnumber)==5:
                 self.__cardnumber=cardnumber
            else:
                 print("Suspicious Activity Detecetd...Contact Bank Your Account is Frozen...............")

card=CreditCardPayment("123456789987","Ali Sajid")
card.process_payment(5000)
card.setCardNumber("51010")
card.process_payment(6000)

paypalaccount=PayPalPayment("1202020202020202022","Zain")
paypalaccount.process_payment(1282828282)
paypalaccount.setCardNumber("12345")
paypalaccount.process_payment(1282828282)


        
       

            


