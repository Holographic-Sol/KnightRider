import os
from cuesdk import CueSdk
import time
import win32api

print('[NAME]: kb_alpha_ [MESSAGE]: started')

color = '255, 0, 0'
led_time_on = 0.05

with open('.\\config.dat', 'r') as fo:
    for line in fo:
        line = line.strip()
        if line.startswith('hdd_led_color: '):
            color = line.replace('hdd_led_color: ', '')
        if line.startswith('hdd_led_time_on: '):
            line = line.replace('hdd_led_time_on: ', '')
            try:
                led_time_on = float(line)
            except Exception as e:
                print('[NAME]: kb_alpha_ [FUNCTION]: main [EXCEPTION]:', e)

color = color.split(',')
color[0] = int(color[0])
color[1] = int(color[1])
color[2] = int(color[2])


def custom_funk_0(target_idx_0):
    kb_on_dict_0 = {53: (color[0], color[1], color[2])}
    sdk.set_led_colors_buffer_by_device_index(target_idx_0, kb_on_dict_0)
    sdk.set_led_colors_flush_buffer()
    time.sleep(led_time_on)


def main():
    global sdk
    sdk = CueSdk(os.path.join(os.getcwd(), 'bin\\CUESDK.x64_2017.dll'))
    connected = sdk.connect()
    if not connected:
        err = sdk.get_last_error()
        print('[NAME]: kb_alpha_ [FUNCTION]: main [MESSAGE]: Handshake failed: %s' % err)
        return
    elif connected:
        device = sdk.get_devices()
        gate_0 = False
        i = 0
        for devices in device:
            target_name = str(device[i])
            if 'K95 RGB PLATINUM' in target_name:
                target_idx_0 = i
                gate_0 = True
            i += 1
        if gate_0 is True:
            i = 0
            while i < 1:
                custom_funk_0(target_idx_0)
                i += 1
        else:
            print('[NAME]: kb_alpha_ [FUNCTION]: main [MESSAGE]: Device Not Found')


if __name__ == "__main__":
    main()
