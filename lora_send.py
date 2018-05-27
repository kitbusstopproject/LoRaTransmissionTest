# -*- coding: utf-8 -*-
import time
import sys


class LoraSendClass:
    def __init__(self, serial_device):
        self.sendDevice = serial_device
        self.sendDevice.cmd_lora('1')
        time.sleep(0.1)
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

    def lora_send(self):
        while True:
            data = input('送信データ：')
            print(data)
            self.sendDevice.cmd_lora(data)
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
                elif data == 'exit':
                    sys.exit()
                else:
                    pass
