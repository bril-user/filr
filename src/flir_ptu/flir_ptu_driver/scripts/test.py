import serial
import time
ser = serial.Serial()
# 设置串口参数
ser.port = "/dev/ttyUSB0" # 串口，例如 'COM1'、'COM3' 等，这需要你根据实际情况进行替换
ser.baudrate = 9600  # 波特率
ser.bytesize = serial.EIGHTBITS  # 数据位
ser.parity = serial.PARITY_NONE  # 校验位
ser.stopbits = serial.STOPBITS_ONE  # 停止位
ser.xonxoff = False  # 关闭软件流控
ser.rtscts = False  # 关闭硬件流控
# 重新打开串口
ser.open()

# 检查串口是否成功打开
if ser.isOpen():
    print("串口已打开")
else:
    print("串口打开失败")
# Send an ASCII string
ser.write(b"PP100\n")

time.sleep(1)  # 等待一秒，确保命令已经发送

# 读取返回数据
while ser.in_waiting:
    response = ser.read(ser.in_waiting)
    print("Response:", response)

# 关闭串口
ser.close()
