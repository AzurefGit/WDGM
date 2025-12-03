import random

from PIL import Image
import numpy as np
from matplotlib import pyplot as plt


def wstaw_inicjaly(obraz, inicjaly, m, n, kolor):
    obraz_kopia = obraz.copy()
    w, h = obraz.size
    w_ini, h_ini = inicjaly.size

    for i in range(w_ini):
        for j in range(h_ini):
            if m + i < w and n + j < h:
                piksel_ini = inicjaly.getpixel((i, j))
                if piksel_ini == 0:
                    obraz_kopia.putpixel((m + i, n + j), kolor)

    return obraz_kopia

def wstaw_inicjaly_maska(obraz, inicjaly, m, n):
    obraz_kopia = obraz.copy()
    w, h = obraz.size
    w_ini, h_ini = inicjaly.size

    for i in range(w_ini):
        for j in range(h_ini):
            if w > i + m >= 0 and h > j + n >= 0:
                pixel_ini = inicjaly.getpixel((i, j))
                if pixel_ini == 0:
                    pixel_obrazu = obraz.getpixel((i + m, j + n))
                    negatyw = (255 - pixel_obrazu[0], 255 - pixel_obrazu[1], 255 - pixel_obrazu[2])
                    obraz_kopia.putpixel((i + m, j + n), negatyw)

    return obraz_kopia

def wstaw_inicjaly_load(obraz, inicjaly, m, n, kolor):
    obraz_kopia = obraz.copy()
    w, h = obraz.size
    w_ini, h_ini = inicjaly.size

    pixele_obraz = obraz_kopia.load()
    pixele_inicjaly = inicjaly.load()

    for i in range(w_ini):
        for j in range(h_ini):
            if w > i + m >= 0 and h > j + n >= 0:
                if pixele_inicjaly[i, j] == 0:
                    pixele_obraz[i + m, j + n] = kolor

    return obraz_kopia

def wstaw_inicjaly_maska_load(obraz, inicjaly, m, n):

    obraz_kopia = obraz.copy()
    w_obraz, h_obraz = obraz.size
    w_ini, h_ini = inicjaly.size

    pixele_obraz = obraz_kopia.load()
    pixele_inicjaly = inicjaly.load()

    for i in range(w_ini):
        for j in range(h_ini):
            if w_obraz > i + m >= 0 and h_obraz > j + n >= 0:
                if pixele_inicjaly[i, j] == 0:
                    p = pixele_obraz[i + m, j + n]
                    pixele_obraz[i + m, j + n] = (255 - p[0], 255 - p[1], 255 - p[2])

    return obraz_kopia

def kontrast(obraz, wsp_kontrastu):
    mn = ((255 + wsp_kontrastu) / 255) ** 2
    return obraz.point(lambda i: 128 + (i - 128) * mn)

def transformacja_logarytmiczna(obraz):
    return obraz.point(lambda i: 255 * np.log(1 + i / 255))

def filtr_liniowy_point(obraz, a, b):
    return obraz.point(lambda i: i * a + b)

def transformacja_gamma(obraz, gamma):
    return obraz.point(lambda i: ((i / 255) ** (1 / gamma)) * 255)

def transformacja_gamma_lista(obraz, gamma):
    listaL = [((i / 255) ** (1 / gamma)) * 255 for i in range(256)]
    listaRGB = listaL + listaL + listaL

    return obraz.point(listaRGB)


def rozjasnij_tablica(obraz, wartosc):
    T = np.array(obraz, dtype='int16')
    T += wartosc
    T = np.clip(T, 0, 255)
    T = T.astype('uint8')

    return Image.fromarray(T, "RGB")

# ---------------------------------- Zad 1 ---------------------------------- #
obraz = Image.open("obraz.png")
inicjaly = Image.open("inicjaly.bmp")


# ---------------------------------- Zad 2 ---------------------------------- #
# a)
obraz1 = wstaw_inicjaly(obraz, inicjaly, 115, 215,(255,0,0))
# obraz1.show()
# obraz1.save("obraz1.png")

# b)
obraz2 = wstaw_inicjaly_maska(obraz, inicjaly, 60, 110)
# obraz2.save('obraz2.png')
# obraz2.show()

# ---------------------------------- Zad 3 ---------------------------------- #
# obraz3 = wstaw_inicjaly_load(obraz, inicjaly, 115, 215,(255,0,0))
# obraz4 = wstaw_inicjaly_maska_load(obraz, inicjaly, 60, 110)
#
# fig, axes = plt.subplots(2, 2, figsize=(12, 10))
#
# axes[0, 0].imshow(obraz1)
# axes[0, 0].set_title('Zadanie 2a')
# axes[0, 0].axis('off')
#
# axes[0, 1].imshow(obraz2)
# axes[0, 1].set_title('Zadanie 2b')
# axes[0, 1].axis('off')
#
# axes[1, 0].imshow(obraz3)
# axes[1, 0].set_title('Zadanie 3a load')
# axes[1, 0].axis('off')
#
# axes[1, 1].imshow(obraz4)
# axes[1, 1].set_title('Zadanie 3b load')
# axes[1, 1].axis('off')
#
# plt.tight_layout()
# plt.savefig('fig1.png')
# plt.show()

