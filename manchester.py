from encoding import Encoding

import matplotlib.pyplot as plt
import numpy as np

class ManchesterDif(Encoding):
  def __init__(self, bits:str):
    super().__init__(bits)
    self.code = self.encode()


  def encode(self) -> tuple:
    timestamp = [0]
    counter = 0
    state = -1
    code = [-1]

    for bit in self.bits:
      if bit == 0:
        state = -1 if state == 1 else 1
        code.append(state)
        timestamp.append(counter)
        counter += .5
        code.append(state)
        timestamp.append(counter)

      elif bit == 1:
        code.append(state)
        timestamp.append(counter)
        counter += .5
        code.append(state)
        timestamp.append(counter)

      state = -1 if state == 1 else 1
      code.append(state)
      timestamp.append(counter)
      counter += .5
      code.append(state)
      timestamp.append(counter)

    return code, timestamp

  
  def plot(self):
        fig, axs = plt.subplots(1)
        
        y_axis = self.code[0]
        x_axis = self.code[1]

        bit_code = [str(i) for i in self.bits]
        plt.xticks(np.arange(len(bit_code)), bit_code)
        plt.yticks([-1, 0, 1], ['-1', '', '1'])

        plt.plot(x_axis, y_axis, 'black', linewidth=2)
        plt.grid()
        plt.show()
