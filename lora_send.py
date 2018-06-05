# -*- coding: utf-8 -*-
import time
import sys


class LoraSendClass:
    """
        LoRa送信用クラス
    """

    def __init__(self, serial_device, set_flag, config):
        self.sendDevice = serial_device
        self.set_flag = set_flag
        self.config = config
        self.sendDevice.cmd_lora('1')
        time.sleep(0.1)
        if self.set_flag == 'on':
            command = ['b', 'c', 'd', 'e', 'f', 'g']
            for cmd, conf in zip(command, self.config):
                self.sendDevice.cmd_lora(cmd)
                time.sleep(0.1)
                self.sendDevice.cmd_lora(conf)
                time.sleep(0.1)
        else:
            self.sendDevice.cmd_lora('d')
            time.sleep(0.1)
            self.sendDevice.cmd_lora('14')
            time.sleep(0.1)
            self.sendDevice.cmd_lora('g')
            time.sleep(0.1)
            self.sendDevice.cmd_lora('0001')
            time.sleep(0.1)
        self.sendDevice.cmd_lora('y')
        time.sleep(0.1)
        self.sendDevice.cmd_lora('z')

    """ES920LRデータ送信メソッド"""
    def lora_send(self):
        while True:
            panid = input('送信先PANID　；')
            addid = input('送信先アドレス；')
            data = input('送信データ　　：')
            print('<-- SEND -- [' + panid + addid + data + ']')
            self.sendDevice.cmd_lora(panid + addid + data)
            if data.find('exit') >= 0:
                sys.exit()
            while self.sendDevice.device.inWaiting() == 0:
                time.sleep(1)
            while self.sendDevice.device.inWaiting() > 0:
                line = self.sendDevice.device.readline()
                line = line.decode('utf-8')
                print(line)
                if line.find('Ack Timeout') >= 0:
                    self.sendDevice.cmd_lora(data)
                    time.sleep(2)
                elif line.find('send data failed') >= 0:
                    time.sleep(4)
                    self.sendDevice.cmd_lora(data)
                    time.sleep(2)
