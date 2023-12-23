import subprocess

def install_packages():
    packages = ['tensorflow', 'pandas', 'numpy', 'PyQt5', 'matplotlib']
    for package in packages:
        subprocess.call(['pip', 'install', package])

if __name__ == "__main__":
    install_packages()
