import socket
import subprocess


def get_random_port():
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.bind(('', 0))
    add, port = tcp.getsockname()
    tcp.close()
    return port


def run_command(command):
    return subprocess.Popen([command], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


def is_android_device_connected():
    output = subprocess.check_output(["adb", "devices"]).decode('utf-8').split('\n')
    return 'List of devices attached' in output[0] and 'device' in output[1]
