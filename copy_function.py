# copy_function

# def copy(file_name, new_file_name):
#     with open(file_name) as file:
#         text = file.read()
    
#     with open(new_file_name, "w") as new_file:
#         new_file.write(text)


# copy("story2.txt", "story2_copy.txt")



def copy_and_reverse(file_name, new_file_name):
    with open(file_name) as file:
        text = file.read()

    with open(new_file_name, "w") as new_file:
        new_file.write(text[::-1])

copy_and_reverse("story2.txt", "story2_copy.txt")
