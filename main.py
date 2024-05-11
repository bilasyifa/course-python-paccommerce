from tabulate import tabulate
from math import sqrt

class Membership:
    # Initialize data
    data = {
        "Sumbul": "Platinum",
        "Ana": "Gold",
        "Cahya": "Platinum"
    }

    # Initialize class attribute
    def __init__(self, username: str) -> None:
        self.username = username
    

    def show_benefits(self) -> None:
        '''
        A method for displaying existing benefits in PacCommerce for each membership tier.
        '''
        # Initialize header's name of benefits
        headers = ["Membership", "Discount", "Benefits"]

        # Initialize benefits data of membership
        tables = [
            ["Platinum", "15%", "Benefit Silver + Gold + Voucher Liburan + Cashback max. 30%"],
            ["Gold", "10%", "Benefit Silver + Voucher Ojek Online"],
            ["Silver", "8%", "Voucher Makanan"]
        ]

        print("Benefits PacCommerce Membership")
        print("")
        print(tabulate(tables, headers, tablefmt="github"))

    def show_requirements(self) -> None:
        '''
        A method for displaying the Monthly Expense and Monthly Income requirements of each membership tier.
        '''
        # Initialize header's name of requirements
        headers = ["Membership", "Monthly Expense (juta)", "Monthly Income (juta)"]

        # Initialize requirements data of membership
        tables = [
            ["Platinum", 8, 15],
            ["Gold", 6, 10],
            ["Silver", 4, 7]
        ]

        print("Requirements PacCommerce Membership")
        print("")
        print(tabulate(tables, headers, tablefmt="github"))
    
    def predict_membership(self, username: str,
                           monthly_expense: float,
                           monthly_income: float) -> None:
        '''
        A method for predicting a user's membership tier using Euclidean distance.

        Parameter
        ---------
        username (str): username from user
        monthly_expense (float): user monthly expense in million format
        monthly_income (floar): user monthly income in million format 
        '''
        # Initialize parameter data of each membership tier
        parameter_data = [[8, 15], [6, 10], [5, 7]]

        result_tmp = []
        
        # Calculate the Euclidean distance for each membership tier
        for idx, _ in enumerate(parameter_data):

            if monthly_expense < monthly_income:
                euclidean_dist = round(sqrt((monthly_expense - parameter_data[idx][0])**2 + \
                                            (monthly_income - parameter_data[idx][1])**2), 2)
                
                result_tmp.append(euclidean_dist)
            
            else:
                raise Exception("Monthly Income must be greater than Monthly Expense")
        
        # Store the Euclidean distance to a dictionary
        dict_result = {
            "Platinum": result_tmp[0],
            "Gold": result_tmp[1],
            "Silver": result_tmp[2]
        }
        
        print(f"The results of calculating the Euclidean distance from user {username} are {dict_result}")

        # Get the minimum distance from result_tmp list
        min_distance = min(result_tmp)
        
        # Iterate to dict_result dictionary
        for key, value in dict_result.items():
            # Compare with minimum distance
            if value == min_distance:
                print(key)

                # Store predicted data to data dictionary
                self.data[username] = key
            
            else:
                pass

    def calculate_price(self, username: str, list_price: list) -> float:
        '''
        A method for calculating total price based on its membership tier.

        Parameter
        ---------
        username (str): existing user username
        price_list (list): user shopping price

        Return
        ------
        total_price (float): user total price
        '''
        # Get membership tier
        if username in self.data:
            membership = self.data.get(username)

            # Create branching loops for each membership tier to get discount
            if membership == "Platinum":
                total_price = sum(list_price) - (sum(list_price) * 0.15)
                return total_price
            elif membership == "Gold":
                total_price = sum(list_price) - (sum(list_price) * 0.10)
                return total_price
            elif membership == "Silver":
                total_price = sum(list_price) - (sum(list_price) * 0.08)
                return total_price
            else:
                raise Exception("Membership has not been identified")
        
        else:
            raise Exception("Member is still not registered in the Database")
        

## Test Case 1
user_1 = Membership("Salsa")
user_1.show_benefits()

## Test Case 2
user_1.show_requirements()

## Test Case 3
user_1.predict_membership(user_1.username, 9, 12)

# Display the new member data
user_1.data

# Display the Membership tier by username
user_1.data["Salsa"]

## Test Case 4
user_1.calculate_price(user_1.username, [150_000, 200_000, 400_000])

## Another Test Case 1
# Use existing user Ana in the database
user_2 = Membership("Ana")
user_2.data

## Another Test Case 2
# Use another username Bambang
user_3 = Membership("Bambang")
user_3.show_benefits()
user_3.show_requirements()
user_3.predict_membership(user_3.username, 3, 4)
user_3.calculate_price(user_3.username, [300_000, 150_000, 1_250_000, 15_000])
user_3.data