# ---------------------------------- Zad 4 ---------------------------------- #
# a)
# obraz_kontrast_50 = kontrast(obraz, 50)
# obraz_kontrast_100 = kontrast(obraz, 100)
# obraz_kontrast_minus100 = kontrast(obraz, -100)
#
# fig, axes = plt.subplots(2, 2, figsize=(14, 10))
#
# axes[0, 0].imshow(obraz)
# axes[0, 0].set_title('Obraz oryginalny')
# axes[0, 0].axis('off')
#
# axes[0, 1].imshow(obraz_kontrast_50)
# axes[0, 1].set_title('Kontrast: wsp = 50')
# axes[0, 1].axis('off')
#
# axes[1, 0].imshow(obraz_kontrast_100)
# axes[1, 0].set_title('Kontrast: wsp = 100')
# axes[1, 0].axis('off')
#
# axes[1, 1].imshow(obraz_kontrast_minus100)
# axes[1, 1].set_title('Kontrast: wsp = -100')
# axes[1, 1].axis('off')
#
# plt.tight_layout()
# plt.savefig('fig2.png')
# plt.show()

# b)
# obraz_log = transformacja_logarytmiczna(obraz)
# obraz_liniowy = filtr_liniowy_point(obraz, 2, 100)
#
# fig, axes = plt.subplots(1, 3, figsize=(15, 5))
#
# axes[0].imshow(obraz)
# axes[0].set_title('Obraz oryginalny')
# axes[0].axis('off')
#
# axes[1].imshow(obraz_log)
# axes[1].set_title('Transformacja logarytmiczna')
# axes[1].axis('off')
#
# axes[2].imshow(obraz_liniowy)
# axes[2].set_title('Filtr liniowy (a=2, b=100)')
# axes[2].axis('off')
#
# plt.tight_layout()
# plt.savefig('fig3.png')
# plt.show()

# c)
# obraz_gamma_1 = transformacja_gamma(obraz, 1.0)
# obraz_gamma_2 = transformacja_gamma(obraz, 2.0)
# obraz_gamma_5 = transformacja_gamma(obraz, 5.0)
#
# fig, axes = plt.subplots(2, 2, figsize=(14, 10))
#
# axes[0, 0].imshow(obraz)
# axes[0, 0].set_title('Obraz oryginalny')
# axes[0, 0].axis('off')
#
# axes[0, 1].imshow(obraz_gamma_1)
# axes[0, 1].set_title('Gamma = 1.0')
# axes[0, 1].axis('off')
#
# axes[1, 0].imshow(obraz_gamma_2)
# axes[1, 0].set_title('Gamma = 2.0')
# axes[1, 0].axis('off')
#
# axes[1, 1].imshow(obraz_gamma_5)
# axes[1, 1].set_title('Gamma = 5.0')
# axes[1, 1].axis('off')
#
# plt.tight_layout()
# plt.savefig('fig4.png')
# plt.show()

# ---------------------------------- Zad 5 ---------------------------------- #
# a)
# obraz_gamma = transformacja_gamma(obraz, 0.5)
# obraz_gamma_lista = transformacja_gamma_lista(obraz, 0.5)
#
# fig, axes = plt.subplots(1, 3, figsize=(15, 5))
#
# axes[0].imshow(obraz)
# axes[0].set_title('Obraz oryginalny')
# axes[0].axis('off')
#
# axes[1].imshow(obraz_gamma)
# axes[1].set_title('transformacja_gamma')
# axes[1].axis('off')
#
# axes[2].imshow(obraz_gamma_lista)
# axes[2].set_title('transformacja_gamma_lista')
# axes[2].axis('off')
#
# plt.tight_layout()
# plt.show()

# ---------------------------------- Zad 6 ---------------------------------- #
# a)
# T = np.array(obraz, dtype='uint8')
# T += 100
# obraz_wynik_numpy = Image.fromarray(T, "RGB")
#
# obraz_wynik_point = obraz.point(lambda i: i + 100)
#
# fig, axes = plt.subplots(1, 3, figsize=(15, 5))
#
# axes[0].imshow(obraz)
# axes[0].set_title('Obraz oryginalny')
# axes[0].axis('off')
#
# axes[1].imshow(obraz_wynik_numpy)
# axes[1].set_title('Metoda numpy:')
# axes[1].axis('off')
#
# axes[2].imshow(obraz_wynik_point)
# axes[2].set_title('Metoda point:')
# axes[2].axis('off')
#
# plt.tight_layout()
# plt.show()

# b)
obraz_test_point = obraz.point(lambda i: i + 100)
obraz_test_point.show()
obraz_test_tablica = rozjasnij_tablica(obraz, 100)
obraz_test_tablica.show()