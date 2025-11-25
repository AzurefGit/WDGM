import random

from PIL import Image
import numpy as np
from PIL import ImageChops
from PIL import ImageStat as stat
import matplotlib.pyplot as plt


def histogram_rgb(path):

    img = Image.open(path)
    img_np = np.array(img)

    R = img_np[:, :, 0].flatten()
    G = img_np[:, :, 1].flatten()
    B = img_np[:, :, 2].flatten()

    plt.figure(figsize=(16, 4))
    plt.suptitle(f"Histogram RGB dla {path}", fontsize=14)

    plt.subplot(1, 3, 1)
    plt.hist(R, bins=256, range=(0, 255))
    plt.title("Kanał R")

    plt.subplot(1, 3, 2)
    plt.hist(G, bins=256, range=(0, 255))
    plt.title("Kanał G")

    plt.subplot(1, 3, 3)
    plt.hist(B, bins=256, range=(0, 255))
    plt.title("Kanał B")

    plt.tight_layout()
    plt.show()

def rysuj_ramke_kolor(w, h, grub, r, g, b):
    t = (h, w, 3)
    tab = np.ones(t, dtype=np.uint8)
    tab[:, :] = [255, 0, 0]  # wypełnienie zielonym kolorem (ramka)
    tab[grub:h - grub, grub:w - grub] = [r, g, b]  # środek wypełniony kolorem (r, g, b)
    return tab

def rozpoznaj_mix(obraz, mix):
    obraz_n = negatyw(obraz)
    nr, ng, nb = obraz_n.split()
    r, g, b = obraz.split()
    kanaly = {
        'r': np.array(r),
        'g': np.array(g),
        'b': np.array(b),
        'nr': np.array(nr),
        'ng': np.array(ng),
        'nb': np.array(nb)
    }

    mix_r, mix_g, mix_b = mix.split()
    mix_kanaly = [np.array(mix_r), np.array(mix_g), np.array(mix_b)]
    nazwy_kanalow = ['R', 'G', 'B']
    tab2 = []

    for i, mix_kanal in enumerate(mix_kanaly):
        for nazwa, kanal in kanaly.items():
            if np.array_equal(mix_kanal, kanal):
                tab2.append(f"{nazwy_kanalow[i]} = {nazwa}")
                break

    return tab2

def negatyw(obraz):
    tab = np.asarray(obraz)
    h, w, d = tab.shape
    tab_neg = tab.copy()
    for i in range(h):
        for j in range(w):
            for k in range(d):
                tab_neg[i, j, k] = 255 - tab_neg[i, j, k]
    return Image.fromarray(tab_neg)

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

def ukryj_kod(obraz, im_kod):
    t_obraz = np.asarray(obraz)
    t_kodowany = t_obraz.copy()
    h, w, d = t_obraz.shape
    t_kod = np.asarray(im_kod).astype(np.uint8)
    for i in range(h):
        for j in range(w):
            if t_kod[i, j] == 0:
                k = np.random.randint(0,2)
                if t_obraz[i, j, k] < 255:
                    t_kodowany[i, j, k] = t_obraz[i, j, k] + 1
    return Image.fromarray(t_kodowany)


def odkryj_kod(obraz_oryginalny, obraz_zakodowany):
    t_oryginal = np.asarray(obraz_oryginalny).astype(np.uint8)
    t_zakodowany = np.asarray(obraz_zakodowany).astype(np.uint8)

    h, w, d = t_oryginal.shape
    t_kod = np.ones((h, w), dtype=np.uint8) * 255  # biały obraz

    for i in range(h):
        for j in range(w):
            if not np.array_equal(t_oryginal[i, j], t_zakodowany[i, j]):
                t_kod[i, j] = 0

    return Image.fromarray(t_kod, mode='L')


def zlicz_czarne_piksele(obraz):
    t_obraz = np.asarray(obraz).astype(np.uint8)
    licznik = 0

    if t_obraz.ndim == 2:
        h, w = t_obraz.shape
        for i in range(h):
            for j in range(w):
                if t_obraz[i, j] == 0:
                    licznik += 1

    return licznik


# Zad 1

# histogram_rgb("bek1.png")
# histogram_rgb("bek2.png")

# Zad2
# Image.fromarray(rysuj_ramke_kolor(120, 60, 10, 100, 200, 30)).show()

