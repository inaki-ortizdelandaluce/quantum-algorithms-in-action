# Quantum Algorithms In Action

This repository contains practical implementations of quantum algorithms presented in the paper [_Quantum Algorithm Implementations for Beginners_](https://arxiv.org/abs/1804.03719). The goal of this project is to make foundational quantum algorithms more accessible to learners and developers by providing clear, well-documented code examples.

## 📘 Algorithms Included

- **Deutsch–Jozsa Algorithm**  
- **Bernstein–Vazirani Algorithm**  
- **Simon’s Algorithm**  
- **Grover’s Search Algorithm**  
- **Quantum Fourier Transform (QFT)**  
- **Shor’s Algorithm** (outline)

## 🧠 Goals

- Help beginners understand the logic behind quantum algorithms  
- Offer clean and easy-to-follow implementations using Python and Qiskit v2.0.0 
- Serve as a learning companion to the concepts discussed in the paper

## 🔧 Framework

Built with [Qiskit](https://qiskit.org) — IBM’s open-source quantum computing SDK.

---

## 🛠️ Project Setup (using Poetry)

This project uses [Poetry](https://python-poetry.org/) for dependency management and packaging.

### Prerequisites

Ensure Poetry is installed on your machine:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

## 🚀 Getting started

### Run poetry install to create your environment.
```
poetry install --no-root
```

### Activate the environment
```
poetry shell
```

### Use poetry run jupyter lab to launch your notebooks inside the managed environment.
```
jupyter notebook
```

