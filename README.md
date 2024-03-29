Після вимірювання часу виконання алгоритмів для обох текстів можна зробити наступні висновки:

- Boyer-Moore найшвидший для обох текстів.
- Алгоритм KMP також показує добрі результати, але трошки повільніший за Boyer-Moore.
- Rabin-Karp виявився менш ефективним порівняно з іншими алгоритмами для даної задачі.

Таким чином, для шукання підрядків у великих текстах рекомендується використовувати Boyer-Moore або KMP.

| Result     | Boyer-Moore          | Knuth-Morris-Pratt   | Rabin-Karp           |
| ---------- | -------------------- | -------------------- | -------------------- |
| Text 1     |              0.00755 |              0.01263 |              0.01887 | 
| Text 1     |              0.00374 |              0.01272 |              0.01893 | 
| Text 2     |              0.00701 |              0.01803 |              0.02840 | 
| Text 2     |              0.00344 |              0.01715 |              0.02869 | 