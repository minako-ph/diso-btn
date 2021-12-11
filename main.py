# -*- coding: utf-8 -*-
import evdev
import subprocess
import time

def getProcess(idx):
    if idx == 0:
        cmd = [
            '/home/pi/s/rpi-rgb-led-matrix/examples-api-use/clock',
            '--led-no-hardware-pulse',
            '--led-slowdown-gpio=2',
            '--led-brightness=50',
            '--led-rows=16',
            '--led-cols=32',
            '-C',
            '255,0,255',
            '-d',
            '%H:%M',
            '-f',
            '/home/pi/s/rpi-rgb-led-matrix/fonts/clR6x12.bdf',
            '-y',
            '3',
            '-x',
            '1'
            ]
        return subprocess.Popen(cmd)
    if idx == 1:
        # cmd = [
        #     '/home/pi/s/rpi-rgb-led-matrix/examples-api-use/text-example',
        #     '--led-no-hardware-pulse',
        #     '--led-slowdown-gpio=2',
        #     '--led-brightness=50',
        #     '--led-rows=16',
        #     '--led-cols=32',
        #     '-C',
        #     '255,0,255',
        #     '-f',
        #     '/home/pi/s/rpi-rgb-led-matrix/fonts/clR6x12.bdf',
        # ]
        cmd = [
            '/home/pi/s/rpi-rgb-led-matrix/examples-api-use/scrolling-text-example',
            '--led-no-hardware-pulse',
            '--led-slowdown-gpio=2',
            '--led-brightness=50',
            '--led-rows=16',
            '--led-cols=32',
            '-C',
            '124,252,0',
            '-f',
            '/home/pi/s/rpi-rgb-led-matrix/fonts/clR6x12.bdf',
            '-s',
            '3',
            '-y',
            '3',
            'minako-ph'
        ]
        p = subprocess.Popen(cmd)
        # p.stdin.write(u'minako'.encode('utf-8'))
        # p.stdin.close()
        return p

if __name__ == '__main__':
    # 初回実行
    currentIndex = 0
    p = getProcess(currentIndex)

    while True:
        try:
            device = evdev.InputDevice('/dev/input/event1')
    
            for event in device.read_loop():
                if event.type == evdev.ecodes.EV_KEY:
                    if event.value == 1: # 0:KEYUP, 1:KEYDOWN, 2: LONGDOWN
                    
                        if event.code == evdev.ecodes.KEY_VOLUMEUP:
                            print(u'KEY_VOLUMEUP')

                            # 現在走ってるプロセスをkillする
                            p.kill()

                            # 参照するプロセスのIndexを更新
                            currentIndex = 0 if currentIndex == 1 else 1

                            # 新しいプロセスの取得
                            p = getProcess(currentIndex)

                        if event.code == evdev.ecodes.KEY_ENTER:
                            print(u'KEY_ENTER') # 現状拾えてない...
        except:
            print('Retry...')
            time.sleep(1)
