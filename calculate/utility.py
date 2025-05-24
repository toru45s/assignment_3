class Calculator:
    @staticmethod
    def calculate(x, y, z):
      x = int(x)
      y = int(y)
      z = int(z)

      # Step-by-step operations
      step1 = x
      x += y       # 1. Add y to x
      step2 = x
      x -= z       # 2. Subtract z from x
      step3 = x
      x *= y       # 3. Multiply x by y
      step4 = x


      if z == 0:   # 5. Check for division by zero
          return {
             "error" : "Division by zero is not allowed."
          }
      x %= z       # 4. Modulus x with z
      step5 = x
      
      x /= z       # 5. Divide x by z
      step6 = x
      
      # 6. Add all values for final result
      final_result = x + y + z
      

      # Print the result
      return {
        'data': {
          'step1': step1,
          'step2': step2,
          'step3': step3,
          'step4': step4,
          'step5': step5,
          'step6': step6,
          'final_result': 
          {
             'x': x,
             'y': y,
             'z': z,
             'final_result': final_result
          }
        },
      }