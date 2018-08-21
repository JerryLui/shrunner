#!/usr/bin/env bash
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#SBATCH --time=15:00
#SBATCH -A VGTT
#SBATCH --mail-user=jerry.x.liu@aptiv.com
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Author: Jerry Liu		(jerry.x.liu@aptiv.com)
# General Script Runner
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

PATH_SCRIPT=$1
PATH_FOLDER=(${LISTOFFOLDERS})
PATH_FOLDER=${PATH_FOLDER[$SLURM_ARRAY_TASK_ID]}

module load mcr/8.1

echo "exec ${PATH_SCRIPT} ${PATH_FOLDER}"
exec ${PATH_SCRIPT} ${PATH_FOLDER}

module purge
