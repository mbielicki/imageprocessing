import numpy as np

class StructuralElement:
    def __init__(self, arr: np.ndarray, center: tuple = (1, 1), use: int = 1, reflected: bool = False) -> None:
        self.arr = arr
        self.center = center
        self._use = use
        self.reflected = reflected
        self.indices = self.get_indices(arr, center)

    def get_indices(self, arr: np.ndarray, center: tuple = (1, 1)) -> np.ndarray:
        return np.transpose(np.nonzero(arr == self._use)) - center
    
    def copy(self, use = None) -> 'StructuralElement':
        if use is None: use = self._use
        return StructuralElement(self.arr.copy(), self.center, use, self.reflected)
    
    def set_use(self, use: int) -> 'StructuralElement':
        return self.copy(use=use)
    
    def max(self) -> int:
        return np.max(np.abs(self.indices))
    
    def reflect(self) -> 'StructuralElement':
        new = self.copy()
        new.reflected = not self.reflected
        new.indices = -self.indices
        return new

iii = StructuralElement(
    np.array([[1, 1, 1],
             [1, 1, 1],
             [1, 1, 1]]),
    center=(1, 1)
)
rd = StructuralElement(
    np.array([[1, 1, 1],
             [1, 1, 1],
             [1, 1, 1]]),
    center=(0, 0)
)


plus = StructuralElement(
    np.array([[-1, 1, -1],
              [ 1, 1,  1],
              [-1, 1, -1]]),
    center=(1, 1)
)

v = StructuralElement(
    np.array(  [[-1, -1, -1],
                [-1,  1,  1],
                [-1,  1, -1]]), 
    center=(1, 1)
)   

xii = StructuralElement(
    np.array([[0,   0,   0],
                [-1,  1,  -1],
                [1,   1,   1]]),
    center=(1, 1)
)

j = StructuralElement(
    np.array([[-1, 1, -1],
                [0, 1, -1],
                [1, 1, -1]]),
    center=(2, 1)
)

reversed_L = StructuralElement(
    np.array([[1, 1, 0],
              [0, 1, 0],
              [0, 1, 0]]),
    center=(1, 1)
)
