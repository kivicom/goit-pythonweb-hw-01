# 🚀 Python Homework: Factory Pattern & SOLID Principles

## 📌 Project Overview

This repository contains solutions to two Python programming exercises:

1. **Factory Pattern Implementation** - Implementing the Factory Design Pattern for vehicle creation.
2. **Applying SOLID Principles** - Refactoring a simple library management system to adhere to SOLID principles.

---

## 📍 Task 1: Factory Pattern Implementation

### 🔹 Description

This task involves implementing the **Factory Design Pattern** to create vehicles with different specifications based on regions (US/EU).

### 🔹 Key Features

- Implemented an **abstract base class `Vehicle`**.
- Created concrete classes: `Car` and `Motorcycle`.
- Introduced **factories**: `USVehicleFactory` and `EUVehicleFactory`.
- Used **logging** instead of `print` for better debugging.

### 🔹 Usage Example

```python
us_factory = USVehicleFactory()
eu_factory = EUVehicleFactory()

us_car = us_factory.create_car("Ford", "Mustang")
us_car.start_engine()

eu_motorcycle = eu_factory.create_motorcycle("BMW", "R1250GS")
eu_motorcycle.start_engine()
```

---

## 📍 Task 2: SOLID Principles Refactor

### 🔹 Description

This task involved refactoring a **library management system** to follow the SOLID principles:

- **S**: Separated book data (`Book`) from library management (`Library`).
- **O**: Allowed `Library` to be extended without modifying existing code.
- **L**: Created an interface `LibraryInterface` to ensure interchangeable implementations.
- **I**: Defined a clear contract with `LibraryInterface`.
- **D**: Introduced `LibraryManager` to interact with the library via an abstraction.

### 🔹 Key Features

- Created **`Book`** class for single responsibility.
- Implemented **`LibraryInterface`** for flexibility.
- Used **`LibraryManager`** to separate concerns.

### 🔹 Usage Example

```python
library = Library()
manager = LibraryManager(library)

manager.add_book("1984", "George Orwell", 1949)
manager.show_books()
manager.remove_book("1984")
manager.show_books()
```

---

## ⚡ Setup & Running Instructions

### 1️⃣ **Create & Activate Virtual Environment**

```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### 2️⃣ **Install Dependencies**

```sh
pip install black mypy pylint
```

### 3️⃣ **Run the Programs**

#### ✅ Factory Pattern

```sh
python vehicle_factory.py
```

#### ✅ SOLID Library Management

```sh
python solid_library.py
```

### 4️⃣ **Check Code Quality**

```sh
black .
mypy vehicle_factory.py solid_library.py
pylint vehicle_factory.py solid_library.py
```
