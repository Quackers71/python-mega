def weather_condition(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return "Cold"

tempIn = float(input("Enter a temperature :"))
print(weather_condition(tempIn))
