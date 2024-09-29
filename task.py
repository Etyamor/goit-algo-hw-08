import heapq


def min_cost_to_connect_cables(cables):
    # Створюємо купу з масиву довжин кабелів
    heapq.heapify(cables)
    total_cost = 0

    # Поки в купі більше одного елемента
    while len(cables) > 1:
        # Витягуємо два найкоротші кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        # Вартість їх об'єднання
        cost = first + second
        total_cost += cost
        # Додаємо об'єднаний кабель назад в купу
        heapq.heappush(cables, cost)
    return total_cost


cables = [4, 3, 2, 6]
min_cost = min_cost_to_connect_cables(cables)
print(f"Мінімальні витрати на з'єднання кабелів: {min_cost}")
