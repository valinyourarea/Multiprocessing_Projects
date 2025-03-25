# src/serial_version.py
import os
import time
import cv2
from filters import grayscale, blur, edge_detection

def process_image_serial(img_path, output_dir):
    img = cv2.imread(img_path)
    if img is None:
        return
    base_name = os.path.splitext(os.path.basename(img_path))[0]
    
    # Filtros
    gray = grayscale(img)
    blurred = blur(img)
    edges = edge_detection(img)
    
    # Guardamos cada resultado
    cv2.imwrite(os.path.join(output_dir, f"{base_name}_gray.jpg"), gray)
    cv2.imwrite(os.path.join(output_dir, f"{base_name}_blur.jpg"), blurred)
    cv2.imwrite(os.path.join(output_dir, f"{base_name}_edges.jpg"), edges)

def run_serial(image_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    start = time.perf_counter()
    
    for filename in os.listdir(image_dir):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            img_path = os.path.join(image_dir, filename)
            process_image_serial(img_path, output_dir)
    
    end = time.perf_counter()
    return end - start

if __name__ == "__main__":
    t_serial = run_serial("../images", "../output/serial")
    print(f"Tiempo total (serial): {t_serial:.2f} s")
