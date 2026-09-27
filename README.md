# Chapter 3 Assessment — Hardware inventory

This is a **timed, graded assessment**. You have **33 minutes**. You may attempt the tiers in any order.

Write your code in `src/hardware_inventory.py`. The data is already there.

## Checking your work

**There are no tests.** The expected outputs below are how you check your work. Run the file and compare what it prints with this README:

```
python src/hardware_inventory.py
```

## Grade bands

| Completed                     | Grade |
|-------------------------------|-------|
| 1 of the two Tier B functions | C+    |
| both Tier B functions         | B     |
| + `stock_flags`               | B+    |
| + `needs_reorder`             | A-    |
| + `supplier_count`            | A     |
| + `restock_report`            | A+    |

## Data

```python
items = [
    {"name": "  Cedar Plank (8ft) ", "supplier": "NORTHWOOD MILLS", "in_stock": 42,  "reorder_at": 50},
    {"name": "Brass Hinge (pair)",   "supplier": "kestrel supply",  "in_stock": 180, "reorder_at": 75},
    {"name": " Deck Screw (box) ",   "supplier": "Northwood Mills", "in_stock": 64,  "reorder_at": 64},
    {"name": "Copper Pipe (10ft)",   "supplier": "KESTREL SUPPLY",  "in_stock": 12,  "reorder_at": 30},
    {"name": "  Sanding Block",      "supplier": "harbor tool co",  "in_stock": 95,  "reorder_at": 40},
]
```

- "Below the reorder point" means strictly below. An item sitting exactly at its reorder point is OK.
- An item with no parenthetical in its name is still a valid name.

---

## Tier B: map, a lambda, chained string methods

**Constraint:** You must use `map()` and a lambda. The body is a single `return` statement. No loops and no list comprehensions.

### 1. `item_names(items: list) -> list`

Each name with the parenthetical size removed and the whitespace trimmed.

```python
item_names(items)
['Cedar Plank', 'Brass Hinge', 'Deck Screw', 'Copper Pipe', 'Sanding Block']
```

### 2. `supplier_codes(items: list) -> list`

Each supplier as a lowercase code with spaces replaced by underscores.

```python
supplier_codes(items)
['northwood_mills', 'kestrel_supply', 'northwood_mills', 'kestrel_supply', 'harbor_tool_co']
```

---

## Tier B+: a conditional expression inside the lambda

**Constraint:** Same as Tier B.

### 3. `stock_flags(items: list) -> list`

For each item, the string `"Reorder"` if its stock has fallen **below** its reorder point, `"OK"` otherwise. A plain list of strings.

```python
stock_flags(items)
['Reorder', 'OK', 'OK', 'Reorder', 'OK']
```

---

## Tier A-: filter and map combined

**Constraint from here on:** No loops. Bodies may be more than one line, and you choose the structure. You must use both `map()` and `filter()`.

### 4. `needs_reorder(items: list) -> list`

For every item that has fallen below its reorder point, a dict with `"name"` (cleaned as in function 1) and `"short_by"` (how many units below the reorder point it is).

```python
needs_reorder(items)
[{'name': 'Cedar Plank', 'short_by': 8}, {'name': 'Copper Pipe', 'short_by': 18}]
```

---

## Tier A: filter and a combine step

### 5. `supplier_count(items: list, supplier: str) -> int`

How many items come from the given supplier. The supplier arrives as a code in the same form function 2 produces.

```python
supplier_count(items, "northwood_mills")   # 2
supplier_count(items, "kestrel_supply")    # 2
supplier_count(items, "harbor_tool_co")    # 1
supplier_count(items, "acme_lumber")       # 0
```

---

## Tier A+: pull it together

### 6. `restock_report(items: list, supplier: str) -> dict`

Everything from one supplier that needs reordering, as a single dictionary with the keys `"count"` (how many items), `"names"` (their cleaned names), and `"units"` (the total number of units short across all of them).

```python
restock_report(items, "northwood_mills")   # {'count': 1, 'names': ['Cedar Plank'], 'units': 8}
restock_report(items, "kestrel_supply")    # {'count': 1, 'names': ['Copper Pipe'], 'units': 18}
restock_report(items, "harbor_tool_co")    # {'count': 0, 'names': [], 'units': 0}
restock_report(items, "acme_lumber")       # {'count': 0, 'names': [], 'units': 0}
restock_report([], "northwood_mills")      # {'count': 0, 'names': [], 'units': 0}
```
