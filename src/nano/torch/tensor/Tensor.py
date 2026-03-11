import numpy as np


class Tensor:
    """A lightweight tensor implementation wrapping NumPy arrays, mimicking PyTorch's API."""

    # ========================== Part 1 ==========================
    # Tensor as NumPy Wrapper
    # Core initialization: wrap raw data (list, scalar, or ndarray)
    # into a NumPy array and expose shape, size, and dtype properties.
    # =============================================================

    def __init__(self, data):
        if isinstance(data, np.ndarray):
            self.data = data
        else:
            self.data = np.array(data)
        self.shape = self.data.shape    # Tuple of dimension sizes, e.g. (2, 3) for a 2x3 matrix
        self.size = self.data.size      # Total number of elements in the tensor
        self.dtype = self.data.dtype    # Data type of elements, e.g. float64, int32

    # ========================== Part 2 ==========================
    # Operator Overloading + Broadcasting
    # Implement Python dunder methods so tensors support +, -, *, /
    # NumPy broadcasting rules apply automatically:
    #   - Scalars broadcast to any shape
    #   - Shapes are compared from trailing dimensions
    #   - Dimensions of size 1 stretch to match the other operand
    # =============================================================

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass

    # ========================== Part 3 ==========================
    # Matrix Multiplication with Shape Validation
    # Implements the @ operator behavior (like torch.matmul).
    # Rule: For 2D tensors (a x b) @ (b x c) -> (a x c)
    #        The inner dimensions must match, otherwise raise an error.
    # =============================================================

    def matmul(self, other):
        pass

    # ========================== Part 4 ==========================
    # Shape Manipulation — Views vs Copies
    # reshape(): Returns a new tensor with a different shape but same data.
    #            Total number of elements must remain unchanged.
    #            e.g. (2, 6) -> (3, 4) is valid, (2, 6) -> (3, 5) is not.
    # transpose(): Swaps axes of the tensor.
    #              For 2D: rows become columns and vice versa.
    #              Note: NumPy transpose returns a view (shared memory),
    #              not a copy — modifying one affects the other.
    # =============================================================

    def reshape(self):
        pass

    def transpose(self):
        pass

    # ========================== Part 5 ==========================
    # Reduction Operations Along Axes
    # Collapse one or more dimensions by aggregating values.
    # - sum():  Total of all elements (or along a specific axis)
    # - mean(): Average of all elements (or along a specific axis)
    # - max():  Maximum value (or along a specific axis)
    # When axis=None (default), reduces the entire tensor to a scalar.
    # When axis=N, reduces along that dimension:
    #   e.g. shape (2, 3) with axis=0 -> shape (3,)
    #        shape (2, 3) with axis=1 -> shape (2,)
    # =============================================================

    def sum(self):
        pass

    def mean(self):
        pass

    def max(self):
        pass
