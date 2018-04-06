#!/bin/bash -l
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#SBATCH --time=15:00
#SBATCH -A VGTT
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Author: Jerry Liu		(jerry.x.liu@aptiv.com)
# General Script Runner
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

PATH_SCRIPT=$1
PATH_FILE=$2
INDEX=$3

exec ${PATH_SCRIPT} ${PATH_FILE} &

