employees = {"chef" : "Ashley", "ceo" : "WOODZ"}
print(employees["ceo"])

# adding in a new key-value pair
employees["waiter"] = "Mike"
print(employees) # {'chef': 'Ashley', 'ceo': 'WOODZ', 'waiter': 'Mike'}
print(employees["waiter"]) # Mike
print(employees["chef"]) # Ashley
# update to K-V
employees["chef"] = "Seung-yeon"
print(employees["chef"]) # Seung-yeon
print(employees["chef"].upper()) # SEUNG-YEON

stock_prices = {
    "GOOGL" : [200, 210, 220],
    "GME" : [20, 100, 300]
}

history = stock_prices["GOOGL"]
print(f"First day price is {history[0]}")

# 중첩된 딕셔너리
mydict = {
    "OUTER" : {"INNER" : 100}
}
print(mydict["OUTER"]) # {'INNER': 100}
print(mydict["OUTER"]["INNER"]) # 100

mydict2 = {
    "key1" : 100,
    "key2" : 200,
    "key3" : 400
}
print(mydict2.keys()) # dict_keys(['key1', 'key2', 'key3'])
print(mydict2.values()) # dict_values([100, 200, 400])
print(mydict2.items()) # dict_items([('key1', 100), ('key2', 200), ('key3', 400)]) -> 튜플 형태

# Q : 아래 정의된 딕셔너리에 키-값 쌍으로 "key4", 400을 추가한 다음, 업데이트된 딕셔너리의 모든 키-값 쌍을 출력하세요.
my_dict = {"key1": 100, "key2": 200, "key3": 300}

my_dict["key4"] = 400
print(my_dict.items())