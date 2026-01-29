try:
    print("Trying risky operation")
    x = int("abc")

except ValueError:
    print("Conversion failed")

finally:
    print("This block always runs")
