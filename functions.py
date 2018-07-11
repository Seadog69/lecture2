# functions.py

def square(x):
    return x * x

def main():
    for i in range(21):
        print(f"{i} ** 2 = {square(i)}")                # Python 3.6 and newer
        print("{} squared is {}".format(i, square(i)))  # prior to Python 3.6

# Trick to allow another module to call square without running all of the code in the module
if __name__ == "__main__" :
    main()