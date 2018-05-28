import sys

import lora_send
import lora_recv
import lora_setting


def main():
    lora_device_name = "/dev/ttyS0"  # ES920LRデバイス名
    lora_device = lora_setting.LoraSettingClass(lora_device_name)  # デバイス名&ボーレート設定
    args = sys.argv
    if len(args) < 2:
        print('Usage: python %s [send | recv]' % (args[0]))
        print('       [send | recv] ... mode select')
        sys.exit()
    if args[1] != "send" and args[1] != "recv":
        print('Usage: python %s [send | recv] [on | off]' % (args[0]))
        print('       [send | recv] ... mode select')
        sys.exit()

    if args[1] == "send":
        lr_send = lora_send.LoraSendClass(lora_device)
        lr_send.lora_send()

    elif args[1] == "recv":
        lr_recv = lora_recv.LoraRecvClass(lora_device)
        lr_recv.lora_recv()


if __name__ == '__main__':
    main()
