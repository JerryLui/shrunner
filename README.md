## shrunner
The best job scheduler for .mat generation on HPCC.

### HPCC Guide:
Step 1. Ensure that python module is loaded by checking .bashrc using `cat ~/.bashrc`,
the output should include the following:
    
    ...
    module load python
    ...
    
If not, add it with the following command `echo module load python >> ~/.bashrc`.


Step 2. Run the script on your log folder to generate .mat files by navigating to the folder containing
the shrunner folder and executing:

    python shrunner /absolute/folder/path/to/your/log/files/with/dvl
    
P.S. this works with file lists ending with .list