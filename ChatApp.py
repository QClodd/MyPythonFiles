class User:
    """This class is for making your users."""
    def __init__(self,username):
        """Function for setting name of user."""
        self.username = username    #variable of user's name

class Chatting(User):
    """Class for loops etc."""
    @staticmethod
    def chat(inst1,inst2):
        """Main engine of chatapp.py ... here are many conditions so check them."""
        mainflow = True #variable for conditions
        while mainflow:
            inst1_message = input("%s : " % inst1.username) #input for writing messages
            inst2_message = False           #same,but for second instance
            if inst1_message == "\end":
                print("User %s has disconnected." % inst1.username)
                break

            if inst1_message == "\more":
                flow_inst1 = True           #flow for first instance
                while flow_inst1:
                    inst1_another_message = input("%s : " % inst1.username) #another input for first instance
                    if inst1_another_message == "\endmore":
                        flow_inst1 = False
                    elif inst1_another_message == "\end":
                        print("User %s has disconnected." % inst1.username)
                        mainflow = False
                        flow_inst1 = False
                        break

            if mainflow:
                inst2_message = input("%s : " % inst2.username)
                if inst2_message == "\end":
                    print("User %s has disconnected." % inst2.username)
                    break

            if inst2_message == "\more" and mainflow is True:
                flow_inst2 = True
                while flow_inst2:
                    inst2_another_message = input("%s : " % inst2.username)
                    if inst2_another_message == "\endmore":
                        flow_inst2 = False

                    elif inst2_another_message == "\end":
                        print("User %s has disconnected." % inst2.username)
                        mainflow = False
                        break
                        

if __name__ == "__main__":
    john = User("John") #Settign names here
    mark = User("Mark")
    Chatting.chat(john,mark) #Execution of whole application
    
