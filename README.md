# 🛍️ Product Management System

This Python project implements a simple Product Management System with two classes: `product` and `product2`.

## 📚 Classes

### `product`

The `product` class represents a basic product with attributes such as `id`, `name`, `type`, and `price`. It includes methods for displaying product details (`show`) and retrieving the price (`getprice`).

### `product2`

The `product2` class inherits from `product` and extends it by adding a `rank` attribute. It overrides the `show` method to include the rank when displaying product details.

## 🚀 Example Usage

```python
# Create an instance of product2
p2 = product2(4, 2, 'Apple', 'iPhone', 2000)

# Display product details
p2.show()
```

## This will output :
```yaml
Name of Product: Apple
Type of Product: iPhone
Price: 2000
Rank: 4
```

## 📝 Installation

Clone the repository :

```bash
git clone https://github.com/your-username/product-management.git
```

Navigate into the project directory :

```bash
cd product-management
```
