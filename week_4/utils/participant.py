class Participant:
    def __init__(self, subject_id, group):
        self.subject_id = subject_id
        self.group = group
    
    def describe(self):
        # 'self' is the object that called this method
        print(f"Participant {self.subject_id} is in group {self.group}")

    @staticmethod
    def greet():
        print("Welcome to our experiment!")