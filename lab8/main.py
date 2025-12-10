import numpy as np
from PIL import Image, ImageOps
from PIL import ImageStat as stat
import matplotlib.pyplot as plt


def statystyki(obraz):
    s = stat.Stat(obraz)
    print("extrema ", s.extrema)  # max i min
    print("count ", s.count)  # zlicza
    print("mean ", s.mean)  # srednia
    print("median ", s.median)  # mediana
    print("stddev ", s.stddev)  # odchylenie standardowe

def histogram_norm(obraz):
    hist = obraz.histogram()
    n_pikseli = obraz.size[0] * obraz.size[1]
    hist_norm = [h / n_pikseli for h in hist]

    return hist_norm

def histogram_cumul(obraz):
    hist_norm = histogram_norm(obraz)
    hist_kumul = []
    suma = 0
    for h in hist_norm:
        suma += h
        hist_kumul.append(suma)

    return hist_kumul


def histogram_equalization(obraz):
    hist_kumul = histogram_cumul(obraz)
    img_array = np.array(obraz)
    equalized_array = np.zeros_like(img_array)
    for i in range(img_array.shape[0]):
        for j in range(img_array.shape[1]):
            p = img_array[i, j]
            equalized_array[i, j] = int(255 * hist_kumul[p])

    return Image.fromarray(equalized_array.astype(np.uint8))

# ------------------------ Zadanie 1 ------------------------ #
obrazek = Image.open("obraz.png")
print("tryb ", obrazek.mode, "\n")
obrazek = obrazek.convert("L")
print("tryb ", obrazek.mode, " (po konwersji)")


# ------------------------ Zadanie 2 ------------------------ #
statystyki(obrazek)
hist = obrazek.histogram()
plt.title("histogram")
plt.bar(range(256), hist[:])
plt.show()

# ------------------------ Zadanie 3 ------------------------ #
hist_norm = histogram_norm(obrazek)
plt.figure()
plt.title("Histogram znormalizowany")
plt.bar(range(256), hist_norm)
plt.xlabel("Wartość piksela")
plt.ylabel("Częstość znormalizowana")
plt.show()

# ------------------------ Zadanie 4 ------------------------ #
hist_kumul = histogram_cumul(obrazek)
plt.figure()
plt.title("Histogram skumulowany")
plt.bar(range(256), hist_kumul)
plt.xlabel("Wartość piksela")
plt.ylabel("Skumulowana częstość")
plt.show()

# ------------------------ Zadanie 5 ------------------------ #
obraz_equalized = histogram_equalization(obrazek)
obraz_equalized.save("equalized.png")

hist_eq = obraz_equalized.histogram()
plt.title("histogram - po wyrównaniu")
plt.bar(range(256), hist_eq[:])
plt.show()

# ------------------------ Zadanie 6 ------------------------ #
obraz_equalized1 = ImageOps.equalize(obrazek, mask=None)
hist_eq1 = obraz_equalized1.histogram()
obraz_equalized1.save("equalized1.png")

#6.1
#Obrazy są praktycznie identyczne. Różnica wynika z zaokląglenia w obliczeniach.
#
#6.2
plt.figure(figsize=(10, 6))
plt.title("Porównanie histogramów")
plt.bar(range(256), hist_eq[:], color='blue', alpha=0.5, label='funkcja histogram_equalization(obraz)',)
plt.bar(range(256), hist_eq1[:], color='red', alpha=0.5, label='metoda equalize')
plt.xlabel("Wartość piksela")
plt.ylabel("Liczba pikseli")
plt.legend()
plt.show()
#
#6.3
statystyki(obraz_equalized)
statystyki(obraz_equalized1)