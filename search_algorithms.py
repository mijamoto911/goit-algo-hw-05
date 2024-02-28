def bad_character_heuristic(pattern):
    bad_char = dict()
    m = len(pattern)

    for i in range(m - 1):
        bad_char[pattern[i]] = m - i - 1

    return bad_char

def boyer_moore(text, pattern):
    n = len(text)
    m = len(pattern)
    bad_char = bad_character_heuristic(pattern)

    i = 0

    while i <= n - m:
        j = m - 1

        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1

        if j < 0:
            return i, i + m - 1  

        i += max(1, j - bad_char.get(text[i + j], -1))

    return None  
    pass

def compute_lps_array(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

def kmp(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = compute_lps_array(pattern)
    i, j = 0, 0

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            return i - j, i - 1  

        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return None  

def rabin_karp(text, pattern):
    d = 256
    q = 101
    n = len(text)
    m = len(pattern)
    h_pattern = 0
    h_text = 0
    h = pow(d, m - 1, q)

    for i in range(m):
        h_pattern = (d * h_pattern + ord(pattern[i])) % q
        h_text = (d * h_text + ord(text[i])) % q

    for i in range(n - m + 1):
        if h_pattern == h_text and pattern == text[i:i + m]:
            return i, i + m - 1  

        if i < n - m:
            h_text = (d * (h_text - ord(text[i]) * h) + ord(text[i + m])) % q

    return None 