def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        try:
            result = func(int_list)
            results[func.__name__] = result
        except Exception as e:
            print(f"Возникло исключение: {e}")
            continue
    return results

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))