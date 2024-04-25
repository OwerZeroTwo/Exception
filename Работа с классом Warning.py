import warnings

def division_warning(numerator, denominator):
    if abs(denominator) < 0.01:
        warnings.warn("Предупреждение: Деление на число, близкое к нулю, может привести к неожиданному поведению", UserWarning)
    return numerator / denominator

# Управление выводом предупреждений
# always - всегда выводить, ignore - игнорировать, error - обращать в ошибку
warnings.simplefilter("always")  # Выберите нужный вариант здесь

result = division_warning(10, 0.005)
print("Результат деления:", result)
