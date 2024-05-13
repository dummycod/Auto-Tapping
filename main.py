from ppadb.client import Client as AdbClient
import time

def connect():
    client = AdbClient(host="127.0.0.1", port=5037) # Default is "127.0.0.1" and 5037

    devices = client.devices()

    if len(devices) == 0:
        print('No devices')
        quit()

    device = devices[0]

    print(f'Connected to {device}')

    return device, client

if __name__ == '__main__':
    device, client = connect()

    device.shell('monkey -p com.kiloo.subwaysurf 1')
    time.sleep(10)
    
    #Open Store.
    device.shell('input tap 450 1507')

    time.sleep(0.5)

    #Open Store Section.
    device.shell('input tap 367 1461')

    time.sleep(0.5)

    while True:
        device.shell('input tap 369 863')
        device.shell('input tap 369 863')
