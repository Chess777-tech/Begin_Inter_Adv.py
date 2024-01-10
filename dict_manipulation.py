# Create a dictionary with student names and their scores. Write code to print the average score and the student with the highest score.


student_scores = {
    'Alice': 85,
    'Bob': 92,
    'Charlie': 78,
    'David': 95,
    'Eva': 88
}

# Caluclate the avg score
average_score = sum(student_scores.values()) / len(student_scores)
print(f"Average Score: {average_score:.2f}")

# Find the student with the highest score 

highest_scorer = max(student_scores, key=student_scores.get)
print(f"Highest Scorer: {highest_scorer} with a score of {student_scores[highest_scorer]}")