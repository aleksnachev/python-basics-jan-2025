kg_package = float(input())
delivery_standard = input()
km_delivery = int(input())
total_sum=0

if delivery_standard == "standard":
    if kg_package<1:
        total_sum=km_delivery*0.03
    elif kg_package<10:
        total_sum=km_delivery*0.05
    elif kg_package<40:
        total_sum=km_delivery*0.1
    elif kg_package<90:
        total_sum=km_delivery*0.15
    elif kg_package<150:
        total_sum=km_delivery*0.2
elif delivery_standard == "express":
    extra = 0
    extra_kg = 0
    extra_km = 0

    if kg_package < 1:
        total_sum = km_delivery * 0.03
        extra_kg = 0.8 * 0.03
        extra_km = kg_package * extra_kg
        extra = km_delivery * extra_km
        total_sum += extra
    elif 1<= kg_package < 10:
        total_sum = km_delivery * 0.05
        extra_kg = 0.4 * 0.05
        extra_km = kg_package * extra_kg
        extra = km_delivery * extra_km
        total_sum += extra
    elif 10<= kg_package < 40:
        total_sum = km_delivery * 0.1
        extra_kg = 0.05 * 0.1
        extra_km = kg_package * extra_kg
        extra = km_delivery * extra_km
        total_sum += extra
    elif 40<= kg_package < 90:
        total_sum = km_delivery * 0.15
        extra_kg = 0.02*0.15
        extra_km = kg_package*extra_kg
        extra = km_delivery*extra_km
        total_sum+=extra
    elif 90<= kg_package < 150:
        total_sum = km_delivery * 0.2
        extra_kg = 0.01 * 0.2
        extra_km = kg_package * extra_kg
        extra = km_delivery * extra_km
        total_sum += extra

print(f"The delivery of your shipment with weight of {kg_package:.3f} kg. would cost {total_sum:.2f} lv.")
