FLIR PTU 使用教程

**Windows:**
1. **Term Tera串口通信：**
   - 下载Term Tera。
   - 连接Host RS232到PC，并选择端口COM5(自适应)。
   - 打开PTU电源，它将开始自动校准。窗口中会显示“Initializing”。
   - 校准完成后，参照文档（E-SERIES-COMMAND-REFERENCE-MANUAL）进行命令输入以控制PTU。

2. **Web页面控制：**
   - 连接ETHERNET。
   - 在串口通信页面，输入“NMD + space”。然后输入“NI + space”查看IP地址。
   - 在浏览器中输入IP地址以访问web页面。打开PTU Configuration进行参数设置。具体内容请参照文档。

**Linux:**
1. 编译flir_ptu包。
2. 运行`source devel/setup.bash`。
3. 执行`roslaunch flir_ptu_driver ptu.launch`，在新的终端中运行`roslaunch flir_ptu_viz view_model.launch`。
4. 使用`rostopic pub /ptu/cmd sensor_msgs/JointState`发送命令，具体格式如下：
```
rostopic pub /ptu/cmd sensor_msgs/JointState "header:
 seq: 0
 stamp: {secs: 0, nsecs: 0}
 frame_id: ''
 name: ['ptu_pan','ptu_tilt']
 position: [-1,0]  # Note the format
 velocity: [0.5,0.5]
 effort: [0]" 
```
   - 更多详情，请参考`cmd_angles.py`文件。
5. 您也可以使用`test.py`，类似Term Tera，来控制PTU。修改[ser.write(b"TP0\n")]中的值 – 命令与Term Tera中的相同。

========

**参考文档链接：**
- [FLIR PTU E46](https://www.flir.com/products/ptu-e46/?vertical=mcs&segment=oem)
  相关文档
  - E-SERIES-COMMAND-REFERENCE-MANUAL

**License**

in English:

FLIR PTU Usage Guide

**Windows:**
1. **Term Tera Serial Communication:**
   - Download Term Tera.
   - Connect Host RS232 to PC and choose the port COM5 (adaptive).
   - Power on the PTU; it will start auto-calibration. "Initializing" will be displayed in the window.
   - Once calibration is complete, refer to the document (E-SERIES-COMMAND-REFERENCE-MANUAL) for commands to input and control the PTU.

2. **Web Page Control:**
   - Connect to ETHERNET.
   - On the serial communication page, enter "NMD + space". Then enter "NI + space" to view the IP address.
   - Type the IP address into a browser to access the web page. Open PTU Configuration to set parameters. Refer to the documentation for specifics.

**Linux:**
1. Compile the flir_ptu package.
2. Run `source devel/setup.bash`.
3. Execute `roslaunch flir_ptu_driver ptu.launch` and in a new terminal `roslaunch flir_ptu_viz view_model.launch`.
4. Use `rostopic pub /ptu/cmd sensor_msgs/JointState` to send commands with the following format:
```
rostopic pub /ptu/cmd sensor_msgs/JointState "header:
 seq: 0
 stamp: {secs: 0, nsecs: 0}
 frame_id: ''
 name: ['ptu_pan','ptu_tilt']
 position: [-1,0]  # Note the format
 velocity: [0.5,0.5]
 effort: [0]" 
```
   - Refer to the `cmd_angles.py` file for more details.
5. You can also use `test.py`, similar to Term Tera, to control the PTU. Modify the value inside [ser.write(b"TP0\n")] – commands are the same as in Term Tera.

========

**Reference Document Links:**
- [FLIR PTU E46](https://www.flir.com/products/ptu-e46/?vertical=mcs&segment=oem)
  RELATED DOCUMENTS
  - E-SERIES-COMMAND-REFERENCE-MANUAL

**License**


