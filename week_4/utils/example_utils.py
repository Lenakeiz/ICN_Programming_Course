def build_subject_demographics_module(subject_id, **meta):

    profile = {"subject_id": subject_id}
    profile.update(meta)
    return profile

def square_number(num):
  return num * num

def add_numbers(a, b):
  return a + b
