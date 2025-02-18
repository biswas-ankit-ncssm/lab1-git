import sys

def money_to_num(mon):
    return int(float(mon[1:])*100)

def error_checking(mon):
    if mon[0] != '$':
        print("ERROR: The string must begin with a $")
        return False
    elif len(mon[1:].split('.')) != 2:
        print("ERROR: The string must include a dollar amount")
        return False
    return True

def return_statement(cash):
    quarters = cash // 25
    if quarters > 0:
        print(f"{quarters} quarters")
        cash -= quarters*25
    dimes = cash // 10
    if dimes > 0:
        print(f"{dimes} dimes")
        cash -= dimes*10
    nickels = cash // 5
    if dimes > 0:
        print(f"{nickels} nickels")
        cash -= nickels*5
    if cash > 0:
        print(f"{cash} pennies")

def main():
    mon = sys.argv[1]
    if error_checking(mon):
        cash = money_to_num(mon)
        return_statement(cash)
    
if __name__=="__main__":
    main()