# Zad3
# bat1 = Image.open("batman1.png")
# mix11 = Image.open("mix11.png")
# print(rozpoznaj_mix(bat1, mix11))

# Zad4
# mono2 = Image.open("mono2.png")
# mono12 = Image.open("mono12.bmp")
# print(ocen_czy_identyczne(mono2, mono12))

# Zad5
# batman = Image.open('batman2.png')
# zakodowany = Image.open('zakodowany2_3.png')
#
# im_kod = odkryj_kod(batman, zakodowany)
# im_kod.save('im_kod.bmp')
# im_kod.show()
#
# czarne_piksele = zlicz_czarne_piksele(im_kod)
# print(f"Liczba czarnych pikseli w obrazie im_kod: {czarne_piksele}")

#7
# def szary(w, h, a, b):
#     t = (h, w)
#     tab = np.zeros(t, dtype=np.uint8)
#     for i in range(h):
#         for j in range(w):
#             tab[i, j] = (a * i ** 2 + b * j ** 2) % 256
#     return Image.fromarray(tab, mode='L')
#
# #Zad2
# bek4 = Image.open('bek4.png')
# print("Tryb:", bek4.mode)
# print("Rozmiar:", bek4.size)
#
# w, h = bek4.size
# obraz_szary = szary(w, h, -1, -2)
# obraz_szary.show()
#
# #Zad3
# t_bek4 = np.asarray(bek4).astype(np.uint8)
# t_szary = np.asarray(obraz_szary).astype(np.uint8)
#
# t_wynik = t_bek4.copy()
# t_wynik[:, :, 0] = t_szary
#
# obraz_wynikowy = Image.fromarray(t_wynik, mode='RGB')
#
# obraz_wynikowy.save('mix.png')
# obraz_wynikowy.show()
#
# #Zad4
# print("Obraz mix.png został zapisany pomyślnie!")
#

#8
# import numpy as np
# from PIL import Image
#
# def wstaw_obraz_w_obraz(obraz_bazowy, obraz_wstawiany, m, n):
#     tablica_baza = np.asarray(obraz_bazowy).astype(np.uint8)
#     h, w, s = tablica_baza.shape
#     tab_obraz = np.asarray(obraz_wstawiany).astype(np.int_)
#     h0, w0, s0 = tab_obraz.shape
#     poczatek_y = max(0, n)
#     poczatek_x = max(0, m)
#     koniec_y = min(h, n + h0)
#     koniec_x = min(w, m + w0)
#     for wiersz in range(poczatek_y, koniec_y):
#         for kolumna in range(poczatek_x, koniec_x):
#             tablica_baza[wiersz, kolumna] = tab_obraz[wiersz - n][kolumna - m]
#     return Image.fromarray(tablica_baza)
#
# def wstaw_obraz(obraz_bazowy, obraz_wstawiany, m, n, kolor):
#     obraz = obraz_bazowy.copy()
#     if obraz_wstawiany.mode == "1":
#         t_obraz = np.asarray(obraz_wstawiany)
#         tablica_baza = np.asarray(obraz).astype(np.uint8)
#         h0, w0 = t_obraz.shape
#         h, w, s = tablica_baza.shape
#         poczatek_y = max(0, n)
#         poczatek_x = max(0, m)
#         koniec_y = min(h, n + h0)
#         koniec_x = min(w, m + w0)
#         for wiersz in range(poczatek_y, koniec_y):
#             for kolumna in range(poczatek_x, koniec_x):
#                 if not t_obraz[wiersz - n, kolumna - m]:
#                     tablica_baza[wiersz, kolumna] = kolor
#         obraz = Image.fromarray(tablica_baza)
#     else:
#         print("Nieprawidłowy format obrazu wstawianego")
#     return obraz
#
# tablica = np.loadtxt("tab2.txt", dtype=np.uint8)
#
# obraz_z_tablicy = Image.fromarray(tablica * 255).convert('1')
#
# obraz_batman = Image.open('batman2.png')
#
# h_batman, w_batman = obraz_batman.size[1], obraz_batman.size[0]
# h_tablica, w_tablica = obraz_z_tablicy.size[1], obraz_z_tablicy.size[0]
#
# m = w_batman - w_tablica
# n = 0
#
# kolor_czerwony = (255, 0, 0)
#
# obraz_wynikowy = wstaw_obraz(obraz_batman, obraz_z_tablicy, m, n, kolor_czerwony)
#
# obraz_wynikowy.save('wynik.png')
# obraz_wynikowy.show()

