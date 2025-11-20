# Docker Configuration for Distributed Computing Cluster

This repository contains Docker configuration files for setting up a distributed computing environment with one master node and multiple worker nodes. The setup is designed for running HPC (High Performance Computing) benchmarks and distributed computing tasks.

## Architecture

The cluster consists of:
- **1 Master Node**: Generates SSH keys and coordinates the cluster
- **2 Worker Nodes** (node01, node02): Accept SSH connections from master for distributed tasks

All nodes are connected via a custom Docker network (`testnet`) and share data through a common volume.

## Prerequisites

- Docker
- Docker Compose

## Quick Start

1. Clone this repository:
```bash
git clone https://github.com/GabrieleGranzotto/Docker-Configuration.git
cd Docker-Configuration
```

2. Build and start the cluster:
```bash
docker-compose up -d
```

3. Verify all containers are running:
```bash
docker-compose ps
```

4. Access the master node:
```bash
docker exec -it master /bin/bash
```

## Features

### Installed Tools

All nodes include:
- **Editors**: nano, vim
- **Build tools**: gcc, g++, make
- **Benchmark tools**:
  - HPCC (High Performance Computing Challenge)
  - MPICH (MPI implementation)
  - stress-ng (stress testing)
  - sysbench (system benchmarking)
  - iozone3 (filesystem benchmarking)
  - iperf3 (network benchmarking)
- **Network tools**: netcat, curl, wget

### SSH Configuration

- Master node generates an SSH key pair at startup
- Public key is shared via the `/data` volume
- Worker nodes automatically configure SSH authentication
- Password-less SSH access from master to all worker nodes

## Directory Structure

```
.
├── docker-compose.yml          # Main orchestration file
├── master/
│   └── Dockerfile             # Master node configuration
├── nodes/
│   └── Dockerfile             # Worker nodes configuration
├── misc/
│   ├── data/
│   │   └── hpccinf.txt       # HPCC benchmark configuration
│   └── scripts/
│       ├── setup.sh          # Node SSH setup script
│       └── docker_iozone_script.sh  # IOzone benchmark script
└── shared_data/               # Shared volume between containers
```

## Resource Allocation

Each container is configured with:
- **CPU**: 2 cores
- **Memory**: 2GB RAM

You can adjust these limits in `docker-compose.yml` if needed.

## Usage Examples

### Running HPCC Benchmark

From the master node:
```bash
# The hpccinf.txt configuration file is already in place
cd /root
mpirun -np 6 hpcc
```

### Running IOzone Benchmark

From the master node:
```bash
cd /root
bash iozone_script.sh
```

### Testing Network Performance

From the master node, test network speed to a worker node:
```bash
# On node01 (in another terminal)
docker exec -it node01 iperf3 -s

# On master
docker exec -it master iperf3 -c node01
```

### SSH into Worker Nodes

From the master node:
```bash
ssh root@node01
ssh root@node02
```

## Stopping the Cluster

```bash
docker-compose down
```

To remove all data:
```bash
docker-compose down -v
```

## Network Configuration

The cluster uses a custom bridge network (`testnet`) that allows:
- Container-to-container communication using hostnames
- Isolated network environment
- DNS resolution for container names

## Troubleshooting

### Containers not starting

Check container logs:
```bash
docker-compose logs master
docker-compose logs node01
docker-compose logs node02
```

### SSH connection issues

Verify the SSH key was generated:
```bash
docker exec -it master cat /data/id_rsa.pub
```

### Permission issues

The shared volume uses the root user inside containers. Ensure your Docker daemon has proper permissions.

## Contributing

Feel free to open issues or submit pull requests for improvements.

## License

This project is available for educational and research purposes.
