# Display_Raspberry_pi_Stats
## Displaying Raspberry pi System Stats on TFT Display(SPI)
This python Script uses cskau's Python_ST7735 Library :
https://github.com/cskau/Python_ST7735.git

Install essential dependenciesusing
```
sudo apt-get update
sudo apt-get install build-essential python-dev python-smbus python-pip python-imaging python-numpy
```

For a Raspberry Pi make sure you have the RPi.GPIO and Adafruit GPIO libraries by executing:
```
sudo pip install RPi.GPIO
sudo pip install Adafruit_GPIO
```

instal it by 
```
git clone https://github.com/cskau/Python_ST7735.git
cd Python_ST7735/
python3 setup.py install
```
