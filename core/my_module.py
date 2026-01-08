test = "Test String"

def find_index(sequence, target):
     """Return index of target or -1 if not found"""
     for i, value in enumerate(sequence):
         if value == target:
             return i
     return -1