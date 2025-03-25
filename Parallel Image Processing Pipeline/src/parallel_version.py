# src/parallel_version.py
import os
import time
import cv2
from multiprocessing import Pool
from filters import grayscale, blur, edge_detection

def process_single_image(args):
    """Función que procesa una imagen (usada por Pool.map)."""
    img_path, output_dir = args
    img = cv2.imread(img_path)
    if img is None:
        return
    
    base_name = os.path.splitext(os.path.basename(img_path))[0]
    gray = grayscale(img)
    blurred = blur(img)
    edges = edge_detection(img)
    
    cv2.imwrite(os.path.join(output_dir, f"{base_name}_gray.jpg"), gray)
    cv2.imwrite(os.path.join(output_dir, f"{base_name}_blur.jpg"), blurred)
    cv2.imwrite(os.path.join(output_dir, f"{base_name}_edges.jpg"), edges)

def run_parallel(image_dir, output_dir, processes=2):
    os.makedirs(output_dir, exist_ok=True)
    tasks = []
    
    for filename in os.listdir(image_dir):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            img_path = os.path.join(image_dir, filename)
            tasks.append((img_path, output_dir))
    
    start = time.perf_counter()
    
    with Pool(processes=processes) as pool:
        pool.map(process_single_image, tasks)
    
    end = time.perf_counter()
    return end - start

if __name__ == "__main__":
    for p in [1, 2, 3, 4, 6]:
        t_par = run_parallel("../images", f"../output/parallel_{p}", processes=p)
        print(f"Tiempo con {p} procesos: {t_par:.2f} s")
