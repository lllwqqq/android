# coding=utf-8
import os
import time
# 使用adb shell获得event 体系里 宽（0035）和高（0036）
# todo 我这里直接获取到的乱码，所以暂时手动获取，后面来解决乱码问题
# os.system('adb shell getevent -p | grep -e "0035"')

# 使用上面那条命令获取到event里面的宽和高,已知手机(LenovoK30-T)分辨率为1280*720
eventWidth = '720'
eventHigh = '1280'

# 计算比例

# rateW = eventWidth/720
# rateH = eventHigh/1280

# 打开支付宝
# os.system('adb shell am start com.eg.android.AlipayGphone/.AlipayLogin')
# time.sleep(3)

# 执行adb shell getevent | grep -e "0035" -e "0036" 命令后，记录下输出的最后一列值
# 点击扫一扫
#/dev/input/event0: 0003 0035 00000073
#/dev/input/event0: 0003 0036

# scan_width = 115
# scan_hight = 225
# os.system('adb shell input tap 115 225')
# time.sleep(1)

# 点击相册
#/dev/input/event0: 0003 0035 00000284
#/dev/input/event0: 0003 0036 0000006b
# photo_width = 644
# photo_hight = 107
# os.system('adb shell input tap 644 107')
# time.sleep(1)
# 选择二维码
# pic_1 = (),pic_2 = (),pic_3 = (),pic_4 = (),pic_5 = (),pic_6 = (),pic_7 = (),pic_8 = ()
# codes = ('644 107')
# for code in codes:
#     os.system('adb shell input tap %s' %code)
# 滑动
os.system('adb shell input swipe 606 992 606 675 100')





# os.system('adb shell am start com.eg.android.AlipayGphone/.AlipayLogin')
# os.system('adb shell logcat')
