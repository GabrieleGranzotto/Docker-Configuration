#!/bin/bash
echo "Avvio del cluster di VM..."

VBoxManage startvm "Ubuntu_VM_Master" --type headless
VBoxManage startvm "Ubuntu_VM1" --type headless
VBoxManage startvm "Ubuntu_VM2" --type headless

echo "Comando di avvio inviato a tutte le VM."
