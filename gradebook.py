last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]
subjects = ['physics','calculus','poetry','history']
subjects.append("computer science")
grades = [98,97,85,88]
grades.append(100)
gradebook = list(zip(subjects,grades))
gradebook.append(("visual arts", 93))
full_gradebook = gradebook + last_semester_gradebook
print(full_gradebook)







































