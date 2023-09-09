import datetime

date = datetime.date(2023, 9, 8)

s = " "

text = "Gemaakt door Luka op"

a = int(input("Wat is het totaal? "))

b = int(input("Wat is de hoeveelheid? "))

# noinspection PyRedundantParentheses
c = (360 / a) * (b)

print("")

print("de hoek is",c,"graden")

print("")

print(f'{text}{s}{date}')

from datetime import datetime

now = datetime.now()

dt_n = now.strftime("%Y-%m-%d %H:%M:%S")
print("Uitgevoerd op",dt_n)
