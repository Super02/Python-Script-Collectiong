def decimal_to_any_base(decimal, base):
  """
  Converts a decimal number to a number in any base.

  Args:
    decimal: The decimal number to convert.
    base: The base to convert to.

  Returns:
    A string representing the number in the given base.
  """

  if base < 2 or base > 16:
    raise ValueError("Invalid base.")

  digits = "0123456789ABCDEF"
  result = ""

  while decimal > 0:
    remainder = decimal % base
    result = digits[remainder] + result
    decimal //= base

  return result

if __name__ == "__main__":
  decimal = int(input("Enter a decimal number: "))
  base = int(input("Enter a base: "))
  print(f"{decimal} in base {base} is {decimal_to_any_base(decimal, base)}")
