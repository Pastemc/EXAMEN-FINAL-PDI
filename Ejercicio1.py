import cv2
import matplotlib.pyplot as plt

# Lee la imagen desde el archivo
image = cv2.imread('nel.jpg')

# Convierte la imagen a escala de grises
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Guarda la imagen en escala de grises
cv2.imwrite('nel.jpg', gray_image)

# Convierte la imagen de BGR a RGB para mostrarla correctamente con matplotlib
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Crea los subplots
plt.figure(figsize=(10, 5))

# Muestra la imagen original en el primer subplot
plt.subplot(1, 2, 1)
plt.imshow(image_rgb)
plt.title('Imagen Original')
plt.axis('off')

# Muestra la imagen en escala de grises en el segundo subplot
plt.subplot(1, 2, 2)
plt.imshow(gray_image, cmap='gray')
plt.title('Imagen en Escala de Grises')
plt.axis('off')

# Muestra las imágenes
plt.show()
