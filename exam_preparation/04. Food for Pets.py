days = int(input())
all_food = float(input())
eaten_food = 0
dog_eaten = 0
cat_eaten = 0
biscuits_eaten = 0

for day in range(1,days+1):
    now_dog = float(input())
    now_cat = float(input())

    if day%3 == 0:
        biscuits_eaten += 0.1*(now_cat+now_dog)

    dog_eaten += now_dog
    cat_eaten+= now_cat
    eaten_food+= now_cat+now_dog

print(f"Total eaten biscuits: {round(biscuits_eaten)}gr.")
print(f"{(eaten_food/all_food*100):.2f}% of the food has been eaten.")
print(f"{(dog_eaten/eaten_food*100):.2f}% eaten from the dog.")
print(f"{(cat_eaten/eaten_food*100):.2f}% eaten from the cat.")
