import numpy as np

def calculate(num_list):

  if len(num_list) < 9:   
    raise ValueError("List must contain nine numbers.")

  matrix = np.array(num_list).reshape(3,3)

  calculations = {
      "mean": [list(np.mean(matrix, axis=0)), list(np.mean(matrix, axis=1)), float(np.mean(matrix))],

      "variance": [list(np.var(matrix, axis=0)), list(np.var(matrix, axis=1)), float(np.var(matrix))],

      "standard deviation": [list(np.std(matrix, axis=0)), list(np.std(matrix, axis=1)), float(np.std(matrix))],

      "max": [list(np.max(matrix, axis=0)), list(np.max(matrix, axis=1)), float(np.max(matrix))],

      "min": [list(np.min(matrix, axis=0)), list(np.min(matrix, axis=1)), float(np.min(matrix))],

      "sum": [list(np.sum(matrix, axis=0)), list(np.sum(matrix, axis=1)), float(np.sum(matrix))],
  }

  #list(np.min(matrix, axis=0)) -> list() because otherwise it prints array([1,2,3])

  return calculations

