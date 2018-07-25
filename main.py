import sys

import lora_send
import lora_recv
import lora_setting


def main(argc, argv):
    lora_device_name = "/dev/ttyS0"  # ES920LRデバイス名
    lora_device = lora_setting.LoraSettingClass(lora_device_name)  # デバイス名&ボーレート設定
    if argc < 2:
        print('Usage: python %s [send | recv]' % (argv[0]))
        print('       [send | recv] ... mode select')
        sys.exit()
    if argv[1] != 'send' and argv[1] != 'recv':
        print('Usage: python %s [send | recv]' % (argv[0]))
        print('       [send | recv] ... mode select')
        sys.exit()

    channel = input('channel:')

    if argv[1] == 'send':
        lr_send = lora_send.LoraSendClass(lora_device, channel)
        lr_send.lora_send()
    elif argv[1] == 'recv':
        lr_recv = lora_recv.LoraRecvClass(lora_device, channel)
        lr_recv.lora_recv()


if __name__ == '__main__':
    main(len(sys.argv), sys.argv)
    sys.exit()

