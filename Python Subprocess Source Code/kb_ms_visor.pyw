from cuesdk import CueSdk
import time

print('[NAME]: kb_ms_[cpu_spike_visor]_1 [MESSAGE]: started')


def custom_funk_0(target_idx_0, target_idx_1):

    # initialize kb
    kb_off_item = []
    kb_on_item = []
    kb_off_dict_0 = {2: (0, 0, 0)}
    kb_off_dict_1 = {3: (0, 0, 0)}
    kb_off_dict_2 = {4: (0, 0, 0)}
    kb_off_dict_3 = {5: (0, 0, 0)}
    kb_off_dict_4 = {6: (0, 0, 0)}
    kb_off_dict_5 = {7: (0, 0, 0)}
    kb_off_dict_6 = {8: (0, 0, 0)}
    kb_off_dict_7 = {9: (0, 0, 0)}
    kb_off_dict_8 = {10: (0, 0, 0)}
    kb_off_dict_9 = {11: (0, 0, 0)}
    kb_off_dict_10 = {12: (0, 0, 0)}
    kb_off_dict_11 = {73: (0, 0, 0)}
    kb_on_dict_0 = {2: (0, 255, 255)}
    kb_on_dict_1 = {3: (0, 255, 255)}
    kb_on_dict_2 = {4: (0, 255, 255)}
    kb_on_dict_3 = {5: (0, 255, 255)}
    kb_on_dict_4 = {6: (0, 255, 255)}
    kb_on_dict_5 = {7: (0, 255, 255)}
    kb_on_dict_6 = {8: (0, 255, 255)}
    kb_on_dict_7 = {9: (0, 255, 255)}
    kb_on_dict_8 = {10: (0, 255, 255)}
    kb_on_dict_9 = {11: (0, 255, 255)}
    kb_on_dict_10 = {12: (0, 255, 255)}
    kb_on_dict_11 = {73: (0, 255, 255)}
    kb_off_item.append(kb_off_dict_0)
    kb_off_item.append(kb_off_dict_1)
    kb_off_item.append(kb_off_dict_2)
    kb_off_item.append(kb_off_dict_3)
    kb_off_item.append(kb_off_dict_4)
    kb_off_item.append(kb_off_dict_5)
    kb_off_item.append(kb_off_dict_6)
    kb_off_item.append(kb_off_dict_7)
    kb_off_item.append(kb_off_dict_8)
    kb_off_item.append(kb_off_dict_9)
    kb_off_item.append(kb_off_dict_10)
    kb_off_item.append(kb_off_dict_11)
    kb_on_item.append(kb_on_dict_0)
    kb_on_item.append(kb_on_dict_1)
    kb_on_item.append(kb_on_dict_2)
    kb_on_item.append(kb_on_dict_3)
    kb_on_item.append(kb_on_dict_4)
    kb_on_item.append(kb_on_dict_5)
    kb_on_item.append(kb_on_dict_6)
    kb_on_item.append(kb_on_dict_7)
    kb_on_item.append(kb_on_dict_8)
    kb_on_item.append(kb_on_dict_9)
    kb_on_item.append(kb_on_dict_10)
    kb_on_item.append(kb_on_dict_11)

    # initialize mouse
    ms_off_item = []
    ms_on_item = []
    ms_off_dict_0 = {148: (0, 0, 0)}
    ms_off_dict_1 = {149: (0, 0, 0)}
    ms_off_dict_2 = {150: (0, 0, 0)}
    ms_off_dict_3 = {151: (0, 0, 0)}
    ms_on_dict_0 = {148: (0, 255, 255)}
    ms_on_dict_1 = {149: (0, 255, 255)}
    ms_on_dict_2 = {150: (0, 255, 255)}
    ms_on_dict_3 = {151: (0, 255, 255)}
    ms_off_item.append(ms_off_dict_0)
    ms_off_item.append(ms_off_dict_1)
    ms_off_item.append(ms_off_dict_2)
    ms_off_item.append(ms_off_dict_3)
    ms_on_item.append(ms_on_dict_0)
    ms_on_item.append(ms_on_dict_1)
    ms_on_item.append(ms_on_dict_2)
    ms_on_item.append(ms_on_dict_3)

    # kb visor right
    i = 0
    for kb_on_items in kb_on_item:
        sdk.set_led_colors_buffer_by_device_index(target_idx_0, kb_on_item[i])
        sdk.set_led_colors_flush_buffer()
        if i != 0:
            off_var_int = (i - 1)
            sdk.set_led_colors_buffer_by_device_index(target_idx_0, kb_off_item[off_var_int])
        i += 1
        time.sleep(0.02)
    sdk.set_led_colors_buffer_by_device_index(target_idx_0, kb_off_item[-1])

    # mouse visor
    sdk.set_led_colors_buffer_by_device_index(target_idx_1, ms_off_item[3])
    sdk.set_led_colors_flush_buffer()
    time.sleep(0.08)
    sdk.set_led_colors_buffer_by_device_index(target_idx_1, ms_off_item[0])
    sdk.set_led_colors_flush_buffer()
    sdk.set_led_colors_buffer_by_device_index(target_idx_1, ms_off_item[1])
    sdk.set_led_colors_flush_buffer()
    sdk.set_led_colors_buffer_by_device_index(target_idx_1, ms_off_item[2])
    sdk.set_led_colors_flush_buffer()
    time.sleep(0.08)
    sdk.set_led_colors_buffer_by_device_index(target_idx_1, ms_on_item[0])
    sdk.set_led_colors_flush_buffer()
    sdk.set_led_colors_buffer_by_device_index(target_idx_1, ms_on_item[1])
    sdk.set_led_colors_flush_buffer()
    sdk.set_led_colors_buffer_by_device_index(target_idx_1, ms_on_item[2])
    sdk.set_led_colors_flush_buffer()
    time.sleep(0.08)
    sdk.set_led_colors_buffer_by_device_index(target_idx_1, ms_on_item[3])
    sdk.set_led_colors_flush_buffer()

    # kb visor left
    i = len(kb_on_item)-1
    for kb_on_items in kb_on_item:
        sdk.set_led_colors_buffer_by_device_index(target_idx_0, kb_on_item[i])
        sdk.set_led_colors_flush_buffer()
        if i is not len(kb_on_item)-1:
            off_var_int = (i + 1)
            sdk.set_led_colors_buffer_by_device_index(target_idx_0, kb_off_item[off_var_int])
        i -= 1
        time.sleep(0.02)


def main():
    global sdk
    sdk = CueSdk()
    connected = sdk.connect()
    if not connected:
        err = sdk.get_last_error()
        print('[NAME]: kb_ms_[cpu_spike_visor]_1 [FUNCTION]: main [MESSAGE]: Handshake failed: %s' % err)
    elif connected:
        device = sdk.get_devices()
        gate_0 = False
        gate_1 = False
        i = 0
        for devices in device:
            target_name = str(device[i])
            if 'K95 RGB PLATINUM' in target_name:
                target_idx_0 = i
                gate_0 = True
            if 'SCIMITAR RGB ELITE' in target_name:
                target_idx_1 = i
                gate_1 = True
            i += 1
        if gate_0 is True and gate_1 is True:
            i = 0
            while i < 2:
                custom_funk_0(target_idx_0, target_idx_1)
                i += 1
        else:
            print('[NAME]: kb_ms_[cpu_spike_visor]_1 [FUNCTION]: main [MESSAGE]: Device(s) Not Found')
            time.sleep(1)


if __name__ == "__main__":
    main()
