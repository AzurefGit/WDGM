from PIL import Image, ImageFilter
import matplotlib.pyplot as plt
import numpy as np


obraz = Image.open('obraz.png')

def filtruj(obraz, kernel, scale):
    if isinstance(kernel, list):
        kernel = tuple(kernel)

    k = int(np.sqrt(len(kernel)))


    filter_kernel = ImageFilter.Kernel(
        size=(k, k),
        kernel=kernel,
        scale=scale
    )

    return obraz.filter(filter_kernel)



print("=== Zadanie 2: Filtr BLUR ===")
obraz_blur_gotowy = obraz.filter(ImageFilter.BLUR)

blur_kernel = [
    1, 1, 1, 1, 1,
    1, 0, 0, 0, 1,
    1, 0, 0, 0, 1,
    1, 0, 0, 0, 1,
    1, 1, 1, 1, 1
]
blur_scale = 16

obraz_blur_wlasny = filtruj(obraz, blur_kernel, blur_scale)

fig1, axes1 = plt.subplots(1, 3, figsize=(15, 5))
axes1[0].imshow(obraz, cmap='gray')
axes1[0].set_title('Obraz oryginalny')
axes1[0].axis('off')

axes1[1].imshow(obraz_blur_gotowy, cmap='gray')
axes1[1].set_title('BLUR - gotowy filtr')
axes1[1].axis('off')

axes1[2].imshow(obraz_blur_wlasny, cmap='gray')
axes1[2].set_title('BLUR - funkcja filtruj()')
axes1[2].axis('off')

plt.tight_layout()
plt.savefig('fig1_blur.png', dpi=150, bbox_inches='tight')
print("Zapisano fig1_blur.png")
print("Porównanie BLUR: Oba filtry dają podobny efekt rozmycia obrazu.\n")

print("=== Zadanie 3: Filtr CONTOUR ===")

obraz_contour_gotowy = obraz.filter(ImageFilter.CONTOUR)

contour_kernel = [
    -1, -1, -1,
    -1, 8, -1,
    -1, -1, -1
]
contour_scale = 1

obraz_contour_wlasny = filtruj(obraz, contour_kernel, contour_scale)

fig2, axes2 = plt.subplots(1, 3, figsize=(15, 5))
axes2[0].imshow(obraz, cmap='gray')
axes2[0].set_title('Obraz oryginalny')
axes2[0].axis('off')

axes2[1].imshow(obraz_contour_gotowy, cmap='gray')
axes2[1].set_title('CONTOUR - gotowy filtr')
axes2[1].axis('off')

axes2[2].imshow(obraz_contour_wlasny, cmap='gray')
axes2[2].set_title('CONTOUR - funkcja filtruj()')
axes2[2].axis('off')

plt.tight_layout()
plt.savefig('fig2_contour.png', dpi=150, bbox_inches='tight')
print("Zapisano fig2_contour.png")
print("Porównanie CONTOUR: Oba filtry wykrywają krawędzie w podobny sposób.\n")

print("=== Zadanie 4: Filtry EMBOSS i SOBEL ===")

obraz_L = obraz.convert('L')

obraz_emboss = obraz_L.filter(ImageFilter.EMBOSS)

sobel1_kernel = [-1, 0, 1, -2, 0, 2, -1, 0, 1]
sobel1_scale = 1
obraz_sobel1 = filtruj(obraz_L, sobel1_kernel, sobel1_scale)

sobel2_kernel = [-1, -2, -1, 0, 0, 0, 1, 2, 1]
sobel2_scale = 1
obraz_sobel2 = filtruj(obraz_L, sobel2_kernel, sobel2_scale)

fig3, axes3 = plt.subplots(2, 2, figsize=(12, 12))

axes3[0, 0].imshow(obraz_L, cmap='gray')
axes3[0, 0].set_title('Obraz oryginalny (tryb L)')
axes3[0, 0].axis('off')

axes3[0, 1].imshow(obraz_emboss, cmap='gray')
axes3[0, 1].set_title('Filtr EMBOSS')
axes3[0, 1].axis('off')

axes3[1, 0].imshow(obraz_sobel1, cmap='gray')
axes3[1, 0].set_title('SOBEL1 (krawędzie pionowe)')
axes3[1, 0].axis('off')

axes3[1, 1].imshow(obraz_sobel2, cmap='gray')
axes3[1, 1].set_title('SOBEL2 (krawędzie poziome)')
axes3[1, 1].axis('off')

plt.tight_layout()
plt.savefig('fig2.png', dpi=150, bbox_inches='tight')
print("Zapisano fig2.png")

print("\n=== ANALIZA RÓŻNIC ===")
print("1. EMBOSS: Tworzy efekt 3D/wytłoczenia, podkreśla krawędzie z efektem cienia.")
print("   Jasne obszary po jednej stronie krawędzi, ciemne po drugiej.")
print()
print("2. SOBEL1 (pionowy): Wykrywa głównie krawędzie PIONOWE (zmiany intensywności")
print("   w poziomie). W przypadku kości dłoni - widoczne są kontury kości biegnące")
print("   pionowo.")
print()
print("3. SOBEL2 (poziomy): Wykrywa głównie krawędzie POZIOME (zmiany intensywności")
print("   w pionie). Wyraźnie widoczne są stawy palców i połączenia kości biegnące")
print("   poziomo.")
print()
print("4. Różnice:")
print("   - EMBOSS daje efekt artystyczny/3D")
print("   - SOBEL1 i SOBEL2 są komplementarne - każdy wykrywa inny kierunek gradientu")
print("   - Połączenie SOBEL1 i SOBEL2 dałoby pełną detekcję krawędzi we wszystkich")
print("     kierunkach (często używa się: sqrt(SOBEL1² + SOBEL2²))")

print("\n=== Wszystkie zadania wykonane! ===")
plt.show()