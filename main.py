import timeit

from search_algorithms import boyer_moore,  kmp, rabin_karp

with open("article1.txt", "r", encoding="utf-8") as file:
    text1 = file.read()

with open("article2.txt", "r", encoding="utf-8") as file:
    text2 = file.read()

existing_pattern = "example"
non_existing_pattern = "randompattern"

existing_boyer_moore_text1 = timeit.timeit(lambda: boyer_moore(text1, existing_pattern), number=10)
non_existing_boyer_moore_text1 = timeit.timeit(lambda: boyer_moore(text1, non_existing_pattern), number=10)
existing_boyer_moore_text2 = timeit.timeit(lambda: boyer_moore(text2, existing_pattern), number=10)
non_existing_boyer_moore_text2 = timeit.timeit(lambda: boyer_moore(text2, non_existing_pattern), number=10)

existing_kmp_text1 = timeit.timeit(lambda: kmp(text1, existing_pattern), number=10)
non_existing_kmp_text1 = timeit.timeit(lambda: kmp(text1, non_existing_pattern), number=10)
existing_kmp_text2 = timeit.timeit(lambda: kmp(text2, existing_pattern), number=10)
non_existing_kmp_text2 = timeit.timeit(lambda: kmp(text2, non_existing_pattern), number=10)

existing_rabin_karp_text1 = timeit.timeit(lambda: rabin_karp(text1, existing_pattern), number=10)
non_existing_rabin_karp_text1 = timeit.timeit(lambda: rabin_karp(text1, non_existing_pattern), number=10)
existing_rabin_karp_text2 = timeit.timeit(lambda: rabin_karp(text2, existing_pattern), number=10)
non_existing_rabin_karp_text2 = timeit.timeit(lambda: rabin_karp(text2, non_existing_pattern), number=10)

if __name__ == '__main__':
    print(f"| {'Result': <10} | {'Boyer-Moore': <20} | {'Knuth-Morris-Pratt': <20} | {'Rabin-Karp': <20} |")
    print(f"| {'-'*10} | {'-'*20} | {'-'*20} | {'-'*20} |")
    
    print(f"| {'Text 1':<10} | {existing_boyer_moore_text1:20.5f} | {existing_kmp_text1:20.5f} | {existing_rabin_karp_text1:20.5f} | ")
    print(f"| {'Text 1':<10} | {non_existing_boyer_moore_text1:20.5f} | {non_existing_kmp_text1:20.5f} | {non_existing_rabin_karp_text1 :20.5f} | ")
    print(f"| {'Text 2':<10} | {existing_boyer_moore_text2:20.5f} | {existing_kmp_text2:20.5f} | {existing_rabin_karp_text2:20.5f} | ")
    print(f"| {'Text 2':<10} | {non_existing_boyer_moore_text2:20.5f} | {non_existing_kmp_text2:20.5f} | {non_existing_rabin_karp_text2:20.5f} | ")
    
    
    