#TempConvert.py
#Name:Arturo
#Date:2/9/2025
#Assignment:Temp Convert


def main():
  #Prompt the user for a Fahrenheit temperature
  #Convert that temperature to celsius, rounding to 1 decimal percision
  #Output converted temperature.
  tempF = input("Enter a degree in Fahrenheit: ")

  tempC = (int(tempF)-32) / 1.8

  tempC = round(tempC, 2)
  
  
  print(tempF, "is ", tempC, "degrees celsius.")

if __name__ == '__main__':
  main()
