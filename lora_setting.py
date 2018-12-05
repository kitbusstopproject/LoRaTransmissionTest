# -*- coding: utf-8 -*-
import serial
import time
import RPi.GPIO as GPIO


# LoRa設定用クラス
class LoraSettingClass:

    def __init__(self, serial_device=''):
        try:  # インスタンス変数 serialDevice を生成
            self.device = serial.Serial(serial_device, 115200)
        except Exception as e:
            error_mes = '{0}'.format(e)
            print(error_mes)
        self.cmd = None
        self.reset_pin = 11

    # LoRaに対して命令コマンドを入力する
    def cmd_lora(self, cmd=''):
        if not cmd:  # cmdが未入力の場合は終了
            print('cmdが入力されていません')
            return
        self.cmd = '{0}\r\n'.format(cmd)
        self.device.write(self.cmd.encode())

    # LoRaリセット
    def reset_lora(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.reset_pin, GPIO.OUT)
        GPIO.output(self.reset_pin, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(self.reset_pin, GPIO.LOW)
        time.sleep(0.1)
        GPIO.cleanup()
        time.sleep(1)

    def close(self):
        self.device.close()
