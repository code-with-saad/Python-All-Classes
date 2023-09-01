# create a dict or object

# d = {
#     "name": "Saad",
#     "gender": "male",
#     "dob": "2007"
# }
# print(d)

# # how to access specified items
# print(d["name"])
# print(d["gender"])

# del d["dob"]
# # print(d["dob"])
# print(d.get("dob"))
# print(d.get("dob", False))
# print(d.get("gender", False))


# create nested list
# d = {
#     "name": "Saad",
#     "gender": "male",
#     "dob": "2007",
#     "employe_info": {
#         "id": 1,
#         "joining_date": "2020"
#     }
# }

# print(d["employe_info"])
# print(d["employe_info"][id])

# nested_d = d["employe_info"]
# print(nested_d)
# print(nested_d["id"])


# how to update item from the list

# d = {
#     "name": "Saad",
#     "gender": "male",
#     "dob": "2007",
#     "employe_info": {
#         "id": 1,
#         "joining_date": "2020"
#     }
# }

# print(len(d))

# d.update({"name": "Kashif"})
# print(d["name"])


# d.update({"date_of_birth": "2007"})
# print(d["date_of_birth"])
# print(d["name"])
# print(d["dob"])
# d["name"] = "Hassan"
# d["dob"] = "2009"

# print(d["name"])
# print(d["dob"])


# d = {
#     "name": "Saad",
#     "gender": "male",
#     "dob": "2007",
#     "employe_info": {
#         "id": 1,
#         "joining_date": "2020"
#     }
# }

# print(d)
# del d["name"]
# print(d)


# how to empty the dict

# d = {
#     "name": "Saad",
#     "gender": "male",
#     "dob": "2007",
#     "employe_info": {
#         "id": 1,
#         "joining_date": "2020"
#     }
# }

# print(d)
# print(d.clear())
# print(d = {})


# how to display all the keys of the dict
# how to display all the values of the dict

# d = {
#     "name": "Saad",
#     "gender": "male",
#     "dob": "2007",
#     "employe_info": {
#         "id": 1,
#         "joining_date": "2020"
#     }
# }

# print(d.keys())
# print(d.values())


# how to merge two dicts

# d1 = {"a": 1, "b": 2, "c": 3}
# d2 = {"d": 4, "e": 5, "f": 6}

# d3 = d1 | d2
# print(d3)

# d4 = {**d1, **d2}
# print(d4)


# ======================== Exercises ===================================

# create a dict and add properties => name, age, gender
# update above dict using update function and add more information i.e salary, department, joining date
# remove the key "age" from the dict
# add new key "dob" to above dict
# overwrite above key "dob" with "date_of_birth"
# create another dict and name the variable as d2 and add info like "address", "street", "house_no"
# merge d1 and d2



d = {
    "name": "Saad",
    "age": 16,
    "gender": "Male"
}

# print(d)
d.update({"salary": "100000", "department": "computer_programming", "joining date": "2019"})
# print(d)
''
del d["age"]
# print(d)

d.update({"dob": 2007})
# print(d)

d["date_of_birth"] = d.pop("dob")
# print(d)

d2 = {"address": "ABC XYZ", "street": "xyz", "house_no": 123}

# print(d | d2)





# ================================ Loop =======================================

# l = list(range(10))

# user_friends = [1001, 22, 301, 444, 55, 67, 79, 81]

# for i in user_friends:
#     if i == 301:
#         continue
#     if i == 79:
#         break
#     print("Friends Id", i)


print("============================ My Shop ====================================")



# wish = "string"
# cold_drinks = ["pepsi", "fanta", "merinda", "7up", "sprite", "cococola", "string"]


# for cold_drink in cold_drinks:
#     if cold_drink == wish:
#         print("available")


# total_items_in_list = len(cold_drinks)
# new_list = list(range(total_items_in_list))

# for num in new_list:
#     if cold_drinks[num] == wish:
#         print("available")

# for num in range(len(cold_drinks)):
#     if cold_drinks[num] == wish:
#         print("available")


# wish = "string"
# cold_drinks = ["pepsi", "fanta", "merinda", "7up", "sprite", "cococola", "string"]

# for num in cold_drinks:
#     if num == wish:
#         print("available")
#         break
# else:
#     print("not available")


for i in range(1, 11, 1):
    print(f"2 x {i} = {i * 2}")


# reverse loop 
for i in range(0, -6, -1,):
    print(i)