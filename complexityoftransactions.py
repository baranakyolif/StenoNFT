
#A small architecture has been added to our project to select the optimal 
pixels without compromising the integrity of an image file.  This architecture
is based on the algorithmic description of the propagation steps of a protista known
in biology as Physarum polycephalum and the addition of this algorithm to Dijkstra's algorithm. 
These algorithms are optimization architecture designed to select the most suitable pixels for 
textual data to be hidden in an image.

 


from google.colab import drive
drive.mount('/content/drive')
import numpy as np
from PIL import Image

import matplotlib.pyplot as plt
import heapq

def load_image(image_path):
    """Resmi yükler ve numpy array olarak döndürür."""
    with Image.open(image_path) as img:
        return np.array(img)

def create_graph(image):
    """Pikseller arasında bir graf oluşturur. Kenar ağırlıkları renk farklarına dayanır."""
    height, width, _ = image.shape
    graph = {}
    for i in range(height):
        for j in range(width):
            edges = {}
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < height and 0 <= nj < width:
                    diff = np.linalg.norm(image[i, j] - image[ni, nj])
                    edges[(ni, nj)] = diff
            graph[(i, j)] = edges
    return graph

def dijkstra(graph, start, end):
    """Dijkstra algoritması ile en kısa yolu bulur."""
    heap = [(0, start)]
    visited = set()
    distances = {start: 0}
    parents = {start: None}

    while heap:
        current_distance, current_node = heapq.heappop(heap)

        if current_node in visited:
            continue
        visited.add(current_node)

        if current_node == end:
            break

        for neighbor, weight in graph[current_node].items():
            if neighbor in visited:
                continue
            new_distance = current_distance + weight
            if new_distance < distances.get(neighbor, float('inf')):
                distances[neighbor] = new_distance
                parents[neighbor] = current_node
                heapq.heappush(heap, (new_distance, neighbor))

    return parents

def reconstruct_path(parents, start, end):
    """Bulunan en kısa yolu geri takip eder."""
    path = []
    current = end
    while current != start:
        path.append(current)
        current = parents[current]
    path.append(start)
    path.reverse()
    return path

def visualize_path(image, path):
    """Bulunan yolu resim üzerinde görselleştirir."""
    for (i, j) in path:
        image[i, j] = [255, 0, 0]  # Yolu kırmızıyla işaretle
    plt.imshow(image)
    plt.title('Yol Görselleştirmesi')
    plt.show()

# Parametreler
image_path = '/content/drive/My Drive/1.png'  # Google Drive üzerindeki resim yolu
start = (10, 10)  # Başlangıç noktası
end = (90, 90)    # Bitiş noktası

# İşlemler
image = load_image(image_path)
graph = create_graph(image)
parents = dijkstra(graph, start, end)
path = reconstruct_path(parents, start, end)
visualize_path(image, path)
