# Hextroadinary

## Description

Meet ROXy, a coder obsessed with being exclusively the world's best hacker. She specializes in short, cryptic, hard-to-decipher secret codes. The below hex values, for example, she did something with them to generate a secret code. Can you figure out what? Your answer should start with `0x`.

Values:
- `0xc4115`
- `0x4cf8`

## Solution

The description hints at an XOR operation ("exclusively" -> Exclusive OR). We can perform a bitwise XOR operation in Python to find the secret code.

```python
# XOR operation between the two hex values
print(hex(0xc4115 ^ 0x4cf8))
```

## Flag

`0xc0ded`