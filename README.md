# TabPad 
TabPad is an onscreen gamepad for Linux touchscreen devices (mainly tablets).

# Screenshot
![alt text](https://raw.githubusercontent.com/nitg16/TabPad/master/TabPad.jpg)

# Installation 
    sudo apt install python3-pyqt5 xdotool

# Running TabPad 
    python3 TabPad.py 

# Configuring TabPad  
Edit `TabPadConfig.py` file.

# TabPad is Not Transparent
TabPad transparency depends on your compositing manager. If the compositing manager do not support transparency, you may see an opaque or a translucent background. TapPad works absolutely fine with Compiz and Kwin.

# Current Limitations 
  * Diagonal movement keys are yet to be implemented.
  * Works only in games running in windowed mode (no fullscreen support yet).
