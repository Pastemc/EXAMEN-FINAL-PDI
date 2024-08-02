import cv2
import matplotlib.pyplot as plt

# Lee la imagen desde el archivo
image = cv2.imread('moneda.jpeg')

# Convierte la imagen a escala de grises
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplica el detector de bordes de Canny
edges = cv2.Canny(gray_image, 100, 200)

# Guarda la imagen con los bordes detectados
cv2.imwrite('moneda.jpeg', edges)

# Convierte la imagen de BGR a RGB para mostrarla correctamente con matplotlib
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Crea los subplots
plt.figure(figsize=(15, 5))

# Muestra la imagen original en el primer subplot
plt.subplot(1, 3, 1)
plt.imshow(image_rgb)
plt.title('Imagen Original')
plt.axis('off')

# Muestra la imagen en escala de grises en el segundo subplot
plt.subplot(1, 3, 2)
plt.imshow(gray_image, cmap='gray')
plt.title('Imagen en Escala de Grises')
plt.axis('off')

# Muestra la imagen con los bordes detectados en el tercer subplot
plt.subplot(1, 3, 3)
plt.imshow(edges, cmap='gray')
plt.title('Bordes Detectados (Canny)')
plt.axis('off')

# Muestra las imágenes
plt.show()
