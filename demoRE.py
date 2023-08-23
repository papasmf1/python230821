# demoRE.py
import re 

result = re.search("[0-9]*th", "  35th")
print(result)
print(result.group())
# result = re.match("[0-9]*th", "  35th")
# print(result)
# print(result.group())

print("---연도를 찾는경우---")
result = re.search("\d{4}", "올해는 2023년입니다.")
print(result.group())
print("---우편번호를 찾는경우---")
result = re.search("\d{5}", "우리 동네는 52300입니다.")
print(result.group())

