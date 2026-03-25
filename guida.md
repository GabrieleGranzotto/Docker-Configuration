---
output:
  pdf_document: default
  html_document: default
---
# Guida ai Tool di Benchmark: VM vs. Container

Questa guida analizza i tool di benchmark per isolare le performance di CPU, Memoria, Disco e Rete, e delinea i risultati attesi dal confronto tra un ambiente VM e un ambiente Container.

---

## Guida ai Tool di Benchmark

### 1. MPICH (Gestore MPI)

* **A cosa serve:** Questo non è un benchmark, ma un'implementazione del protocollo MPI (come Open MPI, che hai usato finora). `mpich` fornisce i comandi (come `mpiexec` o `mpirun`) per lanciare un programma su più nodi.
* **Come si usa:** Lo stai già usando! Quando lanci `mpirun -np 6 --hostfile ...`, stai usando un'implementazione MPI per avviare il tuo benchmark.

* **Comando Esempio:**
    ```bash
    # Questo comando usa MPICH (o Open MPI) per lanciare 'il_tuo_programma'
    mpirun -np 6 --hostfile myhosts.txt ./il_tuo_programma
    ```

### 2. stress-ng (Stress Test Generico)

* **A cosa serve:** È un "martello". Serve a stressare al massimo uno o più sottosistemi per vedere se "reggono" e per monitorare il loro comportamento al limite.
* **Come si usa:** Specifichi cosa stressare (cpu, memoria, I/O) e per quanto tempo.

* **Test CPU (2 core al 100%):**
    ```bash
    # Lancia 2 processi che fanno calcoli intensivi per 60 secondi
    stress-ng --cpu 2 --timeout 60s
    ```

* **Test Memoria (Saturazione RAM):**
    ```bash
    # Lancia 2 processi che allocano e usano 1.8GB di RAM totali (900M l'uno)
    stress-ng --vm 2 --vm-bytes 900M --timeout 60s
    ```

### 3. sysbench (Benchmark Sintetico)

* **A cosa serve:** È un benchmark più "scientifico" di `stress-ng`. Fornisce numeri precisi sulle performance di CPU, memoria e I/O, misurando "eventi al secondo" o "banda".
* **Come si usa:** Si divide in due fasi: `prepare` (prepara i file di test) e `run` (esegue il test).

* **Test CPU:**
    ```bash
    # Esegue un test sulla CPU usando 2 thread, per 60 secondi
    sysbench cpu --threads=2 --time=60 run
    ```

* **Test Memoria (Bandwidth):**
    ```bash
    # Misura la velocità della RAM usando 2 thread
    sysbench memory --threads=2 --memory-block-size=1M --memory-total-size=10G run
    ```

### 4. iozone3 (Benchmark I/O Disco)

* **A cosa serve:** È il test definitivo per misurare le performance del tuo "disco". Nel tuo caso, misurerà la velocità del disco virtuale della VM contro l'accesso al filesystem dell'host del container.
* **Come si usa:** È molto complesso, ma la modalità automatica (`-a`) è perfetta.

* **Test Automatico:**
    ```bash
    # Esegue un test I/O completo. 
    # -a = automatico, -g 1G = usa un file di test da 1GB
    iozone -a -g 1G
    ```

### 5. iperf3 (Benchmark di Rete)

* **A cosa serve:** Questo è **il tool più importante per te**. Misura in modo pulito e diretto la larghezza di banda massima e la latenza tra due nodi. Questo isolerà il collo di bottiglia che abbiamo visto con HPCC.
* **Come si usa:** Funziona in modalità client/server.

* **Sul Nodo 1 (es. `worker1`):**
    ```bash
    # Avvia il server iperf3
    iperf3 -s
    ```

* **Sul Nodo 2 (es. `master`):**
    ```bash
    # Avvia il client e si connette al server
    iperf3 -c worker1
    ```

### 6. netcat-openbsd (Utility di Rete)

* **A cosa serve:** È il "coltellino svizzero" per il networking. Non è un benchmark, ma può essere usato per testare la connettività di base. `iperf3` è molto meglio, ma `netcat` è utile per il debug.
* **Come si usa:** Apri una porta su un nodo e invii dati dall'altro.

* **Sul Nodo 1 (es. `worker1`):**
    ```bash
    # Si mette in ascolto sulla porta 1234 e butta via i dati ricevuti
    nc -l -p 1234 > /dev/null
    ```

* **Sul Nodo 2 (es. `master`):**
    ```bash
    # Invia 1GB di dati (1M * 1000 volte) alla porta 1234 del worker1
    dd if=/dev/zero bs=1M count=1000 | nc worker1 1234
    ```

---

## Cosa Aspettarci (L'Ipotesi)

Basandoci sui risultati di HPCC, ecco cosa mi aspetto che questi nuovi test riveleranno:

### 1. CPU (sysbench, stress-ng)
* **Ipotesi:** Performance quasi identiche.
* **Perché:** I nostri test HPL a nodo singolo hanno mostrato una parità quasi perfetta. Sia la VM che il container hanno un accesso molto efficiente ai 2 core fisici. Mi aspetto che la VM sia più stabile e il container marginalmente più veloce, ma la differenza sarà trascurabile (1-5%).

### 2. Memoria (sysbench, stress-ng)
* **Ipotesi:** Container leggermente più veloce.
* **Perché:** I test STREAM e RandomAccess hanno mostrato che i container hanno una larghezza di banda della memoria e una velocità di accesso casuale superiori. `sysbench memory` confermerà questa maggiore larghezza di banda (MB/s).

### 3. I/O Disco (iozone3)
* **Ipotesi:** Container **molto** più veloce.
* **Perché:** Il disco di una VM è un file (es. `.vmdk`). Un container che usa un *bind mount* scrive direttamente sul filesystem host, saltando un intero strato di virtualizzazione. `iozone` mostrerà velocità di scrittura/lettura molto più elevate per il container.

### 4. Rete (iperf3)
* **Ipotesi:** Container **drammaticamente** più veloce.
* **Perché:** **Questo è il tuo risultato chiave.** HPCC ci ha mostrato che la rete delle VM ha una latenza e una larghezza di banda terribili. `iperf3` isolerà questo fattore e ce lo mostrerà in numeri puri (Gbits/sec). Mi aspetto che la rete delle VM sia 6-10 volte peggiore.
