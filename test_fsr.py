import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import time

spi = busio.SPI(clock = board.SCK, MISO = board.MISO, MOSI = board.MOSI)
cs = digitalio.DigitalInOut(board.CE0)
mcp = MCP.MCP3008(spi, cs)
channel = AnalogIn(mcp, MCP.P0)

while(1):
	print('Raw ADC Value: ', channel.value)
	print('ADC Voltage: ' + str(channel.voltage) + ' V')
	time.sleep(0.5)
