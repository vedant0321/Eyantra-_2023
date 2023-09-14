# Main function
if __name__ == '__main__':
    
    # Take the T (test_cases) input
    test_cases = int(input())

    # Write your code from here
    for i in range(test_cases):
        students_scores = []
        n = int(input())
        for i in range(n):
            input_line=input()
            parts = input_line.split()
            name, score = parts[0], float(parts[1])
            students_scores.append((name, score))

        scores_dict = {}

        for student, score in students_scores:
            if student not in scores_dict:
                scores_dict[student] = score
            else:
                scores_dict[student] = max(scores_dict[student], score)
        max_score = max(scores_dict.values())
        max_score_students = [student for student, score in scores_dict.items() if score == max_score]
        max_score_students.sort()
        for student in max_score_students:
            print(student)
