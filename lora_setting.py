# -*- coding: utf-8 -*-
import serial


# LoRa設定用クラス
class LoraSettingClass:
    def __init__(self, serial_device=''):
        try:  # インスタンス変数 serialDevice を生成
            self.device = serial.Serial(serial_device, 115200)
        except Exception as e:
            error_mes = '{0}'.format(e)
            print(error_mes)
        self.cmd = None

    # LoRaに対して命令コマンドを入力する
    def cmd_lora(self, cmd=''):
        if not cmd:  # cmdが未入力の場合は終了
            print('cmdが入力されていません')
            return
        self.cmd = '{0}\r\n'.format(cmd)
        self.device.write(self.cmd.encode())
