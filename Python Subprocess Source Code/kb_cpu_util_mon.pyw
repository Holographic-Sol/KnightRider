import os
from cuesdk import CueSdk
import time
import win32api
import psutil

print('[NAME]: kb_cpu_util_mon [MESSAGE]: started')

color = [255, 0, 0]
led_time_on = 0.05
c = ()

initiation = False
keep_going_bool = True
kb_bool = [False, False, False,
           False, False, False,
           False, False, False,
           False]

item = [({116: (color[0], color[1], color[2])}),
        ({117: (color[0], color[1], color[2])}),
        ({118: (color[0], color[1], color[2])}),
        ({113: (color[0], color[1], color[2])}),
        ({114: (color[0], color[1], color[2])}),
        ({115: (color[0], color[1], color[2])}),
        ({109: (color[0], color[1], color[2])}),
        ({110: (color[0], color[1], color[2])}),
        ({111: (color[0], color[1], color[2])})]

item_off = [({116: (0, 0, 0)}),
            ({117: (0, 0, 0)}),
            ({118: (0, 0, 0)}),
            ({113: (0, 0, 0)}),
            ({114: (0, 0, 0)}),
            ({115: (0, 0, 0)}),
            ({109: (0, 0, 0)}),
            ({110: (0, 0, 0)}),
            ({111: (0, 0, 0)})]


def initialize():
    global color, led_time_on, item
    try:
        with open('.\\config.dat', 'r') as fo:
            for line in fo:
                line = line.strip()
                if line.startswith('cpu_threshold_led_color: '):
                    color = line.replace('cpu_threshold_led_color: ', '')
                    color = color.split(',')
                    color[0] = int(color[0])
                    color[1] = int(color[1])
                    color[2] = int(color[2])
                if line.startswith('cpu_threshold_led_time_on: '):
                    line = line.replace('cpu_threshold_led_time_on: ', '')
                    try:
                        led_time_on = float(line)
                    except Exception as e:
                        print('[NAME]: kb_cpu_util_mon [FUNCTION]: initialize [EXCEPTION]:', e)
        item = [({116: (color[0], color[1], color[2])}),
                ({117: (color[0], color[1], color[2])}),
                ({118: (color[0], color[1], color[2])}),
                ({113: (color[0], color[1], color[2])}),
                ({114: (color[0], color[1], color[2])}),
                ({115: (color[0], color[1], color[2])}),
                ({109: (color[0], color[1], color[2])}),
                ({110: (color[0], color[1], color[2])}),
                ({111: (color[0], color[1], color[2])})]
    except Exception as e:
        print('[NAME]: kb_cpu_util_mon [FUNCTION]: initialize [EXCEPTION]:', e)


