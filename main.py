from insert_category import insert_category
from insert_product import insert_product


Title = input("Title: ")
insert_category(Title = Title)



Title = input("Title: ")
Time_charging = input("Charging_time: ")
Category_id = int(input("Category id: "))

insert_product(Title = Title, Time_charging = Time_charging, Category_id = Category_id)