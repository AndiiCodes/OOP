class SmartphoneApp:
    @staticmethod

    def main():
        battery = 100
        
        print(f"Your battery is at {battery}%")
        phoneNumber = input("Enter the phone number you want to call: ")
        first_two_digits = phoneNumber[:2]
           
        if battery < 5 or battery < 0:
            print("Your battery is low. Please charge your phone")
        elif not phoneNumber.isdigit():
            print("Please entter a valid phone number. Only numerical values are allowed.")
        elif len(phoneNumber) > 10 or len(phoneNumber) < 10:
            print("Incorrect number. Please enter a valid 10 digit phone number")
        elif first_two_digits != "04":
            print("Incorrect area code. Area code should start with 04.")

        else:
            print(f"Calling {phoneNumber}...")
            print(f"Your battery is at {battery - 5}%")
        
SmartphoneApp.main()

