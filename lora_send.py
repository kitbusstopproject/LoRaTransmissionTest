# -*- coding: utf-8 -*-
import time
import lora_setting


# LoRa送信用クラス
class LoraSendClass:

    def __init__(self, lora_device, channel):
        self.sendDevice = lora_setting.LoraSettingClass(lora_device)
        self.channel = channel

    # ES920LRデータ送信メソッド
    def lora_send(self):
        # LoRa初期化
        self.sendDevice.reset_lora()
        # LoRa(ES9320LR)起動待機
        while self.sendDevice.device.inWaiting() > 0:
            try:
                line = self.sendDevice.device.readline()
                if line.find(b'Select'):
                    line = line.decode("utf-8")
                    print(line)
            except Exception as e:
                print(e)
                continue
        # LoRa(ES920LR)設定
        set_mode = ['1', 'd', self.channel, 'e', '0001', 'f', '0001', 'g', '0002',
                    'l', '2', 'n', '2', 'p', '1', 'y', 'z']
        # LoRa(ES920LR)設定コマンド入力
        for cmd in set_mode:
            self.sendDevice.cmd_lora(cmd)
            time.sleep(0.1)
        while self.sendDevice.device.inWaiting() > 0:
            try:
                line = self.sendDevice.device.readline()
                line = line.decode("utf-8")
                print(line)
            except Exception as e:
                print(e)
                continue
        # LoRa(ES920LR)データ送信
        while True:
            try:
                data = 'aaaa'
                print('<-- SEND -- [00010002 {} ]'.format(data))
                self.sendDevice.cmd_lora('00010002{}'.format(data))
            except KeyboardInterrupt:
                self.sendDevice.close()
            time.sleep(5)
