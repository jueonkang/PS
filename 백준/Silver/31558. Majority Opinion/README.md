# [Silver I] Majority Opinion - 31558 

[문제 링크](https://www.acmicpc.net/problem/31558) 

### 성능 요약

메모리: 132896 KB, 시간: 160 ms

### 분류

애드 혹

### 제출 일자

2024년 9월 29일 11:09:10

### 문제 설명

<p>Farmer John has an important task - figuring out what type of hay to buy for his cows.</p>

<p>Farmer John's $N$ cows ($2 \le N \le 10^5$) are numbered $1$ through $N$ and each cow likes exactly one type of hay $h_i$ ($1 \le h_i \le N$). He wants all his cows to like the same type of hay.</p>

<p>To make this happen, Farmer John can host focus groups. A focus group consists of getting all cows in a contiguous range numbered $i$ to $j$, inclusive, together for a meeting. If there is a type of hay that more than half the cows in the group like, then after the focus group finishes meeting, all cows end up liking that type of hay. If no such type of hay exists, then no cows change the type of hay they like. For example, in focus group consisting of a range of 16 cows, 9 or more of them would need to have the same hay preference to cause the remaining cows to switch their preference to match.</p>

<p>Farmer John wants to know which types of hay can become liked by all cows simultaneously. He can only host one focus group at a time, but he can run as many focus groups as necessary to get all cows to like the same type of hay.</p>

### 입력 

 <p>The first will consist of an integer $T$, denoting the number of independent test cases $(1 \leq T \leq 10)$.</p>

<p>The first line of each test case consists of $N$.</p>

<p>The second line consists of $N$ integers, the favorite types of hay $h_i$ for the cows in order.</p>

<p>It is guaranteed that the sum of $N$ over all test cases does not exceed $2\cdot 10^5$.</p>

### 출력 

 <p>Output $T$ lines, one line per test case.</p>

<p>If it possible to make all cows like the same type of hay simultaneously, output all possible such types of hay in increasing order. Otherwise, output $-1$. When printing a list of numbers on the same line, separate adjacent numbers with a space, and be sure the line does not end with any extraneous spaces.</p>

