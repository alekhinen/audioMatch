import subprocess

sp1 = ['oggdec', './assets/D1_Ogg/z07.ogg',  '-b', '16', '-o', './assets/z07.wav']
subprocess.call( sp1 )
