
from models import *
from datetime import date
# Create Faculty instances
faculty1 = Faculty.objects.create(faculty_id=1, faculty_name='Dr. John Doe')
faculty2 = Faculty.objects.create(faculty_id=2, faculty_name='Prof. Jane Smith')
faculty3 = Faculty.objects.create(faculty_id=3, faculty_name='Mr. Mike Johnson')

# Create Student instances
student1 = Student.objects.create(student_id=1, student_name='Alice Johnson')
student2 = Student.objects.create(student_id=2, student_name='Bob Smith')
student3 = Student.objects.create(student_id=3, student_name='Charlie Brown')

# Create Internship instances
internship1 = Internship.objects.create(
    id=1,
    student=student1,
    org_name='Tech Corp',
    org_address='123 Tech Street',
    nature_of_work='Software Development',
    reporting_authority='Mr. A',
    start_date=date(2024, 6, 1),
    end_date=date(2024, 9, 1),
    internship_mode='Remote',
    stipend='Yes',
    ppo='Yes',
    status='Completed',
    offer_letter=None  # Assuming no file for simplicity
)

internship2 = Internship.objects.create(
    id=2,
    student=student2,
    org_name='Data Inc',
    org_address='456 Data Road',
    nature_of_work='Data Analysis',
    reporting_authority='Ms. B',
    start_date=date(2024, 7, 1),
    end_date=date(2024, 10, 1),
    internship_mode='Onsite',
    stipend='No',
    ppo='No',
    status='Ongoing',
    offer_letter=None
)

# Create Announcement instances
announcement1 = Announcement.objects.create(
    from_faculty=faculty1,
    to_student=student1,
    message='Congratulations on completing your internship at Tech Corp!',
    created_at='2024-05-15T10:00:00Z'
)

announcement2 = Announcement.objects.create(
    from_faculty=faculty2,
    to_student=student2,
    message='Please submit your internship report by the end of this month.',
    created_at='2024-05-15T11:00:00Z'
)


# Assuming the previous data is already created, we are continuing from there

# Create more Internship instances
internship3 = Internship.objects.create(
    id=3,
    student=Student.objects.get(student_id=1),
    org_name='Innovative Solutions',
    org_address='789 Innovation Drive',
    nature_of_work='UI/UX Design',
    reporting_authority='Mr. C',
    start_date=date(2024, 8, 1),
    end_date=date(2024, 11, 1),
    internship_mode='Hybrid',
    stipend='Yes',
    ppo='No',
    status='Ongoing',
    offer_letter=None
)

internship4 = Internship.objects.create(
    id=4,
    student=Student.objects.get(student_id=2),
    org_name='Finance Plus',
    org_address='101 Finance Avenue',
    nature_of_work='Financial Analysis',
    reporting_authority='Ms. D',
    start_date=date(2024, 6, 15),
    end_date=date(2024, 9, 15),
    internship_mode='Remote',
    stipend='No',
    ppo='Yes',
    status='Completed',
    offer_letter=None
)

internship5 = Internship.objects.create(
    id=5,
    student=Student.objects.get(student_id=3),
    org_name='HealthTech',
    org_address='202 Health Blvd',
    nature_of_work='Machine Learning',
    reporting_authority='Dr. E',
    start_date=date(2024, 7, 1),
    end_date=date(2024, 10, 1),
    internship_mode='Onsite',
    stipend='Yes',
    ppo='Yes',
    status='Ongoing',
    offer_letter=None
)

internship6 = Internship.objects.create(
    id=6,
    student=Student.objects.get(student_id=3),
    org_name='EcoGreen',
    org_address='303 Green Lane',
    nature_of_work='Environmental Research',
    reporting_authority='Mr. F',
    start_date=date(2024, 5, 1),
    end_date=date(2024, 8, 1),
    internship_mode='Remote',
    stipend='No',
    ppo='No',
    status='Completed',
    offer_letter=None
)

internship7 = Internship.objects.create(
    id=7,
    student=Student.objects.get(student_id=1),
    org_name='Cyber Security Corp',
    org_address='404 Security Drive',
    nature_of_work='Cyber Security',
    reporting_authority='Ms. G',
    start_date=date(2024, 9, 1),
    end_date=date(2024, 12, 1),
    internship_mode='Hybrid',
    stipend='Yes',
    ppo='Yes',
    status='Upcoming',
    offer_letter=None
)

internship8 = Internship.objects.create(
    id=8,
    student=Student.objects.get(student_id=2),
    org_name='Marketing Solutions',
    org_address='505 Marketing St',
    nature_of_work='Digital Marketing',
    reporting_authority='Mr. H',
    start_date=date(2024, 8, 1),
    end_date=date(2024, 11, 1),
    internship_mode='Onsite',
    stipend='No',
    ppo='No',
    status='Upcoming',
    offer_letter=None
)

