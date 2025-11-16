from PIL import Image
import numpy as np
from PIL import ImageChops
from PIL import ImageStat as stat
import matplotlib.pyplot as plt
from random import randint


def ocen_czy_identyczne(obraz1, obraz2):
    if obraz1.mode != obraz2.mode:
        return f"obrazy nie są identyczne, bo obrazy mają różne tryby)"

    if obraz1.size != obraz2.size:
        return f"obrazy nie są identyczne, bo obrazy mają różne rozmiary)"

    tab1 = np.array(obraz1)
    tab2 = np.array(obraz2)

    if not np.array_equal(tab1, tab2):
        return "obrazy nie są identyczne, bo obrazy mają różne wartości pikseli"

    return "obrazy identyczne"


def pokaz_roznice(obraz_wejsciowy):
    tab = np.array(obraz_wejsciowy, dtype=np.float64)

    if tab.ndim == 2:
        max_wartosc = np.max(tab)
        if max_wartosc > 0:
            tab_wynikowa = (tab / max_wartosc) * 255
        else:
            tab_wynikowa = tab
        tab_wynikowa = tab_wynikowa.astype(np.uint8)
        obraz_wynikowy = Image.fromarray(tab_wynikowa, mode=obraz_wejsciowy.mode)

    elif tab.ndim > 2:
        tab_wynikowa = np.zeros_like(tab)

        for k in range(tab.shape[2]):
            max_wartosc_kanalu = np.max(tab[:, :, k])
            if max_wartosc_kanalu > 0:
                tab_wynikowa[:, :, k] = (tab[:, :, k] / max_wartosc_kanalu) * 255
            else:
                tab_wynikowa[:, :, k] = tab[:, :, k]

        tab_wynikowa = tab_wynikowa.astype(np.uint8)
        obraz_wynikowy = Image.fromarray(tab_wynikowa, mode=obraz_wejsciowy.mode)

    return obraz_wynikowy

def wstaw_obraz_w_obraz(obraz_bazowy, obraz_wstawiany, m, n):
    tablica_baza = np.asarray(obraz_bazowy).astype(np.uint8)
    h, w, s = tablica_baza.shape
    tab_obraz = np.asarray(obraz_wstawiany).astype(np.int_)
    h0, w0, s0 = tab_obraz.shape

    poczatek_y = max(0, n)
    poczatek_x = max(0, m)
    koniec_y = min(h, n + h0)
    koniec_x = min(w, m + w0)

    for wiersz in range(poczatek_y, koniec_y):
        for kolumna in range(poczatek_x, koniec_x):
            tablica_baza[wiersz, kolumna] = tab_obraz[wiersz - n][kolumna - m]

    return Image.fromarray(tablica_baza)

def wstaw_inicjaly(obraz_bazowy, obraz_wstawiany, m, n, kolor):
    obraz_inicjaly = obraz_bazowy.copy()
    if obraz_wstawiany.mode == "1":
        t_obraz = np.asarray(obraz_wstawiany)
        tablica_baza = np.asarray(obraz_inicjaly).astype(np.uint8)

        h0, w0 = t_obraz.shape
        h, w, s = tablica_baza.shape

        poczatek_y = max(0, n)
        poczatek_x = max(0, m)
        koniec_y = min(h, n + h0)
        koniec_x = min(w, m + w0)

        for wiersz in range(poczatek_y, koniec_y):
            for kolumna in range(poczatek_x, koniec_x):
                if not t_obraz[wiersz - n, kolumna - m]:
                    tablica_baza[wiersz, kolumna] = kolor

        obraz_inicjaly = Image.fromarray(tablica_baza)
    else:
        print("Nieprawidłowy format obrazu wstawianego")

    return obraz_inicjaly

def odkoduj(obraz1, obraz2):
    tab_obraz1 = np.asarray(obraz1).astype(np.uint8)
    tab_obraz2 = np.asarray(obraz2).astype(np.uint8)

    h, w, s = tab_obraz1.shape
    t = (h, w, s)
    t_wynik = np.ones(t, dtype=np.uint8)

    for i in range(h):
        for j in range(w):
            if np.array_equal(tab_obraz1[i, j], tab_obraz2[i, j]):
                t_wynik[i, j] = 0
            else:
                t_wynik[i, j] = 255

    return Image.fromarray(t_wynik)

# ------------------------------------- zad 6 ------------------------------------- #
# a)
# im = Image.open("beksinski.png")
# im1 = Image.open("beksinski1.png")
# im2 = Image.open("beksinski2.png")
# im3 = Image.open("beksinski3.png")
#
# print(ocen_czy_identyczne(im, im1))
# print(ocen_czy_identyczne(im, im2))
# print(ocen_czy_identyczne(im, im3))
# print(ocen_czy_identyczne(im2, im3))
# print(ocen_czy_identyczne(im2, im2))


# ------------------------------------- zad 7 ------------------------------------- #
# a)
# im = Image.open("im3.jpg")
# im_r = pokaz_roznice(im)
# im_r.save("im_jpg3.jpg")
# im_r.show()

# b)
# im = Image.open("im.jpg")
# im_jpg3 = Image.open("im_jpg3.jpg")
# diff = ImageChops.difference(im, im_jpg3)
# diff.show()

# c)
# im = Image.open("im.jpg")
# im_jpg3 = Image.open("im_jpg3.jpg")
# diff = ImageChops.difference(im, im_jpg3)
#
# plt.figure(figsize=(16, 16))
# plt.subplot(2,2,1) # ile obrazów w pionie, ile w poziomie, numer obrazu
# plt.imshow(im)
# plt.axis('off')
# plt.subplot(2,2,2)
# plt.imshow(im_jpg3)
# plt.axis('off')
# plt.subplot(2,2,3)
# plt.imshow(diff)
# plt.axis('off')
# plt.subplot(2,2,4)
# plt.imshow(pokaz_roznice(diff))
# plt.axis('off')
# plt.subplots_adjust(wspace=0.05, hspace=0.05)
# plt.savefig('fig2.png')
# plt.show()

# ------------------------------------- zad 8 ------------------------------------- #
# a)
# im = Image.open("im.jpg")
# inicialy = Image.open('inicjaly.bmp')
#
# obraz1 = wstaw_inicjaly(im, inicialy, (im.size[0] - inicialy.size[0]),0,[0, 255, 0])
# obraz2 = wstaw_inicjaly(obraz1, inicialy,0, (im.size[1] - inicialy.size[1]),[255, 200, 100])
# obraz_inicialy = wstaw_inicjaly(obraz2, inicialy, (im.size[0] - int((inicialy.size[0] / 2))), int(im.size[1] / 2),[100, 200, 255])
# # obraz_inicialy.save("obraz_inicjaly.png")
# obraz_inicialy.show()

# ------------------------------------- zad 9 ------------------------------------- #
# a) i b)
# jesien = Image.open('jesien.jpg')
# zakodowany = Image.open('zakodowany1.bmp')
# kod2 = odkoduj(jesien,zakodowany)
# kod2.save('kod2.bmp')