#============================
#
# im2 = Image.open("im2.bmp")
# print("========== im2.bmp ==========")
# print("Tryb obrazu im2.bmp:", im2.mode)
# print("Rozmiar obrazu im2.bmp:", im2.size)
#
# # Konwersja na tablicę
# t_im2 = np.asarray(im2)
# print("Rozmiar tablicy im2.bmp:", t_im2.shape)
# print("Wymiar tablicy im2.bmp:", t_im2.ndim)
#
# # Wartość elementu tablicy o adresie (100, 50)
# # Uwaga: w PIL (100, 50) to (x=100, y=50), ale w tablicy to [y, x] = [50, 100]
# print("Wartość elementu tablicy im2.bmp o adresie (100, 50):", t_im2[50, 100])
#
# print("\n========== im3.bmp ==========")
# # Wczytanie obrazu im3.bmp
# im3 = Image.open("im3.bmp")
# print("Tryb obrazu im3.bmp:", im3.mode)
# print("Rozmiar obrazu im3.bmp:", im3.size)
#
# # Konwersja na tablicę
# t_im3 = np.asarray(im3)
# print("Rozmiar tablicy obrazu im3.bmp:", t_im3.shape)
# print("Wymiar tablicy im3.bmp:", t_im3.ndim)
#
# print("Wartość piksela obrazu im3.bmp o adresie (100, 50):", im3.getpixel((100, 50)))
# # Lub z tablicy [y, x]:
# print("Wartość z tablicy im3.bmp [50, 100]:", t_im3[50, 100])


# ===============================
# def rgb_to_cmyk(rgb_array):
#     rgb = rgb_array.astype(float) / 255
#     r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
#     k = 1 - np.max(rgb, axis=2)
#     c = (1 - r - k) / (1 - k + 1e-8)
#     m = (1 - g - k) / (1 - k + 1e-8)
#     y = (1 - b - k) / (1 - k + 1e-8)
#     c[np.isnan(c)] = 0
#     m[np.isnan(m)] = 0
#     y[np.isnan(y)] = 0
#     cmyk = np.stack((c, m, y, k), axis=2) * 255
#     return cmyk.astype(np.uint8)
#
# def zlicz_piksele_wartosc(kanal, wartosc):
#     """Zlicza piksele o określonej wartości w kanale"""
#     licznik = 0
#     h, w = kanal.shape
#     for i in range(h):
#         for j in range(w):
#             if kanal[i, j] == wartosc:
#                 licznik += 1
#     return licznik
#
# # Wczytanie obrazu batman1.png
# batman1 = Image.open("batman1.png")
# print("Tryb batman1:", batman1.mode)
# print("Rozmiar batman1:", batman1.size)
#
# # Konwersja do RGB jeśli potrzeba (na wypadek gdyby był RGBA)
# if batman1.mode == "RGBA":
#     batman1 = batman1.convert("RGB")
#
# # Konwersja na tablicę RGB
# t_rgb = np.asarray(batman1).astype(np.uint8)
# print("Kształt tablicy RGB:", t_rgb.shape)
#
# # Konwersja RGB do CMYK
# t_cmyk = rgb_to_cmyk(t_rgb)
# print("Kształt tablicy CMYK:", t_cmyk.shape)
#
# # Wyodrębnienie poszczególnych kanałów
# t_c = t_cmyk[:, :, 0]  # Kanał C (Cyan)
# t_m = t_cmyk[:, :, 1]  # Kanał M (Magenta)
# t_y = t_cmyk[:, :, 2]  # Kanał Y (Yellow)
# t_k = t_cmyk[:, :, 3]  # Kanał K (Black)
#
# print("\n========== Zliczanie pikseli o wartości 20 ==========")
#
# # Zliczanie pikseli o wartości 20 na każdym kanale
# liczba_C_20 = zlicz_piksele_wartosc(t_c, 20)
# liczba_M_20 = zlicz_piksele_wartosc(t_m, 20)
# liczba_Y_20 = zlicz_piksele_wartosc(t_y, 20)
# liczba_K_20 = zlicz_piksele_wartosc(t_k, 20)
#
# print(f"Liczba pikseli o wartości 20 na kanale C jest równa: {liczba_C_20}")
# print(f"Liczba pikseli o wartości 20 na kanale M jest równa: {liczba_M_20}")
# print(f"Liczba pikseli o wartości 20 na kanale Y jest równa: {liczba_Y_20}")
# print(f"Liczba pikseli o wartości 20 na kanale K jest równa: {liczba_K_20}")
#
# # Alternatywnie, szybsza metoda z NumPy:
# print("\n========== Weryfikacja (metoda NumPy) ==========")
# print(f"Kanał C (wartość 20): {np.sum(t_c == 20)}")
# print(f"Kanał M (wartość 20): {np.sum(t_m == 20)}")
# print(f"Kanał Y (wartość 20): {np.sum(t_y == 20)}")
# print(f"Kanał K (wartość 20): {np.sum(t_k == 20)}")

