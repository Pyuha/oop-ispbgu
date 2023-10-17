strokes = 50
pages = 100
symbols = 25
value_mb = 1.44
save_byte = 4
value_kb = 1024


book = strokes*pages*symbols
value_b = int(value_mb*(value_kb**2))
count = book*save_byte
count_value = value_b//count
print("Количество книг, помещающихся на дискету:", count_value)
