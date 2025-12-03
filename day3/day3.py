#!/usr/bin/env python3
from pathlib import Path


def max_two_digit(bank: str) -> int:
    bank = bank.strip()
    best_tens, best_ones = -1, -1
    best_suffix = -1

    for i in range(len(bank) - 2, -1, -1):
        best_suffix = max(best_suffix, int(bank[i + 1]))
        tens = int(bank[i])
        ones = best_suffix
        if (tens > best_tens) or (tens == best_tens and ones > best_ones):
            best_tens, best_ones = tens, ones

    return best_tens * 10 + best_ones

def max_k_digit_number_str(bank: str, k: int) -> str:
    bank = bank.strip()
    if len(bank) < k:
        raise ValueError(f"Bank length {len(bank)} < k={k}: {bank!r}")

    drops = len(bank) - k 
    stack = []

    for ch in bank:
        while drops and stack and stack[-1] < ch:
            stack.pop()
            drops -= 1
        stack.append(ch)

    if drops:
        stack = stack[:-drops]

    return "".join(stack[:k])


def solve_file(filename: str = "input.txt") -> int:
    text = Path(__file__).with_name(filename).read_text(encoding="utf-8")
    total = 0
    total2 = 0
    for line in text.splitlines():
        line = line.strip()
        if line:
            total += max_two_digit(line)
            total2 += int(max_k_digit_number_str(line, 12))
    return total, total2


print(solve_file("day3.txt"))