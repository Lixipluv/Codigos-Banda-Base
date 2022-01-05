from encoding import Encoding

import matplotlib.pyplot as plt
import numpy as np

class B8ZS(Encoding):
  def __init__(self, bits:str):
    super().__init__(bits)
    self.code = self.encode()


  def encode(self) -> tuple:
    timestamp = [0]
    counter = 0
    earliestZero = -1
    state = 1
    code = [0]

    for index, bit in enumerate(self.bits):
      if bit == 1:
        earliestZero = -1
        state = 1 if state == -1 else -1
        code.append(state)
        timestamp.append(counter)
        counter += 1
        timestamp.append(counter)
        code.append(state)

      elif bit == 0:
        if earliestZero == -1:
          earliestZero = index

        if index - earliestZero == 7:
          code.append(0)
          timestamp.append(counter)
          counter += 1
          code.append(0)
          timestamp.append(counter)

          code[earliestZero*2 + 7] = state
          code[earliestZero*2 + 8] = state
          state = 1 if state == -1 else -1
          code[earliestZero*2 + 9] = state
          code[earliestZero*2 + 10] = state

          code[earliestZero*2 + 13] = state
          code[earliestZero*2 + 14] = state
          state = 1 if state == -1 else -1
          code[earliestZero*2 + 15] = state
          code[earliestZero*2 + 16] = state
          
          earliestZero = -1
        
        else:
          code.append(0)
          timestamp.append(counter)
          counter += 1
          code.append(0)
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
