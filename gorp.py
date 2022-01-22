import subprocess

def main():
    proc = subprocess.Popen("open -a 'Google Chrome' 'https://www.youtube.com/watch?v=gwxTZaa3NgI'", shell=True)
    proc.communicate()
    
if __name__ == "__main__":
    main()
