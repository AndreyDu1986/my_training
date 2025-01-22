def all_variants(text):
    n = len(text)
    for mask in range(1 << n):
        result = []
        for i in range(n):
            if mask & (1 << i):
                result.append(text[i])
        yield ''.join(result)

if __name__ == "__main__":
    a = all_variants("abc")
    for i in a:
        print(i)