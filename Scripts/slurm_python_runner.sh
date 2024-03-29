#!/usr/bin/env bash
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#SBATCH --time=60:00
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
27)
    module load python/2.7.11
    ;;
35)
    module load python/3.5.2
    ;;
*)
    module load python
    ;;
esac

echo "python ${PATH_SCRIPT} ${PATH_FILE}"
python ${PATH_SCRIPT} ${PATH_FILE}

module purge