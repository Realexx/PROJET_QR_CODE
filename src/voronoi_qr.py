import numpy as np
from scipy.spatial import Voronoi


class VoronoiQR:
    def __init__(self, seeds):
        self.voronoi = Voronoi(seeds)

    #########################################################
    # PARTIE 1 : Dissimuler un code QR dans un code QR hôte #
    #########################################################
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
                    b = 255 - a * 255
                else:
                    a = (255 - img_augmented[i, j]) % 2
                    b = 255 - a * 255

                k = np.argmin(np.sum((self.voronoi.points - np.array([i, j])) ** 2, axis=1)) + 1

                if C[k] == 0:
                    img_extracted[i, j] = a * 255
                else:
                    img_extracted[i, j] = b

        return img_extracted

    ########################################################################
    # Partie 2 : Dissimuler plusieurs images binaires dans un code QR hôte #
    ########################################################################
    def insert_multiple(self, img_host, img_hiddens):
        img_new = np.zeros_like(img_host, dtype=np.uint8)

        for i in range(img_host.shape[0]):
            for j in range(img_host.shape[1]):
                # Calculer la nouvelle valeur du pixel pour chaque image à dissimuler
                pixel_value = sum(img_hidden[i, j] * 2 ** k * 255 for k, img_hidden in enumerate(img_hiddens))
                if img_host[i, j] == 0:
                    img_new[i, j] = pixel_value
                else:
                    img_new[i, j] = 255 - pixel_value

        return img_new

    def extract_multiple(self, img_augmented, n):
        # Initialiser un tableau pour stocker les images extraites
        images_extracted = [np.zeros_like(img_augmented, dtype=np.uint8) for _ in range(n)]

        for i in range(img_augmented.shape[0]):
            for j in range(img_augmented.shape[1]):
                # Décomposer le pixel en une séquence de bits
                if img_augmented[i, j] < 2 ** (n + 1):
                    bits = [int(b) for b in format(img_augmented[i, j], f'0{n}b')]
                else:
                    bits = [int(b) for b in format(255 - img_augmented[i, j], f'0{n}b')]

                # Utiliser les bits pour reconstruire les images binaires
                for k, img in enumerate(images_extracted):
                    img[i, j] = bits[k] * 255

        return images_extracted

    ###################################
    # Partie 3 : QR augmenté sécurisé #
    ###################################
    def insert_voronoi(self, img_host, img_hiddens):
        img_new = np.zeros_like(img_host, dtype=np.uint8)

        for i in range(img_host.shape[0]):
            for j in range(img_host.shape[1]):
                # Trouver la région de Voronoi correspondante
                k = np.argmin(np.sum((self.voronoi.points - np.array([i, j])) ** 2, axis=1))

                # Définir la séquence d'images à insérer en fonction de la région
                if k == 0:
                    sequence = [3, 2, 0, 1]
                elif k == 1:
                    sequence = [1, 3, 2, 0]
                else:  # k == 2
                    sequence = [2, 0, 3, 1]

                # Calculer la nouvelle valeur du pixel pour chaque image à dissimuler
                pixel_value = sum(img_hiddens[sequence[k]][i, j] * 2 ** k * 255 for k in range(4))
                if img_host[i, j] == 0:
                    img_new[i, j] = pixel_value
                else:
                    img_new[i, j] = 255 - pixel_value

        return img_new
