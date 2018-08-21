## shrunner
The best job scheduler for matlab scripting on HPCC.
To compile MATLAB scripts use [Grand Compile Auto](http://10.239.124.134:5000/).

### Basic Tutorial for .mat file generation:

1. Clone this repository to your HPCC folder with ``` git clone https://hpc-gitlab.europe.delphiauto.net/mjbf5f/shrunner.git ```

1. Ensure that python module is loaded by checking .bashrc using `cat ~/.bashrc`,
the output should include ``` module load python ```.
    If not, add it with the following command `echo module load python >> ~/.bashrc` and reload your
.bashrc either by reconnecting or `source ~/.bashrc`

1. Run the script on your log folder to generate .mat files by navigating to the folder containing
the shrunner folder and executing:

    ``` $: python shrunner /absolute/folder/path/to/your/log/files/with/dvl ```
    
__P.S.__ this works with file lists ending with .list

### For more usage:
Try
    
    $: python shrunner -h
    
Shrunner can read file/folder lists and run recursivley. It can also run with any arbitrary matlab or python script.
