import codes
import threading

from rpi_rf import RFDevice


class CMV:

  def __init__(self, gpio=17):
    # Init state
    self.reset(False)

    # Init RF
    self.rfdevice = RFDevice(gpio)
    self.rfdevice.enable_tx()
    self.rfdevice.tx_repeat = 10

    # Fan timer
    # self.timer_fan_restroom = threading.Timer(60*20, self.set_state_fan_restroom, args=[False])
    # self.timer_fan_restroom.daemon = True

  def reset(self, commit=True):
    self.fan_restroom = False

    if commit:
      self.commit()

  def set_state_fan_restroom(self, state):
    self.fan_restroom = state

  def toggle_fan_restroom(self):
    self.fan_restroom = not self.fan_restroom

    # if self.fan_restroom:
    #   self.timer_fan_restroom.start()
    # else:
    #   self.timer_fan_restroom.cancel()

    self.commit(codes.CODE_TOGGLE_RELAY)

  def get_state(self, key=None):
    result = {
      'fan_restroom': 'on' if self.fan_restroom else 'off',
    }
    return result[key] if key else result

  def commit(self, code=None):
    print(f'SEND RF CODE: {code}')
    self.rfdevice.tx_code(code)
