# -*- coding: utf-8 -*-
import time
import sys


class LoraRecvClass:
    def __init__(self, serial_device):
        self.sendDevice = serial_device
        self.sendDevice.cmd_lora('1')
        time.sleep(0.1)
        self.sendDevice.cmd_lora('a')
        time.sleep(0.1)
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

    def lora_recv(self):
        while True:
            if self.sendDevice.device.inWaiting() > 0:
                line = self.sendDevice.device.readline()
                line = line.decode("utf-8")
                print(line)
                if line.find("Ack Timeout") >= 0:
                    continue
                if line.find('exit') >= 0:
                    sys.exit()
