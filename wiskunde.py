import datetime

date = datetime.date(2023, 9, 8)

s = " "

text = "Gemaakt door Luka op de datum"

a = int(input("Wat is het totaal? "))

b = int(input("Wat is de hoeveelheid? "))

c = (360 / a) * (b)

print("")

print("de hoek is",c,"graden")

print("")

print(f'{text}{s}{date}')

