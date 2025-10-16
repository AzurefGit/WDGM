# rozpoznowanie trybów: L, 1 lub RGB; zrobić negatyw

import numpy as np
from PIL import Image


# -------------------------- Zadanie 1 -------------------------- #

def rysuj_ramki_szare(w, h, grub, kolor_ramki, kolor):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    c =  int(w/grub)

    for i in range(c):
        top = i * grub
        bottom = h - i * grub
        left = i * grub
        right = w - i * grub

        if i % 2 == 0:
            tab[top:bottom, left:right] = kolor
        else:
            tab[top:bottom, left:right] = kolor_ramki

    return Image.fromarray(tab)

# rrs = rysuj_ramki_szare(100, 100, 10, 100, 200)
# print(rrs.mode)
# rrs.show()


def rysuj_pasy_pionowe_szare(w, h, grub, zmiana_koloru):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    ile =  int(w/grub)
    for k in range(ile):
        for g in range(grub):
            j = k * grub + g
            for i in range(h):
                tab[i, j] = (k + zmiana_koloru) % 256
    return Image.fromarray(tab)

# rpps = rysuj_pasy_pionowe_szare(100, 246, 1, 10)
# print(rpps.mode)
# rpps.show()


# -------------------------- Zadanie 2 -------------------------- #

gwiazdka = Image.open("gwiazdka.bmp")
print(gwiazdka.mode)

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
        h, w = tab.shape
        tab_neg = tab.copy()
        for i in range(h):
            for j in range(w):
                tab_neg[i, j] = tab_neg[255 - i, 255 - j]
        return Image.fromarray(tab_neg)


obraz_neg = negatyw_szare(gwiazdka)
obraz_neg.show()