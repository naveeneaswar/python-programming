def main():
    pass
a=int(input("Enter number: "))
if(a>1):
    for i in range(2,a):
        if(a%i==0):
            print("no")
            break
    else:
            print("yes")
else:
    print("not a prime")

if __name__ == '__main__':
    main()
