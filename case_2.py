from tabulate import tabulate

class MembershipUser():
    me_platinum = 8
    me_gold = 6
    me_silver = 5
    mi_platinum = 15
    mi_gold = 10
    mi_silver = 7


    def __init__(self, username, monthly_expense, monthly_income):
        self.username = username
        self.monthly_expense = monthly_expense
        self.monthly_income = monthly_income

    def show_benefit(self):
        table = [['Platinum', '15%', 'Benefit from Silver and Gold + Cashback max. 30%'],
                 ['Gold', '10%', 'Benefit from Silver + Voucher Ojek Online'],
                 ['Silver', '8%','Voucher makanan']
                 ]
        
        headers = [['Membership', 'Discount', 'Another benefit']]

        print('Benefit Membership PacCommerce')
        print('')
        print(tabulate(table, headers))

    def show_requirements(self):
        table = [['Platinum', '8', '15'],
                 ['Gold', '6', '10'],
                 ['Silver', '5', '7']
                 ]

        headers =[['Membership', 'Monthly Expense (million)', 'Monthly Income (Million)']]

        print('Requirements Membership PacCommerce')
        print('')
        print(tabulate(table, headers))
    
    def predict_membership(self):
        user_platinum = (((self.monthly_expense-self.me_platinum)**2)+((self.monthly_income-self.mi_platinum)**2))**0.5
        user_gold = (((self.monthly_expense-self.me_gold)**2)+((self.monthly_income-self.mi_gold)**2))**0.5
        user_silver = (((self.monthly_expense-self.me_silver)**2)+((self.monthly_income-self.mi_silver)**2))**0.5
        
        if user_platinum<user_gold and user_platinum<user_silver:
            membership = "Platinum"
            return membership

        elif user_gold<user_platinum and user_gold<user_silver:
            membership = 'Gold'
            return membership
        
        elif user_silver<user_gold and user_silver<user_platinum:
            membership = 'Silver'
            return membership

    def calculate_price(self, list_harga_barang):
        category = self.predict_membership()

        if category == 'Platinum':
            total_price = (sum(list_harga_barang))-(sum(list_harga_barang)*0.15)
            print(total_price)

        elif category == 'Gold':
            total_price = (sum(list_harga_barang))-(sum(list_harga_barang)*0.1)
            print(total_price)

        elif category == 'Silver':
            self.total_price = (sum(list_harga_barang))-(sum(list_harga_barang)*0.05)
            print(total_price)



# Cek Kode
user_1 = MembershipUser('Sumbul', 9, 16)
user_2 = MembershipUser('Ana', 6, 9)
user_3 = MembershipUser('Cahya', 5, 12)
user_4 = MembershipUser('Shandy', 7, 11)

# Case 1

# Case 2
print(user_2.predict_membership())
print(user_2.calculate_price([300_000, 150_000, 140_000]))

# Case 3
print(user_3.predict_membership())
print(user_3.calculate_price([250_000, 200_000, 100_000]))

# Case 4
print(user_4.predict_membership())
print(user_4.calculate_price([100_000, 100_000, 125_000]))