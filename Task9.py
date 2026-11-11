numbers = [10, 20, 30, 40]

while True:
    try:
        index = int(input("Enter an index number: "))
        value = numbers[index]         
        divisor = int(input("Enter a divisor: "))
        result = value / divisor
        print("Result:", result)
        break                           
    except ValueError:
        print("Error: please enter a whole number, not text. Try again.\n")
    except IndexError:
        print("Error: the index must be between 0 and", len(numbers) - 1, "- try again.\n")
    except ZeroDivisionError:
        print("Error: you cannot divide by zero. Try again.\n")
    except Exception as e:
        print("An unexpected error occurred:", e, "- try again.\n")
    