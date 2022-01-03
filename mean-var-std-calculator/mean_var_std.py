import numpy as np

def calculate(liste):
  try:
    arr = np.array(liste).reshape(3,3)
  except:
    raise ValueError("List must contain nine numbers.")
  """
  if len(liste) != 9:
    raise ValueError("List must contain nine numbers.")
  else:
    arr =np.array(liste).reshape(3,3)
  """

  operations = {
      "mean": np.mean,
      "variance": np.var,
      "standard deviation": np.std, 
      "max": np.max, 
      "min": np.min, 
      "sum": np.sum
      }

  calculations = {
        k: [v(arr, axis=0).tolist(),
            v(arr, axis=1).tolist(),
            v(arr)
            ] for k, v in operations.items()
          }

  return calculations