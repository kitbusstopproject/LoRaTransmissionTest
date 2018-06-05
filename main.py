import sys

import lora_send
import lora_recv
import lora_setting


def main(argc, argv):
    lora_device_name = "/dev/ttyS0"  # ES920LRデバイス名
    lora_device = lora_setting.LoraSettingClass(lora_device_name)  # デバイス名&ボーレート設定
    set_flag = None
    config = []
    if argc < 3:
        print('Usage: python %s [send | recv] [set | unset]' % (argv[0]))
        print('       [send | recv] ... mode select')
        print('       [set | unset] ... mode select')
        sys.exit()
    if argv[1] != 'send' and argv[1] != 'recv' and argv[2] != 'set' and argv[2] != 'unset':
        print('Usage: python %s [send | recv] [set | unset]' % (argv[0]))
        print('       [send | recv] ... mode select')
        print('       [set | unset] ... mode select')
        sys.exit()

    if argv[2] == 'set':
        set_flag = 'on'
        bw = input('bw     :')
        sf = input('sf     :')
        channel = input('channel:')
        panid = input('panID  :')
        ownid = input('ownID  :')
        dstid = input('dstID  :')
        config = [bw, sf, channel, panid, ownid, dstid]

    if argv[1] == 'send':
        lr_send = lora_send.LoraSendClass(lora_device, set_flag, config)
        lr_send.lora_send()
    elif argv[1] == 'recv':
        lr_recv = lora_recv.LoraRecvClass(lora_device, set_flag, config)
        lr_recv.lora_recv()


if __name__ == '__main__':
    main(len(sys.argv), sys.argv)
    sys.exit()

