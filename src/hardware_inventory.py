items = [
    {"name": "  Cedar Plank (8ft) ", "supplier": "NORTHWOOD MILLS", "in_stock": 42,  "reorder_at": 50},
    {"name": "Brass Hinge (pair)",   "supplier": "kestrel supply",  "in_stock": 180, "reorder_at": 75},
    {"name": " Deck Screw (box) ",   "supplier": "Northwood Mills", "in_stock": 64,  "reorder_at": 64},
    {"name": "Copper Pipe (10ft)",   "supplier": "KESTREL SUPPLY",  "in_stock": 12,  "reorder_at": 30},
    {"name": "  Sanding Block",      "supplier": "harbor tool co",  "in_stock": 95,  "reorder_at": 40},
]


# === TIER B ===
# Each body is a single return statement. No loops, no list comprehensions.
# clean_name uses chained string methods. supplier_codes must use map() and
# a lambda.

def clean_name(name: str) -> str:
    """Return the name with the parenthetical size removed and the
    whitespace trimmed.

    Examples:
        clean_name("  Cedar Plank (8ft) ")  ->  'Cedar Plank'
        clean_name(" Deck Screw (box) ")    ->  'Deck Screw'
        clean_name("  Sanding Block")       ->  'Sanding Block'
    """
    pass


def supplier_codes(items: list) -> list:
    """Return each supplier as a lowercase code with spaces replaced by
    underscores.

    Example:
        supplier_codes(items)  ->
        ['northwood_mills', 'kestrel_supply', 'northwood_mills', 'kestrel_supply', 'harbor_tool_co']
    """
    pass


# === TIER B+ ===
# Must use map() and a lambda. Body is a single return statement.
# No loops, no list comprehensions.

def stock_flags(items: list) -> list:
    """Return "Reorder" for each item whose stock has fallen below its
    reorder point, "OK" otherwise.

    Example:
        stock_flags(items)  ->  ['Reorder', 'OK', 'OK', 'Reorder', 'OK']
    """
    pass


# === TIER A-, A and A+ ===
# No loops. Bodies may be more than one line. map() and filter() must both
# be used.

def needs_reorder(items: list) -> list:
    """For every item below its reorder point, return a dict with keys
    "name" (cleaned as in clean_name) and "short_by" (how many units below
    the reorder point it is).

    Example:
        needs_reorder(items)  ->
        [{'name': 'Cedar Plank', 'short_by': 8}, {'name': 'Copper Pipe', 'short_by': 18}]
    """
    pass


def supplier_count(items: list, supplier: str) -> int:
    """Return how many items come from the given supplier. The supplier is
    a code in the same form supplier_codes produces.

    Examples:
        supplier_count(items, "northwood_mills")  ->  2
        supplier_count(items, "harbor_tool_co")   ->  1
        supplier_count(items, "acme_lumber")      ->  0
    """
    pass


def restock_report(items: list, supplier: str) -> dict:
    """Return everything from one supplier that needs reordering, as a dict
    with keys "count" (how many items), "names" (their cleaned names) and
    "units" (the total number of units short across all of them).

    Examples:
        restock_report(items, "northwood_mills")  ->  {'count': 1, 'names': ['Cedar Plank'], 'units': 8}
        restock_report(items, "harbor_tool_co")   ->  {'count': 0, 'names': [], 'units': 0}
        restock_report([], "northwood_mills")     ->  {'count': 0, 'names': [], 'units': 0}
    """
    pass


def main():
    print('clean_name("  Cedar Plank (8ft) "):', repr(clean_name("  Cedar Plank (8ft) ")))
    print('clean_name(" Deck Screw (box) "):  ', repr(clean_name(" Deck Screw (box) ")))
    print('clean_name("  Sanding Block"):     ', repr(clean_name("  Sanding Block")))
    print()
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
