import subprocess

def install_jenkins_module():
    try:
        # Use pip to install jenkins package
        subprocess.check_call(['pip', 'install', 'jenkins'])
        print("jenkins module installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install jenkins module. Error: {e}")

if __name__ == "__main__":
    install_jenkins_module()
