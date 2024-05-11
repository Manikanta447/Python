def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        char = string[i]
        if char == sub_string[0] and (len(string)-i)+1 > len(sub_string):
            temp_str = string[i:len(sub_string)+i]
            if temp_str == sub_string:
                count += 1
    return count

string = input().strip() //ABCDCDC
sub_string = input().strip() //CDC
    
count = count_substring(string, sub_string)
print(count) //COUNT = 2
