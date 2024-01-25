# SETUP

export ML_PATH="$HOME/Documents/Aprendendo_Python/ML"
python3 -m pip install -U virtualenv # install virtualenv
python3 -m virtualenv my_env # create virtualenv
cd $ML_PATH

# RUN

source my_env/bin/activate # activate virtualenv
deactivate # deactivate virtualenv

# INSTALL

pip install -r requirements.txt # install requirements

python3 -m ipykernel install --user --name=python3 # install kernel for jupyter notebook

# RUN

jupyter notebook # run jupyter notebook
control + C # stop jupyter notebook

http://localhost:8888/  # open in browser