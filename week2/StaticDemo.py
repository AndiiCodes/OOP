class StaticDemo:
    @staticmethod
    def main():
        mobile_number = input("Enter your mobile number: ")
        print(type(mobile_number))
        if not mobile_number.isdigit():
            print("Error: Invalid mobile number. Only numerical values are allowed.")
            return  # Exit the program
        
        print("This is a static function. The code below can be called/invoked without creating an object of the class")
        print("Static function will be used during the classes this week and for the next couple of weeks")
        print("Hello there")
        print("Enjoy the week")

StaticDemo.main()