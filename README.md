# NanoTorch

A tiny implementation of PyTorch built from scratch for learning purposes.

> *"Don't import torch. Build it."*

This project follows the [TinyTorch curriculum](https://mlsysbook.ai/tinytorch/intro.html) from the ML Systems Book. The goal is to understand PyTorch internals by implementing core components from the ground up using only NumPy.

## Project Structure

```
NanoTorch/
├── src/
│   └── nano/
│       └── torch/
│           ├── __init__.py
│           └── tensor/
│               ├── __init__.py
│               └── Tensor.py
├── requirements.txt
├── setup.py
└── README.md
```

## Usage

```python
from nano.torch import Tensor

t = Tensor([1, 2, 3])
print(t.shape)  # (3,)
print(t.dtype)  # float64
```

## Roadmap

### Foundation Tier

| Module | Topic | Status |
|--------|-------|--------|
| 01 | Tensor Operations | In Progress |
| 02 | Activation Functions | Planned |
| 03 | Neural Network Layers | Planned |
| 04 | Loss Functions | Planned |
| 05 | Data Loading | Planned |
| 06 | Automatic Differentiation | Planned |
| 07 | Optimization Algorithms | Planned |
| 08 | Training Workflows | Planned |

### Architecture Tier

| Module | Topic | Status |
|--------|-------|--------|
| 09 | Convolutional Operations | Planned |
| 10 | Tokenization | Planned |
| 11 | Embedding Layers | Planned |
| 12 | Attention Mechanisms | Planned |
| 13 | Transformer Architectures | Planned |

### Optimization Tier

| Module | Topic | Status |
|--------|-------|--------|
| 14 | Profiling | Planned |
| 15 | Quantization | Planned |
| 16 | Compression | Planned |
| 17 | Hardware Acceleration | Planned |
| 18 | Memoization | Planned |
| 19 | Benchmarking | Planned |

### Capstone

| Module | Topic | Status |
|--------|-------|--------|
| 20 | Torch Olympics | Planned |

## Setup

```bash
# Clone the repository
git clone https://github.com/CoderCouple/NanoTorch.git
cd NanoTorch

# Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install the package in development mode
pip install -e .
```

## Reference

- [TinyTorch Curriculum — ML Systems Book](https://mlsysbook.ai/tinytorch/intro.html)
