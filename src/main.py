import cv2
from seeds_generator import SeedGenerator
from voronoi_qr import VoronoiQR
import matplotlib.pyplot as plt
from scipy.spatial import voronoi_plot_2d


def plot_voronoi(vor):
    voronoi_plot_2d(vor)
    plt.show()


def main():
    #########################################################
    # PARTIE 1 : Dissimuler un code QR dans un code QR hôte #
    #########################################################
    # Charger les images des codes QR
    img_host = cv2.imread('../qrcodes/qrcode_host.png', cv2.IMREAD_GRAYSCALE)
    img_hidden = cv2.imread('../qrcodes/qrcode_hidden.png', cv2.IMREAD_GRAYSCALE)

    # Générer N germes aléatoirement
    N = 9
    seed_gen = SeedGenerator(key=6)
    seeds = seed_gen.generate_seeds(N, img_host.shape)
    print(seeds)

    # Partitionner l'ensemble {1, 2, … , N} en deux parties A et B de même taille
    A = set(range(1, N + 1, 2))
    B = set(range(2, N + 1, 2))

    # Définir la clé C
    C = {k: 0 if k in A else 1 for k in range(1, N + 1)}
    print(C)

    # Créer le diagramme de Voronoi et effectuer l'insertion
    vor_qr = VoronoiQR(seeds)
    # plot_voronoi(vor_qr.voronoi)
    img_augmented = vor_qr.insert(img_host, img_hidden, C)
    # Sauvegarder l'image augmentée
    cv2.imwrite('../qrcodes/qrcode_augmented.png', img_augmented)

    # Effectuer l'extraction
    img_extracted = vor_qr.extract(img_augmented, C)
    # Sauvegarder l'image extraite
    cv2.imwrite('../qrcodes/qrcode_hidden_retrieved.png', img_extracted)

    ########################################################################
    # Partie 2 : Dissimuler plusieurs images binaires dans un code QR hôte #
    ########################################################################


if __name__ == '__main__':
    main()
