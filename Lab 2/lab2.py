import matplotlib.pyplot as plt

# Функція для зчитування координат із файлу
def read_coordinates(file_name):
    coordinates = []
    try:
        with open(file_name, "r") as file:
            for line in file:
                x, y = map(int, line.split())  # Розділяємо і перетворюємо в числа
                coordinates.append((x, y))
    except FileNotFoundError:
        print(f"Файл {file_name} не знайдено!")
        return []
    return coordinates

# Основна функція для побудови графіка
def plot_points(points, canvas_size=(960, 540), output_file="output_image.png"):
    if not points:
        print("Список точок порожній, нічого виводити.")
        return

    # Створюємо полотно з правильними розмірами
    width, height = canvas_size
    plt.figure(figsize=(width/100, height/100), dpi=100)

    # Розпаковуємо координати
    x_coords, y_coords = zip(*points)
    
    # Створюємо графік 
    plt.scatter(x_coords, y_coords, 
               c='blue',
               s=10, 
               alpha=0.6,
               label=f"Точки ({len(points)})")

    plt.title("Візуалізація координат точок", pad=15)
    plt.xlabel("X-координата")
    plt.ylabel("Y-координата")
    
    # Додаємо сітку 
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()

    # Додаємо відступи пропорційно до діапазону даних
    x_range = max(x_coords) - min(x_coords)
    y_range = max(y_coords) - min(y_coords)
    padding_x = x_range * 0.05  # 5% відступ
    padding_y = y_range * 0.05
    
    plt.xlim(min(x_coords) - padding_x, max(x_coords) + padding_x)
    plt.ylim(min(y_coords) - padding_y, max(y_coords) + padding_y)

    # Зберігаємо результат
    try:
        plt.savefig(output_file, 
                   bbox_inches='tight', 
                   dpi=100,
                   facecolor='white',
                   edgecolor='none')
        print(f"Графік успішно збережено у файл: {output_file}")
    except Exception as e:
        print(f"Помилка при збереженні файлу: {e}")
    
    plt.show()
    
    plt.close()

file_name = "DS1.txt"
points = read_coordinates(file_name)
plot_points(points)
