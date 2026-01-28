def manage_roster(enrolled, drop_requests, waitlist):
    """
    Processes student drop requests and adds from waitlist if needed.
    
    Args:
        enrolled: Set of currently enrolled student names
        drop_requests: List of student names requesting to drop
        waitlist: Set of students on the waitlist
    
    Returns:
        int: Count of final enrolled students
    """
    remaining_students = enrolled - set(drop_requests)

    if len(remaining_students) < 5:
        students_required = 7 - len(remaining_students)

        for i in range(students_required):
            if len(waitlist) == 0:
                break
            new_student = waitlist.pop()

            remaining_students.add(new_student)
            
    
    return len(remaining_students)
