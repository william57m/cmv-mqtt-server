import threading
import RPi.GPIO as GPIO


class CMV:

  def __init__(self, gpio_fan_restroom=22):
    # Init state
    self.reset(False)

    self.gpio_fan_restroom = gpio_fan_restroom

    # Init GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.gpio_fan_restroom, GPIO.OUT)

    # Fan timer
    # self.timer_fan_restroom = threading.Timer(60*20, self.set_state_fan_restroom, args=[False])
    # self.timer_fan_restroom.daemon = True

  # def set_state_fan_restroom(self, state):
  #   self.fan_restroom = state

  def reset(self, commit=True):
    self.fan_restroom = False

  def toggle_fan_restroom(self):
    self.fan_restroom = not self.fan_restroom
    output = GPIO.HIGH if self.fan_restroom else GPIO.LOW
    GPIO.output(self.gpio_fan_restroom, output)

    # if self.fan_restroom:
    #   self.timer_fan_restroom.start()
    # else:
    #   self.timer_fan_restroom.cancel()

  def get_state(self, key=None):
    result = {
      'fan_restroom': 'on' if self.fan_restroom else 'off',
    }
    return result[key] if key else result

