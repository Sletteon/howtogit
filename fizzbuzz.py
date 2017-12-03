# !/usr/bin/env python
def fizzbuzz():
    for i in range(101):
        if i%4==0:
            print("buzz")
        if i%3==0:
            print("fizz")
        if i%12==0:
            print("fizzbuzz")
        else:
             print(i)
def main():
     fizzbuzz();
if __name__=='__main__':
         main()

