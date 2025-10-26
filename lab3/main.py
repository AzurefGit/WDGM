import numpy as np
from PIL import Image


# -------------------------- Zadanie 1 -------------------------- #

# def rysuj_ramki_szare(w, h, grub, kolor_ramki, kolor):
#     t = (h, w)
#     tab = np.ones(t, dtype=np.uint8)
#     c =  int(w/grub)
#
#     for i in range(c):
#         top = i * grub
#         bottom = h - i * grub
#         left = i * grub
#         right = w - i * grub
#
#         if i % 2 == 0:
#             tab[top:bottom, left:right] = kolor
#         else:
#             tab[top:bottom, left:right] = kolor_ramki
#
#     return Image.fromarray(tab)

# rrs = rysuj_ramki_szare(100, 100, 10, 100, 150)
# print(rrs.mode)
# rrs.show()


# def rysuj_pasy_pionowe_szare(w, h, grub, zmiana_koloru):
#     t = (h, w)
#     tab = np.ones(t, dtype=np.uint8)
#     ile =  int(w/grub)
#     for k in range(ile):
#         for g in range(grub):
#             j = k * grub + g
#             for i in range(h):
#                 tab[i, j] = (k + zmiana_koloru) % 256
#     return Image.fromarray(tab)

# rpps = rysuj_pasy_pionowe_szare(150, 200, 15, 100)
# print(rpps.mode)
# rpps.show()


# -------------------------- Zadanie 2 -------------------------- #

def negatyw_szare(obraz):
    if obraz.mode == "L":
        tab = np.asarray(obraz)
        h, w = tab.shape
        tab_neg = tab.copy()
        for i in range(h):
            for j in range(w):
                tab_neg[i, j] = 255 - tab[i, j]
        return Image.fromarray(tab_neg)

    elif obraz.mode == "1":
        tab = np.asarray(obraz)
        h, w = tab.shape
        tab_neg = tab.copy()
        for i in range(h):
            for j in range(w):
                tab_neg[i, j] = ~tab_neg[i, j]
        return Image.fromarray(tab_neg)

    elif obraz.mode == "RGB":
        tab = np.asarray(obraz)
        h, w, d = tab.shape
        tab_neg = tab.copy()
        for i in range(h):
            for j in range(w):
                for k in range(d):
                    tab_neg[i, j, k] = 255 - tab_neg[i, j, k]
        return Image.fromarray(tab_neg)

#a)
# gwiazdka = Image.open("gwiazdka.bmp")
# print(gwiazdka.mode)
# obraz_neg_g = negatyw_szare(gwiazdka)
# obraz_neg_g.show()

#b)
# def rysuj_ramki_kolorowe(w, kolor, a, b, c):
#     t = (w, w, 3)
#     tab = np.zeros(t, dtype=np.uint8)
#     kolor_r = kolor[0]
#     kolor_g = kolor[1]
#     kolor_b = kolor[2]
#     z = w
#     for k in range(int(w / 2)):
#         for i in range(k, z - k):
#             for j in range(k, z - k):
#                 tab[i, j] = [kolor_r, kolor_g, kolor_b]
#         kolor_r = (kolor_r - a) % 256
#         kolor_g = (kolor_g - b) % 256
#         kolor_b = (kolor_b - c) % 256
#     return Image.fromarray(tab)
#
#
# rrk = rysuj_ramki_kolorowe(200, [20, 120,220], a = 6, b = 10, c = -6)
# rrk.show()
# obraz_neg_r = negatyw_szare(rrk)
# obraz_neg_r.show()

# c)
# def rysuj_po_skosie_szare(h, w, a, b):
#     t = (h, w)
#     tab = np.zeros(t, dtype=np.uint8)
#     for i in range(h):
#         for j in range(w):
#             tab[i, j] = (a*i + b*j) % 256
#     return Image.fromarray(tab)


# rpss = rysuj_po_skosie_szare(100, 300, 6, 10)
# rpss.show()
# obraz_neg_rpss = negatyw_szare(rpss)
# obraz_neg_rpss.show()

# -------------------------- Zadanie 3 -------------------------- #

def koloruj_w_paski(obraz, grub, kolor, zmiana_koloru):
    if obraz.mode == "1":
        t_obraz = np.asarray(obraz)
        h, w = t_obraz.shape
        t = (h, w, 3)
        tab = np.ones(t, dtype=np.uint8)
        ile = int(h / grub)
        for k in range(ile):
            r = (kolor[0] + k * zmiana_koloru) % 256
            g = (kolor[1] + k * zmiana_koloru) % 256
            b = (kolor[2] + k * zmiana_koloru) % 256
            for m in range(grub):
                i = k * grub + m
                for j in range(w):
                    if not t_obraz[i, j]:
                        tab[i, j] = [r, g, b]
                    else:
                        tab[i, j] = [255, 255, 255]

        return Image.fromarray(tab)
    else:
        print("Zły tryb obrazu")

inicjaly = Image.open("inicjaly.bmp")
print(inicjaly.mode)
kwp = koloruj_w_paski(inicjaly, 1, [100, 200, 0], 2020)
kwp.show()
# kwp.save("kwp.jpg")
# kwp.save("kwp.png")

# odp do pytań: plik jpg ulega kompresji stratnej przez co wygląda gorzej niż plik png.

# ---------------- Zadanie 4 ------------------ #
# Typ unit8 w przypadku podania wartości innej niż z przedziału 0 - 255 będzie konwertować daną liczbę na liczbę właśnie z tego przedziału, przykłady:
# a) 328 - 256 = 72
# b) -24 + 256 = 232