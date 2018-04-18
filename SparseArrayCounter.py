def query(data, queries):
    d = {}
    for entry in data:
        if d.get(entry):
            d[entry] += 1
        else:
            d[entry] = 1

    result = []
    for q in queries:
        if d.get(q):
            result.append(d.get(q))
        else:
            result.append(0)
    return result

if __name__ == "__main__":
    N = int(input().strip())
    input_strings = []
    for i in range(N):
        input_strings.append(input().strip())
    Q = int(input().strip())
    query_strings = []
    for i  in range(Q):
        query_strings.append(input().strip())

    res = query(input_strings, query_strings)
    for r in res:
        print(r)

