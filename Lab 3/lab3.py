import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull
import numpy as np

# Функція для зчитування координат із файлу
def read_coordinates(file_name):
    try:
        points = np.loadtxt(file_name, dtype=int)
        return points
    except FileNotFoundError:
        print(f"Файл {file_name} не знайдено!")
        return np.array([])

# Функція для збереження опуклої оболонки у новий датасет
def save_convex_hull(hull_points, output_file="convex_hull.txt"):
    try:
        np.savetxt(output_file, hull_points, fmt='%d %.8f')
        print(f"Опуклу оболонку збережено у файл: {output_file}")
    except Exception as e:
        print(f"Помилка при збереженні опуклої оболонки: {e}")

# Функція для побудови графіка
def plot_with_convex_hull(points, hull_indices, canvas_size=(960, 540), output_file="output_image.png"):
    if points.size == 0:
        print("Список точок порожній, нічого виводити.")
        return

    # Отримуємо точки опуклої оболонки за індексами
    hull_points = points[hull_indices]
    hull_points = np.vstack((hull_points, hull_points[0]))  

    # Створюємо полотно
    fig, ax = plt.subplots(figsize=(canvas_size[0] / 100, canvas_size[1] / 100), dpi=100)

    # Відображаємо точки вихідного датасету
    ax.scatter(points[:, 0], points[:, 1], c='blue', s=10, label="Вихідні точки")

    # Відображаємо опуклу оболонку
    ax.plot(hull_points[:, 0], hull_points[:, 1], c='red', linewidth=2, label="Опукла оболонка")

    # Налаштування вигляду графіка
    ax.set_title("Опукла оболонка та вихідні точки", pad=10)
    ax.set_xlabel("X-координата", labelpad=5)
    ax.set_ylabel("Y-координата", labelpad=5)
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.legend()
    ax.set_aspect('auto')  

    # Зберігаємо результат у файл
    try:
        plt.savefig(output_file, bbox_inches='tight', dpi=100)
        print(f"Графік успішно збережено у файл: {output_file}")
    except Exception as e:
        print(f"Помилка при збереженні графіка: {e}")
    
    plt.show()
    plt.close()

file_name = "DS1.txt"
output_hull_file = "convex_hull.txt"
output_image_file = "output_image.png"

points = read_coordinates(file_name)

# Перевірка, чи є точки для обробки
if points.size > 0:
    hull = ConvexHull(points)
    hull_indices = hull.vertices

    save_convex_hull(points[hull_indices], output_hull_file)
    
    plot_with_convex_hull(points, hull_indices, canvas_size=(960, 540), output_file=output_image_file)
