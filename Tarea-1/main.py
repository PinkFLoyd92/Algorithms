
def main():
    description = ""
    n =-1
    while (n<0 or n>1000):
        n= input("Type a number between 0 and 1000: ")
        n=int(n)
        # World Cup 1998 - Group A
    for x in range(0,n):
        while (len(description)<5 or len(description)>100 or ('-' not in description)):
            description = input("Enter the Cup name and the group names.")
            if('-' not in description):
                print("Missing separator: -")
            if(len(description)<5 or len(description)>100):
                print("wrong range, please enter a string with more than 5 characters.")
        
        
        
        
if __name__ == '__main__':
    main()
