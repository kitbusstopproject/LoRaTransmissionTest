# -*- coding: utf-8 -*-
import time


class LoraRecvClass:
    """
        LoRa受信用クラス
    """

    def __init__(self, serial_device, channel):
        self.sendDevice = serial_device
        self.channel = channel
        self.sendDevice.cmd_lora('1')
        time.sleep(0.1)
        self.sendDevice.cmd_lora('a')
        time.sleep(0.1)
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

    """ES920LRデータ受信メソッド"""
    def lora_recv(self):
        while True:
            if self.sendDevice.device.inWaiting() > 0:
                try:
                    line = self.sendDevice.device.readline()
                    line = line.decode("utf-8")
                except Exception as e:
                    print(e)
                    continue
                print(line)
                if line.find('RSSI') >= 0 and line.find('information') == -1:
                    log = line
                    log_list = log.split('):Receive Data(')
                    rssi = log_list[0][5:]
                    data = log_list[1].replace(")", "").strip()
                    num = log_list[1][0:3]
                    print(num + ',' + rssi + ',' + data)
                    with open('recv_log.csv', 'a') as f:
                        f.write(num + ',' + rssi + ',' + data + '\n')
