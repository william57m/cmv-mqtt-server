import codes

from enum import Enum
from rpi_rf import RFDevice

class CMV:

  def __init__(self, gpio=17):
    # Init state
    self.reset(False)

    # Init RF
    self.rfdevice = RFDevice(gpio)
    self.rfdevice.enable_tx()
    self.rfdevice.tx_repeat = 10

  def reset(self, commit=True):
    self.fan_restroom = False

    if commit:
      self.commit()

  def toggle_fan_restroom(self):
    self.fan_restroom = not self.fan_restroom
    self.commit(codes.CODE_TOGGLE_RELAY)

  def get_state(self, key=None):
    result = {
      'fan_restroom': 'on' if self.fan_restroom else 'off',
    }
    return result[key] if key else result

  def commit(self, code=None):
    print(f'SEND RF CODE: {code}')
    self.rfdevice.tx_code(code)
