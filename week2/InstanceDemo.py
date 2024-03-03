class InstanceDemo: # creating a class
    def demo(): # creating an instance function
        print("This is an instance function. The code below can only be called/invoked by creating an object of the class")
        print("Instance function will be used during the classes later in the semester when covering the topics for object-oriented programming (OOP)")
        print("Hello there")
        print("Enjoy the week")

obj = InstanceDemo() # creating an object of the class
InstanceDemo.demo() # calling/invoking the instance function using the object of the class