#!/bin/bash
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#SBATCH --time=15:00
#SBATCH -A VGTT
#SBATCH --job-name=JERRYXL
#SBATCH --mail-user=jerry.x.liu@aptiv.com
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Author: Jerry Liu		(jerry.x.liu@aptiv.com)
# General Script Runner
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

PATH_SCRIPT=$1
PATH_FILE=(${LISTOFLOGS})
PATH_FILE=${PATH_FILE[$SLURM_ARRAY_TASK_ID]}

module load mcr/8.1

echo "exec ${PATH_SCRIPT} ${PATH_FILE}"
exec ${PATH_SCRIPT} ${PATH_FILE}

module purge
