import cv2

from qr_generator import *
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
    generate_host_qrcode()
    qr_host = cv2.imread('../qrcodes/qrcode_host.png', cv2.IMREAD_GRAYSCALE)
    generate_hidden_qrcode()
    qr_to_hide = cv2.imread('../qrcodes/qrcode_hidden.png', cv2.IMREAD_GRAYSCALE)

    # Générer N germes aléatoirement
    N = 9
    seed_gen = SeedGenerator(key=6)
    seeds = seed_gen.generate_seeds(N, qr_host.shape)
    print(f"Germes Exercice 1 : \n{seeds}")

    # Partitionner l'ensemble {1, 2, … , N} en deux parties A et B de même taille
    A = set(range(1, N + 1, 2))
    B = set(range(2, N + 1, 2))

    # Définir la clé C
    C = {k: 0 if k in A else 1 for k in range(1, N + 1)}
    print(f"C = {C}")

    # Créer le diagramme de Voronoi et effectuer l'insertion
    vor_qr = VoronoiQR(seeds)
    # plot_voronoi(vor_qr.voronoi)
    qr_augmented = vor_qr.insert(qr_host, qr_to_hide, C)
    # Sauvegarder l'image augmentée
    cv2.imwrite('../qrcodes/qrcode_augmented.png', qr_augmented)

    # Effectuer l'extraction
    img_extracted = vor_qr.extract(qr_augmented, C)
    # Sauvegarder l'image extraite
    cv2.imwrite('../qrcodes/qrcode_hidden_retrieved.png', img_extracted)

    ########################################################################
    # Partie 2 : Dissimuler plusieurs images binaires dans un code QR hôte #
    ########################################################################
    # Charger les images des codes QR à cacher
    nb_qr_to_hide = 5
    generate_multiple_qrcode_to_hide(nb_qr_to_hide)
    qrs_to_hide = [cv2.imread(f'../qrcodes/multiples/qrcode_hidden_{i}.png', cv2.IMREAD_GRAYSCALE)
                   for i in range(nb_qr_to_hide)]

    # Créer l'image augmentée en dissimulant les images binaires
    qr_augmented_multiple = vor_qr.insert_multiple(qr_host, qrs_to_hide)
    # Sauvegarder l'image augmentée
    cv2.imwrite('../qrcodes/multiples/qrcode_augmented_multiple.png', qr_augmented_multiple)

    # Effectuer l'extraction
    img_extracted_multiple = vor_qr.extract_multiple(qr_augmented_multiple, nb_qr_to_hide)
    # Sauvegarder les images extraites
    for i, img_extracted in enumerate(reversed(img_extracted_multiple)):
        cv2.imwrite(f'../qrcodes/multiples/qrcode_hidden_retrieved_{i}.png', img_extracted)

    ###################################
    # Partie 3 : QR augmenté sécurisé #
    ###################################
    # Générer 3 germes pour l'insertion sécurisée
    seed_gen = SeedGenerator(key=2)
    seeds = seed_gen.generate_seeds(3, qr_host.shape)
    print(f"\nGermes Exercice 3 : \n{seeds}")

    vor_qr_secured = VoronoiQR(seeds)
    plot_voronoi(vor_qr_secured.voronoi)

    # Charger les images des codes QR à cacher
    nb_qr_to_hide = 4
    generate_secure_qrcode_to_hide(nb_qr_to_hide)
    qrs_to_hide = [cv2.imread(f'../qrcodes/secured/qrcode_hidden_{i}.png', cv2.IMREAD_GRAYSCALE)
                   for i in range(nb_qr_to_hide)]

    # Créer l'image augmentée en dissimulant les images binaires
    qr_augmented_secured = vor_qr_secured.insert_voronoi(qr_host, qrs_to_hide)
    cv2.imwrite('../qrcodes/secured/qrcode_augmented_secured.png', qr_augmented_secured)

    # Effectuer l'extraction
    img_extracted_secured = vor_qr_secured.extract_voronoi(qr_augmented_secured)
    for i, img_extracted in enumerate(reversed(img_extracted_secured)):
        cv2.imwrite(f'../qrcodes/secured/qrcode_hidden_retrieved_{i}.png', img_extracted)


if __name__ == '__main__':
    main()
