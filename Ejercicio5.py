import cv2
import matplotlib.pyplot as plt

# Lee la imagen en color desde el archivo
image = cv2.imread('cara.jpg')

# Convierte la imagen a escala de grises
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplica la ecualización de histograma
equalized_image = cv2.equalizeHist(gray_image)

# Guarda la imagen resultante
cv2.imwrite('cara.jpg', equalized_image)

# Convierte la imagen original a RGB para mostrarla correctamente con matplotlib
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Crea los subplots
plt.figure(figsize=(20, 5))

# Muestra la imagen original en color en el primer subplot
plt.subplot(1, 4, 1)
plt.imshow(image_rgb)
plt.title('Imagen Original en Color')
plt.axis('off')

# Muestra la imagen en escala de grises en el segundo subplot
plt.subplot(1, 4, 2)
plt.imshow(gray_image, cmap='gray')
plt.title('Imagen en Escala de Grises')
plt.axis('off')

# Muestra la imagen ecualizada en el tercer subplot
plt.subplot(1, 4, 3)
plt.imshow(equalized_image, cmap='gray')
plt.title('Imagen Ecualizada')
plt.axis('off')

# Muestra el histograma de la imagen ecualizada en el cuarto subplot
plt.subplot(1, 4, 4)
plt.hist(equalized_image.ravel(), 256, [0, 256])
plt.title('Histograma de la Imagen Ecualizada')

# Muestra las imágenes y el histograma
plt.show()
