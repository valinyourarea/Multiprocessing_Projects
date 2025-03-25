# src/benchmark.py
import matplotlib.pyplot as plt
import serial_version
import parallel_version

def main():
    image_dir = "../images"
    out_serial = "../output/serial"
    
    # Versión serial
    time_serial = serial_version.run_serial(image_dir, out_serial)
    print(f"Tiempo serial: {time_serial:.2f} s")
    
    # Versión paralela con 1,2,3,4,6 procesos
    process_counts = [1, 2, 3, 4, 6]
    times_parallel = []
    
    for p in process_counts:
        out_parallel = f"../output/parallel_{p}"
        t_par = parallel_version.run_parallel(image_dir, out_parallel, processes=p)
        times_parallel.append(t_par)
        print(f"Tiempo paralelo ({p} procesos): {t_par:.2f} s")
    
    # Graficar
    plt.figure(figsize=(8,5))
    # Graficamos el serial como si fuera "1 proceso"
    plt.plot([1], [time_serial], 'ro-', label="Serial")
    # Graficamos los tiempos paralelos
    plt.plot(process_counts, times_parallel, 'bo-', label="Paralelo")
    
    plt.title("Tiempo de ejecución vs Número de procesos")
    plt.xlabel("Número de procesos")
    plt.ylabel("Tiempo (s)")
    plt.grid(True)
    plt.legend()
    plt.savefig("benchmark.png")
    plt.show()

if __name__ == "__main__":
    main()
