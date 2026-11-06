# ✨ The Ancient Scroll of Fibonacci ✨
# Inscribed by Kiro the Grey Hat
# A spell to summon the sacred sequence of numbers

def cast_fibonacci_spell(n):
    """Cast the Fibonacci spell to generate the first n numbers of the sequence."""
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# 🔮 Invoke the spell for the first 10 numbers
print("=" * 45)
print("   ✨ THE SCROLL OF FIBONACCI AWAKENS ✨")
print("=" * 45)

fib_sequence = cast_fibonacci_spell(10)

print(f"\n🌀 Summoning the first 10 Fibonacci numbers...\n")
for i, num in enumerate(fib_sequence, 1):
    print(f"   ✦ Term {i:>2}: {num}")

print(f"\n📜 The sacred sequence: {fib_sequence}")
print("\n" + "=" * 45)
print("   🧙 The spell is complete. So mote it be!")
print("=" * 45)
