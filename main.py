import sys

import lora_send
import lora_recv
import lora_setting


def main():
    serial_lora_device = "/dev/ttyS0"
    send_device = lora_setting.LoraSettingClass(serial_lora_device)
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
        lr_send = lora_send.LoraSendClass(send_device)
        lr_send.lora_send()

    elif args[1] == "recv":
        lr_recv = lora_recv.LoraRecvClass(send_device)
        lr_recv.lora_recv()


if __name__ == '__main__':
    main()
