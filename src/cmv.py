import RPi.GPIO as GPIO
import time
import smbus

bus_address = 0x48
bus = smbus.SMBus(1)

def open_close_relay(pin_number, timeout=0.2):
  GPIO.output(pin_number, GPIO.HIGH)
  time.sleep(timeout)
  GPIO.output(pin_number, GPIO.LOW)


class CMV:

  def __init__(self, gpio_fan_restroom=22):
    # Init state
    self.reset(False)
    self.read_state()

    # Init GPIO
    self.gpio_fan_restroom = gpio_fan_restroom
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.gpio_fan_restroom, GPIO.OUT)

  def set_internal_state_fan_restroom(self, state):
    self.fan_restroom = state

  def relay_high(self):
    GPIO.output(self.gpio_fan_restroom, GPIO.HIGH)

  def relay_low(self):
    GPIO.output(self.gpio_fan_restroom, GPIO.LOW)

  def reset(self, commit=True):
    self.fan_restroom = False

  def toggle_fan_restroom(self):
    self.fan_restroom = not self.fan_restroom
    open_close_relay(self.gpio_fan_restroom)

  def get_state(self, key=None):
    result = {
      'fan_restroom': 'on' if self.fan_restroom else 'off',
    }
    return result[key] if key else result

  def read_state(self):
    value = bus.read_byte(bus_address)
    print('READ STATE:')
    print(value)

