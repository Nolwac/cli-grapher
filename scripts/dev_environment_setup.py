import os


# install project requirements
def install_requirements():
    os.system("python -m pip install -r requirements.txt")  # install project requirements
    os.system("pre-commit install")  # install pre-commit prequirements for code formating


if __name__ == "__main__":
    install_requirements()
