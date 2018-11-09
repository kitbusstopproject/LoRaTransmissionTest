# -*- coding: utf-8 -*-
import time
import sys
import lora_setting
import string
import random


class LoraSendClass:
    """
        LoRa送信用クラス
    """

    def __init__(self, lora_device, channel):
        self.sendDevice = lora_setting.LoraSettingClass(lora_device)
        self.channel = channel
        self.sendDevice.cmd_lora('1')
        time.sleep(0.1)
        self.sendDevice.cmd_lora('d')
        time.sleep(0.1)
        self.sendDevice.cmd_lora(self.channel)
        time.sleep(0.1)
        self.sendDevice.cmd_lora('g')
        time.sleep(0.1)
        self.sendDevice.cmd_lora('0001')
        time.sleep(0.1)
        self.sendDevice.cmd_lora('p')
        time.sleep(0.1)
        self.sendDevice.cmd_lora('1')
        time.sleep(0.1)
        self.sendDevice.cmd_lora('y')
        time.sleep(0.1)
        self.sendDevice.cmd_lora('z')

    """ES920LRデータ送信メソッド"""
    def lora_send(self):
        index1 = 1
        index2 = 1
        while self.sendDevice.device.inWaiting() == 0:
            time.sleep(1)
        while self.sendDevice.device.inWaiting() > 0:
            try:
                line = self.sendDevice.device.readline()
                line = line.decode("utf-8")
            except Exception as e:
                print(e)
                continue
            print(line)
        print('== 11byte Start ==')
        with open('send_11byte_log.csv', 'a') as f:
            f.write('[Start(11byte)]\n')
        while index1 <= 20:
            print('{0:04d}'.format(index1))
            num = '{0:04d}'.format(index1)
            data = ''.join([random.choice(string.ascii_lowercase) for i in range(7)])
            print('<-- SEND -- [00010001' + data + num + ']')
            self.sendDevice.cmd_lora('00010001' + data + num)
            with open('send_11byte_log.csv', 'a') as f:
                f.write(data + num + '\n')
            index1 += 1
            time.sleep(5)
        print('== 22byte Start ==')
        with open('send_22byte_log.csv', 'a') as f:
            f.write('[Start(22byte)]\n')
        while index2 <= 20:
            print('{0:04d}'.format(index2))
            num = '{0:04d}'.format(index2)
            data = ''.join([random.choice(string.ascii_lowercase) for i in range(18)])
            print('<-- SEND -- [00010001' + data + num + ']')
            self.sendDevice.cmd_lora('00010001' + data + num)
            with open('send_22byte_log.csv', 'a') as f:
                f.write(data + num + '\n')
            index2 += 1
            time.sleep(5)
        sys.exit()
