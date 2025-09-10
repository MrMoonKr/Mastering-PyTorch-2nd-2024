import subprocess

def run_nvidia_smi():
    try:
        result = subprocess.run(['nvidia-smi'], capture_output=True, text=True, check=True)
        print(result.stdout)
    except FileNotFoundError:
        print("nvidia-smi 명령을 찾을 수 없습니다. NVIDIA 드라이버가 설치되어 있는지 확인하세요.")
    except subprocess.CalledProcessError as e:
        print("nvidia-smi 실행 중 오류 발생:")
        print(e.stderr)

if __name__ == "__main__":
    run_nvidia_smi()