def get_cpu():
    global c, kb_bool
    c = psutil.cpu_percent(0.1)
    if c < 10:
        kb_bool[0] = True
        kb_bool[1] = False
        kb_bool[2] = False
        kb_bool[3] = False
        kb_bool[4] = False
        kb_bool[5] = False
        kb_bool[6] = False
        kb_bool[7] = False
        kb_bool[8] = False
        kb_bool[9] = False

    elif c >= 10 and c < 20:
        kb_bool[0] = True
        kb_bool[1] = True
        kb_bool[2] = False
        kb_bool[3] = False
        kb_bool[4] = False
        kb_bool[5] = False
        kb_bool[6] = False
        kb_bool[7] = False
        kb_bool[8] = False
        kb_bool[9] = False
        kb_bool[9] = False

    elif c >= 20 and c < 30:
        kb_bool[0] = True
        kb_bool[1] = True
        kb_bool[2] = True
        kb_bool[3] = False
        kb_bool[4] = False
        kb_bool[5] = False
        kb_bool[6] = False
        kb_bool[7] = False
        kb_bool[8] = False
        kb_bool[9] = False
        kb_bool[9] = False

    elif c >= 30 and c < 40:
        kb_bool[0] = True
        kb_bool[1] = True
        kb_bool[2] = True
        kb_bool[3] = True
        kb_bool[4] = False
        kb_bool[5] = False
        kb_bool[6] = False
        kb_bool[7] = False
        kb_bool[8] = False
        kb_bool[9] = False

    elif c >= 40 and c < 50:
        kb_bool[0] = True
        kb_bool[1] = True
        kb_bool[2] = True
        kb_bool[3] = True
        kb_bool[4] = True
        kb_bool[5] = False
        kb_bool[6] = False
        kb_bool[7] = False
        kb_bool[8] = False
        kb_bool[9] = False
        kb_bool[9] = False

    elif c >= 50 and c < 60:
        kb_bool[0] = True
        kb_bool[1] = True
        kb_bool[2] = True
        kb_bool[3] = True
        kb_bool[4] = True
        kb_bool[5] = True
        kb_bool[6] = False
        kb_bool[7] = False
        kb_bool[8] = False
        kb_bool[9] = False
        kb_bool[9] = False

    elif c >= 60 and c < 70:
        kb_bool[0] = True
        kb_bool[1] = True
        kb_bool[2] = True
        kb_bool[3] = True
        kb_bool[4] = True
        kb_bool[5] = True
        kb_bool[6] = True
        kb_bool[7] = False
        kb_bool[8] = False
        kb_bool[9] = False

    elif c >= 70 and c < 80:
        kb_bool[0] = True
        kb_bool[1] = True
        kb_bool[2] = True
        kb_bool[3] = True
        kb_bool[4] = True
        kb_bool[5] = True
        kb_bool[6] = True
        kb_bool[7] = True
        kb_bool[8] = False
        kb_bool[9] = False

    elif c >= 80 and c < 90:
        kb_bool[0] = True
        kb_bool[1] = True
        kb_bool[2] = True
        kb_bool[3] = True
        kb_bool[4] = True
        kb_bool[5] = True
        kb_bool[6] = True
        kb_bool[7] = True
        kb_bool[8] = True
        kb_bool[9] = False

    elif c >= 90:
        kb_bool[0] = True
        kb_bool[1] = True
        kb_bool[2] = True
        kb_bool[3] = True
        kb_bool[4] = True
        kb_bool[5] = True
        kb_bool[6] = True
        kb_bool[7] = True
        kb_bool[8] = True
        kb_bool[9] = True


def custom_funk_0(target_idx_0):
    global keep_going_bool, initiation, kb_bool, color

    initialize()
    get_cpu()

    if initiation is False:
        for _ in item_off:
            kb_on_dict_0 = _
            try:
                sdk.set_led_colors_buffer_by_device_index(target_idx_0, kb_on_dict_0)
            except Exception as e:
                print('[NAME]: kb_cpu_util_mon [FUNCTION]: custom_funk_0 [EXCEPTION]:', e)
        initiation = True

    i = 0
    for _ in item:
        if kb_bool[i] is True:
            kb_on_dict_0 = item[i]
            sdk.set_led_colors_buffer_by_device_index(target_idx_0, kb_on_dict_0)

        elif kb_bool[i] is False:
            kb_on_dict_0 = item_off[i]
            sdk.set_led_colors_buffer_by_device_index(target_idx_0, kb_on_dict_0)

        i += 1

    sdk.set_led_colors_flush_buffer()
    time.sleep(led_time_on)


def main():
    global sdk, keep_going_bool

    while keep_going_bool is True:
        sdk = CueSdk(os.path.join(os.getcwd(), 'bin\\CUESDK.x64_2017.dll'))
        connected = sdk.connect()
        try:
            with open('kb_cpu_util_mon.sys', 'r') as fo:
                try:
                    for line in fo:
                        line = line.strip()
                        if line.startswith('running: '):
                            if line == 'running: True':
                                keep_going_bool = True
                            else:
                                keep_going_bool = False
                except Exception as e:
                    print('[NAME]: kb_cpu_util_mon [FUNCTION]: main [EXCEPTION]:', e)
        except Exception as e:
            print('[NAME]: kb_cpu_util_mon [FUNCTION]: main [EXCEPTION]:', e)

        if not connected:
            err = sdk.get_last_error()
            print('[NAME]: kb_cpu_util_mon [FUNCTION]: main [MESSAGE]: Handshake failed: %s' % err)
            time.sleep(1)

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
                print('[NAME]: kb_cpu_util_mon [FUNCTION]: main [MESSAGE]: Device Not Found')
                time.sleep(1)


if __name__ == "__main__":
    main()
