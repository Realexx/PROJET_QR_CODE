import numpy as np
from scipy.spatial import Voronoi


class VoronoiQR:
    def __init__(self, seeds):
        self.voronoi = Voronoi(seeds)

    def insert(self, img_host, img_hidden, C):
        # Calculer la nouvelle image
        img_new = np.zeros_like(img_host)

        for i in range(img_host.shape[0]):
            for j in range(img_host.shape[1]):
                # Trouver la région de Voronoï correspondante
                k = np.argmin(np.sum((self.voronoi.points - np.array([i, j])) ** 2, axis=1)) + 1
                if img_host[i, j] == 0:
                    if C[k] == 0:
                        img_new[i, j] = img_hidden[i, j] + (1 - img_hidden[i, j]) * 2
                    else:
                        img_new[i, j] = (1 - img_hidden[i, j]) + img_hidden[i, j] * 2
                else:
                    if C[k] == 0:
                        img_new[i, j] = 255 - img_hidden[i, j] - (1 - img_hidden[i, j]) * 2
                    else:
                        img_new[i, j] = 255 - (1 - img_hidden[i, j]) - img_hidden[i, j] * 2
        return img_new

    def extract(self, img_augmented, C):
        img_extracted = np.zeros_like(img_augmented)
        for i in range(img_augmented.shape[0]):
            for j in range(img_augmented.shape[1]):
                if img_augmented[i, j] < 4:
                    a = img_augmented[i, j] % 2
                    b = img_augmented[i, j] // 2
                else:
                    a = (255 - img_augmented[i, j]) % 2
                    b = (255 - img_augmented[i, j]) // 2

                # Trouver la région de Voronoï correspondante
                k = np.argmin(np.sum((self.voronoi.points - np.array([i, j])) ** 2, axis=1)) + 1

                if C[k] == 0:
                    img_extracted[i, j] = a * 255
                else:
                    img_extracted[i, j] = 255 - a * 255  # NE MARCHE PAS AVEC 'b'

        return img_extracted
