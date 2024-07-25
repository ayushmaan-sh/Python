# Customize a coffee order: S, M, L with an option for "Extra shot" of espresso

order_size = "Large"
extra_shot = True

if extra_shot:
    order = order_size + " coffee with extra shot of espresso"
else:
    order = order + " coffee"

print(order)