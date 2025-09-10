import subprocess

def get_nvidia_smi_version():
    try:
        result = subprocess.run(
            ["nvidia-smi", "--version"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        print(result.stdout.strip())
    except FileNotFoundError:
        print("nvidia-smi not found. Make sure NVIDIA drivers are installed.")
    except subprocess.CalledProcessError as e:
        print(f"Error running nvidia-smi: {e.stderr.strip()}")

if __name__ == "__main__":
    get_nvidia_smi_version()