#!/usr/bin/env bash
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#SBATCH --time=30:00
#SBATCH -A VGTT
#SBATCH --mail-user=jerry.x.liu@aptiv.com
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Author: Jerry Liu		(jerry.x.liu@aptiv.com)
# General Script Runner
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

PATH_SCRIPT=$1
DIRNAME=$2
PATH_FILE=(${LISTOFLOGS})
PATH_FILE=${PATH_FILE[$SLURM_ARRAY_TASK_ID]}
PATH_FILE="$DIRNAME/$PATH_FILE"

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

echo "exec ${PATH_SCRIPT} ${PATH_FILE}"
exec ${PATH_SCRIPT} ${PATH_FILE}

module purge
