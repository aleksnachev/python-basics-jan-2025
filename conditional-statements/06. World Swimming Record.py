record = float(input())
meeters = float(input())
sec_one_m = float(input())

delay = (meeters // 15) * 12.5
swimming_record = (meeters * sec_one_m) + delay

if record > swimming_record:
    print(f"Yes, he succeeded! The new world record is {abs(swimming_record):.2f} seconds.")

else:
    print(f"No, he failed! He was {abs(record - swimming_record):.2f} seconds slower.")
