items = [
    {"name": "  Cedar Plank (8ft) ", "supplier": "NORTHWOOD MILLS", "in_stock": 42,  "reorder_at": 50},
    {"name": "Brass Hinge (pair)",   "supplier": "kestrel supply",  "in_stock": 180, "reorder_at": 75},
    {"name": " Deck Screw (box) ",   "supplier": "Northwood Mills", "in_stock": 64,  "reorder_at": 64},
    {"name": "Copper Pipe (10ft)",   "supplier": "KESTREL SUPPLY",  "in_stock": 12,  "reorder_at": 30},
    {"name": "  Sanding Block",      "supplier": "harbor tool co",  "in_stock": 95,  "reorder_at": 40},
]


# === TIER B ===
# Must use map() and a lambda. Body is a single return statement.
# No loops, no list comprehensions.

def item_names(items: list) -> list:
    """Return each name with the parenthetical size removed and the
    whitespace trimmed."""
    pass


def supplier_codes(items: list) -> list:
    """Return each supplier as a lowercase code with spaces replaced by
    underscores."""
    pass


# === TIER B+ ===
# Same constraint as Tier B.

def stock_flags(items: list) -> list:
    """Return "Reorder" for each item whose stock has fallen below its
    reorder point, "OK" otherwise."""
    pass


# === TIER A-, A and A+ ===
# No loops. Bodies may be more than one line. map() and filter() must both
# be used.

def needs_reorder(items: list) -> list:
    """For every item below its reorder point, return a dict with keys
    "name" (cleaned as in item_names) and "short_by" (how many units below
    the reorder point it is)."""
    pass


def supplier_count(items: list, supplier: str) -> int:
    """Return how many items come from the given supplier. The supplier is
    a code in the same form supplier_codes produces."""
    pass


def restock_report(items: list, supplier: str) -> dict:
    """Return everything from one supplier that needs reordering, as a dict
    with keys "count" (how many items), "names" (their cleaned names) and
    "units" (the total number of units short across all of them)."""
    pass


def main():
    print("item_names:    ", item_names(items))
    print("supplier_codes:", supplier_codes(items))
    print("stock_flags:   ", stock_flags(items))
    print("needs_reorder: ", needs_reorder(items))
    print()
    print('supplier_count(items, "northwood_mills"):', supplier_count(items, "northwood_mills"))
    print('supplier_count(items, "kestrel_supply"): ', supplier_count(items, "kestrel_supply"))
    print('supplier_count(items, "harbor_tool_co"): ', supplier_count(items, "harbor_tool_co"))
    print('supplier_count(items, "acme_lumber"):    ', supplier_count(items, "acme_lumber"))
    print()
    print('restock_report(items, "northwood_mills"):', restock_report(items, "northwood_mills"))
    print('restock_report(items, "kestrel_supply"): ', restock_report(items, "kestrel_supply"))
    print('restock_report(items, "harbor_tool_co"): ', restock_report(items, "harbor_tool_co"))
    print('restock_report(items, "acme_lumber"):    ', restock_report(items, "acme_lumber"))
    print('restock_report([], "northwood_mills"):   ', restock_report([], "northwood_mills"))


if __name__ == "__main__":
    main()
