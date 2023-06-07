import math

# فاصله بین دو شهر را محاسبه می‌کند
def distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# الگوریتم تپه‌نوردی برای جستجوی بهینه
def hill_climbing(start_city, goal_city, cities):
    current_city = start_city
    path = [current_city]

    while current_city != goal_city:
        neighbors = []

        # یافتن همسایگان شهر فعلی
        for city in cities:
            if city != current_city:
                neighbors.append(city)

        # محاسبه فاصله شهرهای همسایه تا شهر هدف
        distances = [distance(neighbor, goal_city) for neighbor in neighbors]

        # پیدا کردن شهری که فاصله آن کمتر است
        best_neighbor = neighbors[distances.index(min(distances))]

        # اگر فاصله بهترین همسایه کمتر از فاصله شهر فعلی باشد، به همسایه برس
        if distance(best_neighbor, goal_city) < distance(current_city, goal_city):
            current_city = best_neighbor
            path.append(current_city)
        else:
            # اگر هیچ همسایه‌ای با فاصله کمتری پیدا نشد، به مسیر قبلی برگرد
            path.pop()
            current_city = path[-1]

    return path

# مثال اجرای الگوریتم
cities = [(0, 0), (1, 5), (3, 2), (7, 4), (9, 1)]  # مختصات شهرها
start_city = (0, 0)  # شهر شروع
goal_city = (9, 1)  # شهر هدف

optimal_path = hill_climbing(start_city, goal_city, cities)
print(optimal_path)
