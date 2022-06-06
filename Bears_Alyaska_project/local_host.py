import subprocess

cmd = 'docker port alaska'
returned_output = subprocess.check_output(cmd).decode("utf-8")

LOCAL_TCP = returned_output.split(':')[-1]  #берем адрес хоста
