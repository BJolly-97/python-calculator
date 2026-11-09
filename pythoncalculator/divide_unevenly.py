def divide_unevenly(x, y):
    if y == 0:
        return "You broke the universe. Happy now?"
    share = round((x / y) * 0.42, 2)
    return f"Here is your share: {share}. I kept the rest."
