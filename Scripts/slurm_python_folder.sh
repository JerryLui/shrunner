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

module load python

echo "python ${PATH_SCRIPT} ${PATH_FOLDER}"
python ${PATH_SCRIPT} ${PATH_FOLDER}

module purge