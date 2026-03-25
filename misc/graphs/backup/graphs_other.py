import matplotlib.pyplot as plt
from matplotlib.colors import LightSource
from matplotlib import cm, cbook
import numpy as np
import pandas as pd
plt.style.use('ggplot')

# stress-ng cpu stress test results
t = [60, 120, 180]
speed_docker1 = [2126.83, 2010.17, 2006.96]
speed_docker2 = [953.83, 905.20, 895.66]
speed_docker3 = [899.61, 872.50, 868.87]
speed_vm1 = [1922.99, 1898.73, 1913.83]
speed_vm2 = [933.34, 935.49, 950.11]
speed_vm3 = [931.67, 921.35, 942.81]

plt.plot(t, speed_docker1, marker='o', label='docker1', color='blue')
plt.plot(t, speed_docker2, marker='o', label='docker2', color='blue')
plt.plot(t, speed_docker3, marker='o', label='docker3', color='blue')
plt.plot(t, speed_vm1, marker='s', label='vm1', color='orange')
plt.plot(t, speed_vm2, marker='s', label='vm2', color='orange')
plt.plot(t, speed_vm3, marker='s', label='vm3', color='orange')
plt.title('stress-ng CPU Results')
plt.ylim(300, 2200)
plt.xlabel('Time [seconds]')
plt.ylabel('Speed [bogo ops/second]')
plt.legend(ncol=2)
plt.grid(True)
plt.savefig('graphs/stressng_cpu_stress_test.png', dpi=400)

# same thing but for memory stress test
speed_docker1_mem = [94251.05, 90419.46, 95237.23]
speed_docker2_mem = [21135.92, 35621.07, 33198.91]
speed_docker3_mem = [21103.33, 35432.80, 31075.28]
speed_vm1_mem = [80026.08, 80493.97, 82890.64]
speed_vm2_mem = [18809.48, 37787.45, 36168.29]
speed_vm3_mem = [18330.98, 37033.63, 21436.62]    
plt.figure()
plt.plot(t, speed_docker1_mem, marker='o', label='docker1', color='blue')
plt.plot(t, speed_docker2_mem, marker='o', label='docker2', color='blue')
plt.plot(t, speed_docker3_mem, marker='o', label='docker3', color='blue')
plt.plot(t, speed_vm1_mem, marker='s', label='vm1', color='orange')
plt.plot(t, speed_vm2_mem, marker='s', label='vm2', color='orange')
plt.plot(t, speed_vm3_mem, marker='s', label='vm3', color='orange')
plt.title('stress-ng Memory Results')
plt.ylim(15000, 100000)
plt.xlabel('Time [seconds]')
plt.ylabel('Speed [bogo ops/second]')
plt.yticks(rotation=60)
plt.legend(ncol=2)
plt.grid(True)
plt.savefig('graphs/stressng_memory_stress_test.png', dpi=400)

# Sysbench CPU Results
plt.figure()
prime_number = [10_000, 50_000, 100_000, 150_000]
cpu_speed_docker = [2683.59, 297.81, 113.81, 65.01]
cpu_speed_vm = [2634.30, 294.02, 114.09, 64.21]
plt.plot(prime_number, cpu_speed_docker, marker='o', label='docker', color='blue')
plt.plot(prime_number, cpu_speed_vm, marker='s', label='vm', color='orange')
plt.title("Sysbench CPU test")
plt.ylabel("Speed [event/seconds]")
plt.xlabel("prime numbers")
plt.yticks(rotation=60)
plt.legend()
plt.grid(True)
plt.savefig('graphs/sysbench_cpu.png', dpi=400)

# Sysbench Memory Results
plt.figure()
total_size = [1024, 2048, 10240, 20480, 40960, 61440]
memory_speed_docker = [41270.73, 43289.60, 45250.63, 45388.32, 44181.91, 44224.66]
memory_speed_vm = [35435.37, 32085.42, 40831.94, 43146.28, 42422.50, 42794.13]
plt.plot(total_size, memory_speed_docker, marker='o', label='docker', color='blue')
plt.plot(total_size, memory_speed_vm, marker='s', label='vm', color='orange')
plt.title("Sysbench Memory test")
plt.ylabel("Speed [MiB/s]")
plt.xlabel("Total data size [MiB]")
plt.yticks(rotation=60)
plt.legend()
plt.grid(True)
plt.savefig('graphs/sysbench_memory.png', dpi=400)

# iperf3 data
plt.figure()
docker_iperf3 = 46.6
vm_iperf3 = 3.26
plt.bar(["docker", "vm"],[docker_iperf3, vm_iperf3], color=["blue", "orange"])
plt.title("iperf3 comunication test")
plt.xlabel("Implementation")
plt.ylabel("Bitrate [Gbits/s]")
plt.grid(True)
plt.savefig('graphs/iperf3.png', dpi=400)

#iozone data
plt.figure()
z_column = 'random read'    
output_filename = "graphs/docker_iozone_3d_plot.png"
default_cmap = 'RdYlBu_r'
elevation = 35  # angolo di elevazione della visuale
angle = 120
base_azimuth = -60
azimuth = angle + base_azimuth   # angolo azimutale della visuale

df_iozone = pd.read_csv("risultati_benchmark/docker_iozone.csv")
df_iozone = df_iozone.pivot(index="kB", columns="reclen", values=z_column).fillna(average:=df_iozone[z_column].mean())

z = df_iozone.values
x = df_iozone.columns.values
y = df_iozone.index.values
X, Y = np.meshgrid(x, y)

fig, ax = plt.subplots(figsize=(12, 8), subplot_kw=dict(projection='3d'))

# Imposta etichette
ax.set_xlabel('Record Length (reclen)')
ax.set_ylabel('File Size (kB)')
ax.set_zlabel(z_column)
ax.set_title(f'3D Surface Plot: {z_column} vs. kB and reclen')
ax.view_init(elev=elevation, azim=azimuth)
# Creiamo la fonte di luce (come nell'esempio)
ls = LightSource(270, 45)

# Calcoliamo l'ombreggiatura. 
# Usiamo 'linear' per mappare i dati Z ai colori prima dell'ombreggiatura
# (potrebbe essere necessario convertire in float)
rgb = ls.shade(z.astype(float), cmap=plt.get_cmap(default_cmap), vert_exag=0.1, blend_mode='soft')

# Disegniamo la superficie
surf = ax.plot_surface(X, Y, z, 
                        rstride=1,  # Usa tutti i dati (nessun salto di riga)
                        cstride=1,  # Usa tutti i dati (nessun salto di colonna)
                        facecolors=rgb,       # Colori calcolati dall'ombreggiatura
                        linewidth=0,          # Nessun bordo tra le facce
                        antialiased=False,    # Più veloce, meno smussato
                        shade=False)          # Disattiva ombreggiatura default

# Aggiungi una color bar per mappare i colori all'altezza Z
m = cm.ScalarMappable(cmap=plt.get_cmap(default_cmap))
m.set_array(z)
fig.colorbar(m, shrink=0.5, aspect=10, ax=ax, label=f'Valore {z_column}')

# Salviamo il file
plt.savefig(output_filename, bbox_inches='tight', dpi=400)
plt.close()