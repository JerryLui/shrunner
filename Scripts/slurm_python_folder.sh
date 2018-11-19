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

echo "python ${PATH_SCRIPT} ${PATH_FOLDER}"
python ${PATH_SCRIPT} ${PATH_FOLDER}

module purge