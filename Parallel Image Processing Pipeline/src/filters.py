# src/filters.py
import cv2

def grayscale(img):
    """Convierte la imagen a escala de grises."""
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def blur(img):
    """Aplica un desenfoque gaussiano."""
    return cv2.GaussianBlur(img, (5, 5), 0)

def edge_detection(img):
    """Aplica un detector de bordes (Canny)."""
    return cv2.Canny(img, 100, 200)
