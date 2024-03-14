
int_list = list(map(int,input().split()))

if len(int_list) == 0:
    print(0)
else:
    new_dict = {}
    for i in range(len(int_list)):
        for j in range(i+1,len(int_list)+1):
            new_dict[tuple(int_list[i:j])] = sum(int_list[i:j])

keys = list(new_dict.keys())
values = list(new_dict.values())

index_num = values.index(max(values))
max_subarray = keys[index_num]

print(*max_subarray)
