def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    temp = float(input("Enter temperature in Farenheit: "))
    converted_temp = fahrenheit_to_celsius(temp)
    print(f"{temp}°F is {converted_temp:.2f}°C")

if __name__ == "__main__":
    main()