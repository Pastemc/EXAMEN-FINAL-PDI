import cv2
import matplotlib.pyplot as plt

# Lee la imagen desde el archivo
image = cv2.imread('ok.jpg')

# Cambia el tamaño de la imagen a 300x300 píxeles
resized_image = cv2.resize(image, (300, 300))

# Guarda la imagen redimensionada
cv2.imwrite('ok.jpg', resized_image)

# Convierte la imagen de BGR a RGB para mostrarla correctamente con matplotlib
resized_image_rgb = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)

# Muestra la imagen original y la imagen redimensionada
plt.figure(figsize=(10, 5))

# Muestra la imagen original
plt.subplot(1, 2, 1)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.title('Imagen Original')
plt.axis('off')

# Muestra la imagen redimensionada
plt.subplot(1, 2, 2)
plt.imshow(resized_image_rgb)
plt.title('Imagen Redimensionada (300x300)')
plt.axis('off')

# Muestra las imágenes
plt.show()
