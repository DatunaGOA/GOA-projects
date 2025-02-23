

# 1) 
ch = input("შეიყვანეთ სიმბოლო: ").lower()
if ch in 'aeiou':
    print("ხმოვანია")
elif ch.isalpha():
    print("თანხმოვანი")
else:
    print("არც ხმოვანი და არც თანხმოვანი")

# 2) 
nums = [int(input(f"num {i+1}: ")) for i in range(4)]
nums.sort(reverse=True)  
max_product = nums[0] * nums[1]
print("max product: ", max_product)
