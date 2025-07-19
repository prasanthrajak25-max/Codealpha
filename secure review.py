import subprocess

def run_bandit_scan(target_file):
    print(f"🔍 Scanning {target_file} for security issues with Bandit...\n")
    result = subprocess.run(['bandit', '-r', target_file], capture_output=True, text=True)
    print(result.stdout)

# Example usage:
if __name__ == "__main__":
    run_bandit_scan("insecure_script.py")
