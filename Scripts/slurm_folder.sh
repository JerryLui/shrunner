#!/usr/bin/env bash
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#SBATCH --time=120:00
#SBATCH -A VGTT
#SBATCH --mail-user=jerry.x.liu@aptiv.com
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Author: Jerry Liu		(jerry.x.liu@aptiv.com)
# General Script Runner
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

PATH_SCRIPT=$1
PATH_FOLDER=(${LISTOFFOLDERS})
PATH_FOLDER=${PATH_FOLDER[$SLURM_ARRAY_TASK_ID]}

case $3 in
93)
    module load mcr/9.3
    ;;
92)
    module load mcr/9.2
    ;;
*)
    module load mcr/8.1
    ;;
esac

echo "exec ${PATH_SCRIPT} ${PATH_FOLDER}"
exec ${PATH_SCRIPT} ${PATH_FOLDER}

module purge
