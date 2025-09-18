print("Welcome to the ICN programming course")

welcome_message = "Welcome to the ICN programming course"
print(welcome_message)
welcome_message = "Welcome to the ICN programming course for the third time!"
print(welcome_message)

#f-strings example
region = "hippocampus"; subj = 12
print(f"Subject {subj}: region = {region.title()}")

#concatenation
task, modality = "n-back", "fMRI"
label = task + " - " + modality  # "n-back - fMRI"

#case methods
ec_label = "entorhinal cortex"
print(ec_label.title())
pfc_label = "prefrontal"
print(pfc_label.upper())     
print(pfc_label.lower())

# tab and newline characters
print("ID\tAge\nS01\t23")

# trim examples
subject_name = "  S01  "
print(subject_name.strip())
print(subject_name.lstrip())
print(subject_name.rstrip())

# removing prefixes
subject_name = "sub_1"
subject_num = int(subject_name.removeprefix("sub_"))
print(subject_num)