# =============================
# def rysuj_po_skosie_szare(h, w, a, b):
#     t = (h, w)
#     tab = np.zeros(t, dtype=np.uint8)
#     for i in range(h):
#         for j in range(w):
#             tab[i, j] = (a*i + b*j) % 256
#     return tab
#
# def statystyki(im):
#     s = stat.Stat(im)
#     print("extrema ", s.extrema)
#     print("count ", s.count)
#     print("mean ", s.mean)
#     print("rms ", s.rms)
#     print("median ", s.median)
#     print("stddev ", s.stddev)
#
# bek4 = Image.open("bek4.png")
# print("Tryb bek4:", bek4.mode)
# print("Rozmiar bek4:", bek4.size)
#
# w, h = bek4.size
# print(f"Szerokość (w): {w}, Wysokość (h): {h}")
#
# kanal_alfa = rysuj_po_skosie_szare(h, w, 30, 20)
# print("Kształt kanału alfa:", kanal_alfa.shape)
#
# obraz_alfa = Image.fromarray(kanal_alfa, mode='L')
# print("Tryb obrazu alfa:", obraz_alfa.mode)
# obraz_alfa.save("kanal_alfa.png")
#
#
# t_bek4 = np.asarray(bek4).astype(np.uint8)
# print("Kształt tablicy bek4 RGB:", t_bek4.shape)
#
# obraz_rgba = np.dstack((t_bek4, kanal_alfa))
# print("Kształt tablicy RGBA:", obraz_rgba.shape)
#
# obraz_wynikowy = Image.fromarray(obraz_rgba, mode='RGBA')
# print("\nTryb obrazu wynikowego:", obraz_wynikowy.mode)
# print("Rozmiar obrazu wynikowego:", obraz_wynikowy.size)
#
# obraz_wynikowy.save("bek4_rgba.png")
#
# print("\n========== Statystyki obrazu RGBA ==========")
# statystyki(obraz_wynikowy)
#
# s = stat.Stat(obraz_wynikowy)
# mediana = s.median
#
# print(f"Mediana otrzymanego obrazu RGBA: {mediana}")
# print(f"Mediana kanału R: {mediana[0]}")
# print(f"Mediana kanału G: {mediana[1]}")
# print(f"Mediana kanału B: {mediana[2]}")
# print(f"Mediana kanału A: {mediana[3]}")
#
#
# obraz_wynikowy.show()

# =================================
def statystyki(im, nazwa):
    s = stat.Stat(im)
    print(f"\n========== Statystyki obrazu {nazwa} ==========")
    print("Tryb:", im.mode)
    print("Rozmiar:", im.size)
    print("extrema ", s.extrema)  # max i min
    print("count ", s.count)  # zlicza
    print("mean ", s.mean)  # średnia
    print("rms ", s.rms)  # pierwiastek średniokwadratowy
    print("median ", s.median)  # mediana
    print("stddev ", s.stddev)  # odchylenie standardowe
    return s

# Wczytanie i analiza bek1.png
bek1 = Image.open("bek1.png")
s_bek1 = statystyki(bek1, "bek1.png")

# Wczytanie i analiza bek3.png
bek3 = Image.open("bek3.png")
s_bek3 = statystyki(bek3, "bek3.png")

# Wczytanie i analiza bek4.png
bek4 = Image.open("bek4.png")
s_bek4 = statystyki(bek4, "bek4.png")

# Podsumowanie odpowiedzi
print("\n" + "="*60)
print("ODPOWIEDZI:")
print("="*60)
print(f"Odchylenie standardowe pikseli obrazu bek1.png: {s_bek1.stddev}")
print(f"Mediana pikseli obrazu bek4.png: {s_bek4.median}")
print(f"Średnia pikseli obrazu bek3.png: {s_bek3.mean}")