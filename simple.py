#a simple program for jenkins to test

def odd_or_even(num):
    return (("odd", "even")[num % 2 == 0])

if __name__ == "__main__":
    print("Application started.")
    print(f"The number 6 is {odd_or_even(6)}.")