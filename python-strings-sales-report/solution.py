def build_sales_report(raw: str) -> str:
    """
    `raw` is multi-line text. Each meaningful line has the form
        item , quantity , price
    with arbitrary whitespace around each field.

    Processing rules, applied to every line from splitlines():
      1. Strip the line. Skip it if it is empty or starts
         with "#".
      2. Split on "," . Skip the line if it does not have
         exactly 3 fields.
      3. Strip each field. Skip the line if the quantity field
         is not made only of digits. Convert quantity with
         int() and price with float().
      4. Format the item as title case, truncated to at most 12
         characters (slice AFTER applying title case).
      5. line_total = quantity * price.

    Build these output lines, in order, joined by "\\n" with
    no trailing newline:
      - Header: f"{'ITEM':<12}{'QTY':>4}{'PRICE':>10}{'TOTAL':>12}"
      - One row per valid record, in input order:
          item (width 12, left), quantity (width 4, right),
          price (width 10, right, 2 decimals),
          line_total (width 12, right, 2 decimals, with
          thousands separators)
      - A separator line of 38 "-" characters (use *).
      - Grand total line: "TOTAL" left-aligned in width 26,
        then the sum of all line totals right-aligned in width
        12 with 2 decimals and thousands separators.
      - Summary line:
          f"Rows: {rows} | UTF-8 bytes in items: {bytes_total}"
        where `bytes_total` is the sum of the UTF-8 byte lengths
        of the formatted (title-cased, truncated) item labels.

    If there are no valid records, the report still contains the
    header, separator, a grand total of 0.00, and the summary
    with Rows: 0 and 0 bytes.
    """

    rows = 0
    bytes_total = 0
    grand_total = 0.0
    
    output_lines = [
        f"{'ITEM':<12}{'QTY':>4}{'PRICE':>10}{'TOTAL':>12}"
    ]
    for line in raw.splitlines():
        line = line.strip()
        if line.startswith("#") or not line:
            continue
        splitted = line.split(",")
        if len(splitted) != 3:
            continue

        item = splitted[0].strip().title()[:12]
        quantity = splitted[1].strip()
        price = float(splitted[2].strip())
        
        if not quantity.isdigit():
            continue
        quantity = int(quantity)
        
        line_total = quantity * price
        
        rows += 1
        grand_total += line_total
        bytes_total += len(item.encode("utf-8"))

        row_str = f"{item:<12}{quantity:>4}{price:>10.2f}{line_total:>12,.2f}"
        output_lines.append(row_str)
    
    
    output_lines.append("-" * 38)
    
    # 'TOTAL' needs width 26 (which perfectly aligns under ITEM, QTY, and PRICE widths combined: 12 + 4 + 10)
    output_lines.append(f"{'TOTAL':<26}{grand_total:>12,.2f}")
    
    output_lines.append(f"Rows: {rows} | UTF-8 bytes in items: {bytes_total}")
    
    # Join everything with newlines
    return "\n".join(output_lines)
