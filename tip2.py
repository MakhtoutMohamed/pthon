name = input("what's your name?\n")

total = int(float(input("what's your bill sub-total?\n").replace('$','')))

tip_15 = total * 0.15
tip_18 = total * 0.18
tip_20 = total * 0.20

print("your name is:",name)
print("your bill sub-total is:",total)
print(f"15% is ${tip_15:.2f}")
print(f"18% is ${tip_18:.2f}")
print(f"20% is ${tip_20:.2f}")