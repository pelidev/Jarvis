def prompt_for_columns(cols_info):

    vals = []
    for c in cols_info:
        name, notnull = c[1], c[3]
        while True:
            val = input(f"{name}> ").strip()
            if not val and notnull:
                print(f"{name} cannot be empty!")
            else:
                vals.append(val or None)
                break
    return vals