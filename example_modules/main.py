from Untitled_1 import *

def main():
        oper = input("1 - add 2 - show 3 - delete   -1 exit")
        while oper != "-1":
            user_data = input("-->")
            match oper:
                case "1":
                    2
                    Add(user_data)
                case "2":
                    Show(user_data)
                case "3":
                    Delete(user_data)
                case _:
                    print("dont understand")
            oper = input("1 - add 2 - show 3 - delete   -1 exit")


main()