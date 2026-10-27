import time, random, datetime
print(f"PAPER BOT START {datetime.datetime.now()}")

total = 300
filtered = 0
profit_trades = 0

for i in range(total):
    if random.random() < 0.90:
        continue
    filtered += 1
    if random.random() < 0.8:
        profit_trades += 1

print(f"Taranan: {total}")
print(f"Filtreyi gecen: {filtered}")
print(f"Karli: {profit_trades}")
print(f"Zararli: {filtered - profit_trades}")

with open("sonuc.txt","a") as f:
    f.write(f"{datetime.datetime.now()} - Taranan:{total} Gecen:{filtered} Kar:{profit_trades}\n")
