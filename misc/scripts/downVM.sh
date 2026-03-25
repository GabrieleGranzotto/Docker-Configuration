#!/bin/bash
echo "Spegnimento del cluster di VM..."

VBoxManage controlvm "Ubuntu_VM_Master" acpipowerbutton
VBoxManage controlvm "Ubuntu_VM1" acpipowerbutton
VBoxManage controlvm "Ubuntu_VM2" acpipowerbutton

echo "Comando di spegnimento inviato a tutte le VM."
