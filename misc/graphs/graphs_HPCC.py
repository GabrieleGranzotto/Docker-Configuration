import matplotlib.pyplot as plt
plt.style.use('ggplot')

# HPL cluster results
Nb = [128, 192, 256]
docker_cluster_6 = [5.076, 4.538, 4.266]
vm_cluster_6 = [3.760, 3.558, 3.437]
docker_cluster_10 = [4.348, 4.106, 4.011]
vm_cluster_10 = [4.004, 3.857, 3.811]

plt.plot(Nb, docker_cluster_6, marker='o', markersize=8,linestyle='-', color='blue')
plt.plot(Nb, vm_cluster_6, marker='o', markersize=8, linestyle='-', color='orange')
plt.plot(Nb, docker_cluster_10, marker='s', markersize=8, linestyle='--', color='blue')
plt.plot(Nb, vm_cluster_10, marker='s', markersize=8, linestyle='--', color='orange')

plt.xlabel('NB')
plt.ylabel('Gflops')
plt.title("HPL cluster results [Gflops]")
plt.legend(["docker cluster 6'000 Ns","vm cluster 6'000 Ns", "docker cluster 10'000 Ns", "vm cluster 10'000 Ns"])
plt.grid(True)
plt.savefig("./graphs/HPL_cluster_results.png", dpi=400)


# HPL cluster time results
plt.figure()
t_docker_cluster_6 = [28.38, 31.75, 33.77]
t_vm_cluster_6 = [38.31, 40.49, 41.92]
t_docker_cluster_10 = [153.37, 162.38, 166.27]
t_vm_cluster_10 = [166.55, 172.88, 174.97]

plt.plot(Nb, t_docker_cluster_6, marker='o', markersize=8,linestyle='-', color='blue')
plt.plot(Nb, t_vm_cluster_6, marker='o', markersize=8, linestyle='-', color='orange')
plt.plot(Nb, t_docker_cluster_10, marker='s', markersize=8, linestyle='--', color='blue')
plt.plot(Nb, t_vm_cluster_10, marker='s', markersize=8, linestyle='--', color='orange')

plt.xlabel('NB')
plt.ylabel('time')
plt.title("HPL cluster time [seconds]")
plt.legend(["docker cluster 6'000 Ns","vm cluster 6'000 Ns", "docker cluster 10'000 Ns","vm cluster 10'000 Ns"])
plt.grid(True)
plt.savefig("./graphs/HPL_cluster_time.png", dpi=400)


# HPL results
plt.figure()
docker_6 = [3.676, 3.5, 3.391]
vm_6 = [3.837, 3.774, 3.586]

plt.plot(Nb, docker_6, marker='o', markersize=8,linestyle='-', color='blue')
plt.plot(Nb, vm_6, marker='o', markersize=8, linestyle='-', color='orange')
plt.plot(Nb, docker_cluster_6, marker='s', markersize=8,linestyle='--', color='blue')
plt.plot(Nb, vm_cluster_6, marker='s', markersize=8, linestyle='--', color='orange')

plt.xlabel('NB')
plt.ylabel('Gflops')
plt.title("HPL results [Gflops]")
plt.legend(["docker","vm", "docker cluster", "vm cluster"])
plt.grid(True)
plt.savefig("./graphs/HPL_results.png", dpi=400)


# HPL time results
plt.figure()
t_docker_6 = [39.19, 41.16, 42.48]
t_vm_6 = [37.55, 38.17, 40.17]

plt.plot(Nb, t_docker_6, marker='o', markersize=8,linestyle='-', color='blue')
plt.plot(Nb, t_vm_6, marker='o', markersize=8, linestyle='-', color='orange')
plt.plot(Nb, t_docker_cluster_6, marker='s', markersize=8,linestyle='--', color='blue')
plt.plot(Nb, t_vm_cluster_6, marker='s', markersize=8, linestyle='--', color='orange')

plt.xlabel('NB')
plt.ylabel('time')
plt.title("HPL time [seconds]")
plt.legend(["docker","vm", "docker cluster", "vm cluster"])
plt.grid(True)
plt.savefig("./graphs/HPL_time.png", dpi=400)


# StarSTREAM Triad results
plt.figure()
sst_docker = 5.524
sst_vm = 5.23
sst_docker_cluster = 1.819
sst_vm_cluster = 1.787

plt.bar(['docker', 'vm', 'docker cluster', 'vm cluster'], [sst_docker, sst_vm, sst_docker_cluster, sst_vm_cluster], color=['blue', 'orange', 'blue', 'orange'])
plt.xlabel('Implementation')
plt.ylabel('GB/s')
plt.title("StarSTREAM Triad [GB/s]")
plt.grid(True)
plt.savefig("./graphs/StarSTREAM_Triad.png", dpi=400)


# MPI Random Access results
plt.figure()
sra_docker = 2.27E-02
sra_vm = 1.96E-02
sra_docker_cluster = 3.43E-03
sra_vm_cluster = 1.82E-03
plt.bar(['docker', 'vm', 'docker cluster', 'vm cluster'], [sra_docker, sra_vm, sra_docker_cluster, sra_vm_cluster], color=['blue', 'orange', 'blue', 'orange'])
plt.xlabel('Implementation')
plt.ylabel('GUPs')
plt.title("MPI Random Access [GUPs]")
plt.grid(True)
plt.savefig("./graphs/MPI_Random_Access.png", dpi=400)


# StarDGEMM results
plt.figure()
sdgemm_docker = 1.876
sdgemm_vm = 1.817
sdgemm_docker_cluster = 0.717
sdgemm_vm_cluster = 0.695
plt.bar(['docker', 'vm', 'docker cluster', 'vm cluster'], [sdgemm_docker, sdgemm_vm, sdgemm_docker_cluster, sdgemm_vm_cluster], color=['blue', 'orange', 'blue', 'orange'])
plt.xlabel('Implementation')
plt.ylabel('Gflops')
plt.title("StarDGEMM [Gflops]")
plt.grid(True)
plt.savefig("./graphs/StarDGEMM.png", dpi=400)


# MPIFFT results
plt.figure()
mpifft_docker = 2.399
mpifft_vm = 2.494
mpifft_docker_cluster = 2.546
mpifft_vm_cluster = 0.818
plt.bar(['docker', 'vm', 'docker cluster', 'vm cluster'], [mpifft_docker, mpifft_vm, mpifft_docker_cluster, mpifft_vm_cluster], color=['blue', 'orange', 'blue', 'orange'])
plt.xlabel('Implementation')
plt.ylabel('Gflops')
plt.title("MPIFFT [Gflops]")
plt.grid(True)
plt.savefig("./graphs/MPIFFT.png", dpi=400)
