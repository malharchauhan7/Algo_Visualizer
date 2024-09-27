import matplotlib.pyplot as plt
import numpy as np

def selection_sort(data, draw_bars, delay):
    for i in range(len(data)):
        min_idx = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
        draw_bars(data, ['blue' if x == i or x == min_idx else 'grey' for x in range(len(data))])
        plt.pause(delay)

def draw_bars(data, color_array):
    plt.clf()  
    plt.bar(range(len(data)), data, color=color_array)
    plt.title("Selection Sort Visualization")

def visualize_sorting():
    data = np.random.randint(1, 100, size=50)
    delay = 0.005 
    fig, ax = plt.subplots()

    draw_bars(data, ['grey' for _ in range(len(data))])

    selection_sort(data, draw_bars, delay)

    plt.close()

visualize_sorting()

plt.show(block=False)
