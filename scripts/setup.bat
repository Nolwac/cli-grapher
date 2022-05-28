@echo off
python -m pip install virtualenvwrapper==4.8.4 && mkvirtualenv cli-grapher && workon cli-grapher && python scripts/copy_env_scripts.py && python scripts/dev_environment_setup.py