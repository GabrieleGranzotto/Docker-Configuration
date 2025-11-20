#!/bin/bash
# Setup script for node containers
# This script sets up SSH authentication between master and nodes

# Wait for the master's public key to be available
while [ ! -f /data/id_rsa.pub ]; do
    echo "Waiting for master's public key..."
    sleep 1
done

# Create .ssh directory if it doesn't exist
mkdir -p /root/.ssh

# Add the master's public key to authorized_keys
cat /data/id_rsa.pub >> /root/.ssh/authorized_keys
chmod 600 /root/.ssh/authorized_keys
chmod 700 /root/.ssh

echo "SSH setup complete. Master can now connect to this node."
