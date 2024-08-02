import cv2
import matplotlib.pyplot as plt

# Lee la imagen desde el archivo
image = cv2.imread('fisi.jpg')

# Aplica un filtro de suavizado gaussiano con un kernel de 5x5
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

# Guarda la imagen suavizada
cv2.imwrite('fisi.jpg', blurred_image)

# Convierte la imagen de BGR a RGB para mostrarla correctamente con matplotlib
blurred_image_rgb = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Crea los subplots
plt.figure(figsize=(10, 5))

# Muestra la imagen original en el primer subplot
plt.subplot(1, 2, 1)
plt.imshow(image_rgb)
plt.title('Imagen Original')
plt.axis('off')

# Muestra la imagen suavizada en el segundo subplot
plt.subplot(1, 2, 2)
plt.imshow(blurred_image_rgb)
plt.title('Imagen Suavizada ')
plt.axis('off')

# Muestra las imágenes
plt.show()
