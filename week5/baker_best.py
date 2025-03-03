F, D = map(int, input().split())

bonus = 0
franchise_totals = [0] * F

for _ in range(D):
    sales = list(map(int, input().split()))
    day_total = sum(sales)
    if day_total % 13 == 0:
        bonus += day_total // 13
    for i, sale in enumerate(sales):
        franchise_totals[i] += sale
        
for total in franchise_totals:
    if total % 13 == 0:
        bonus += total // 13

print(bonus)