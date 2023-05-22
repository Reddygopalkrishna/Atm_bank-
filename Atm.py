class Atm:
    def __init__(self, pin, balance):
        self.pin = pin
        self.balance = balance

    def display(self):
        print('Welcome to ABC bank atm')
        i = 0
        while i < 3:
            pin1 = int(input('Enter your pin :'))
            if pin1 != self.pin:
                print('Invalid pin!')
                i = i + 1

            else:
                print('Welcome to Home!')
                op = {1: 'Withdraw',
                      2: 'Deposit',
                      3: 'Balance Enquiry!',
                      4: 'Pin Change',
                      5: 'Amount Transfer',
                      6: 'Exit'}
                print(op)

                option = int(input('Select your option :'))
                if option == 1:
                    self.withdraw()
                    break
                elif option == 2:
                    self.deposit()
                    break
                elif option == 3:
                    self.balance_enquiry()
                    break
                elif option == 4:
                    self.pin_change()
                    break
                elif option == 5:
                    self.amount_transfer()
                    break
                elif option == 6:
                    print('Thank you for using ABC bank atm!')
                    break
                else:
                    print('Select valid option!')
                    break
            if i == 3:
                print('Sorry! You tried to login to many times. Try After sometime!')

    def withdraw(self):
        while True:
            withdraw_amount = int(input('How much amount you want to withdraw!$ :'))
            if self.balance >= withdraw_amount > 0:
                print(f'Take ${withdraw_amount}')
                self.balance = self.balance - withdraw_amount
                print(f'Remaining Balance {self.balance}$')
                print('Thank You!')
                break
            else:
                print('Insufficient Funds!')

    def deposit(self):
        while True:
            deposit_amount = int(input('How much you would like to deposit:$ '))
            if deposit_amount > 1000:
                self.balance = self.balance + deposit_amount
                print(f'Total Balance ${self.balance}')
                print('Thank you!')
                break

            else:
                print('Deposit Amount must be Above $1000!')

    def balance_enquiry(self):
        print(f'${self.balance} Balance')

    def pin_change(self):
        while True:
            old_pin = int(input('Enter your old pin :'))
            if old_pin != self.pin:
                print('Wrong pin!  Re-Enter the pin')

            else:
                while True:
                    new_pin = int(input('Enter your new pin :'))
                    if new_pin == old_pin:
                        print('New pin is same as previous pin!')

                    else:
                        while True:
                            new_pin1 = int(input('Enter again new pin :'))
                            if new_pin != new_pin1:
                                print('New pin is not equal to another new pin !')

                            else:
                                print('Pin Changed, Successfully!')
                                break
                        break
                break

    def amount_transfer(self):
        while True:
            account_num = int(input(' Account Number :'))
            if len(str(account_num)) == 11:
                transfer_amount = int(input('How much amount you want to transfer $'))
                if transfer_amount > self.balance:
                    print('Insufficient Funds!')
                else:
                    print(f'Transferd Successfully!')
                    self.balance = self.balance - transfer_amount
                    print(f'Your Current Balance is ${self.balance}')
                    break
            else:
                print('Invalid Account Number!')

def main():

    obj1 = Atm(123, 50000)
    obj1.display()
    print('Thank You! Visit Again')
if __name__ == '__main__':
    main()
