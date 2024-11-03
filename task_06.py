items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    total_calories = 0
    selected_items = []
    
    for item, properties in sorted_items:
        if budget >= properties["cost"]:
            budget -= properties["cost"]
            total_calories += properties["calories"]
            selected_items.append(item)
    
    return selected_items, total_calories


budget = 100
selected_items, total_calories = greedy_algorithm(items, budget)
print("Вибрані страви:", selected_items)
print("Сумарна калорійність:", total_calories)
