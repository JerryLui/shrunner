#!/bin/bash -l
#SBATCH --time=15:00
#SBATCH -mem=4096
#SBATCH -A VGTT

PATH_SCRIPT = $1
PATH_FILE = $2

exec ${PATH_SCRIPT} ${PATH_FILE} &

