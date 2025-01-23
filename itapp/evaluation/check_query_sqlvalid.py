from sqlvalidator import SQLValidator

# تعریف کوئری SQL
query = "SELECT * FROM users WHERE age > 18"

# ایجاد یک شیء SQLValidator
validator = SQLValidator()

# اعتبارسنجی کوئری
is_valid, errors = validator.validate(query)

# نمایش نتیجه
if is_valid:
    print("کوئری معتبر است.")
else:
    print("کوئری نامعتبر است:")
    for error in errors:
        print(f"- {error}")
