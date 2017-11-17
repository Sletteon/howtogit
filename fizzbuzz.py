def buzz():
    for i in range(101):
        if i%4==0:
            print("buzz")
        else:
            print(i)
def fizz():
    for i in range(101):
        if i%3==0:
            print("fizz")
        else:
            print(i)
def main():
    fizz();
    buzz();
if __name__=='__main__':
        main()
