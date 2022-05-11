#We can execute below command one by one also by executing in the terminal or we can create one init_setup.sh file by using touch 
#filename.sh in the terminal and
#write everything here and it will automatically execute everything one by one 

conda create --prefix ./env python=3.7 -y
source activate ./env
pip install -r requirements.txt
conda env export > conda.yaml