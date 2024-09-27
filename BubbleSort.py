import matplotlib.pyplot as plt
import numpy as np

def bubble_sort(data, draw_bars, delay):
    for i in range(len(data) - 1):
        for j in range(len(data) - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                draw_bars(data, ['blue' if x == j or x == j+1 else 'grey' for x in range(len(data))])
                plt.pause(delay)

def draw_bars(data, color_array):
    plt.clf()  
    plt.bar(range(len(data)), data, color=color_array)
    plt.xlabel("O(n^2)")
    plt.title("Bubble Sort Visualization")

def visualize_sorting():
    data = np.random.randint(1, 100, size=50)
    delay = 0.005 
    fig, ax = plt.subplots()

    draw_bars(data, ['grey' for _ in range(len(data))])

    bubble_sort(data, draw_bars, delay)

    plt.close()

visualize_sorting()

plt.show(block=False)
