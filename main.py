def student_record_system():
  
    names = ["Keith", "Lanz", "James", "Harold", "Dara", "Chuss", "Micoh", "Jurie", "Mary", "Jaddz"]
    grades = [92, 93, 78, 86, 95, 88, 82, 91, 87, 84]

    print("--- Student Record System ---")

   
    average = sum(grades) / len(grades)
    print(f"Class Average: {average:.2f}")


    sorted_grades = grades.copy()
    n = len(sorted_grades)
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_grades[j] > sorted_grades[j + 1]:
                sorted_grades[j], sorted_grades[j + 1] = sorted_grades[j + 1], sorted_grades[j]
    
    print(f"Grades in Ascending Order: {sorted_grades}")


    search_name = input("\nEnter student name to search: ")
    found = False
    
    for i in range(len(names)):
        if names[i].lower() == search_name.lower():
            print(f"Record Found! Name: {names[i]}, Grade: {grades[i]}")
            found = True
            break
    
    if not found:
        print("Student not found in the records.")

if __name__ == "__main__":
    student_record_system()