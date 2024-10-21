import json
import random
from datetime import datetime, timedelta
from faker import Faker

fake = Faker()

# Sample data options for employees
designations = [
    "Software Engineer", "Senior Software Engineer", "Manager", "Data Scientist", "HR Specialist", 
    "DevOps Engineer", "Product Manager", "Sales Executive", "Technical Lead", "Chief Architect", 
    "Marketing Analyst", "Business Analyst"
]
departments = ["IT", "HR", "Sales", "Operations", "Finance", "Marketing", "Customer Support", "R&D", "Legal", "Procurement"]
bands = ["A1", "A2", "B1", "B2", "C1", "C2", "D1", "D2", "E"]
employee_types = ["Permanent", "Contract", "Intern"]
statuses = ["Active", "Inactive", "On Leave", "Retired", "Terminated"]
locations = [
    "New York", "San Francisco", "Chicago", "Boston", "Seattle", "Austin", "Los Angeles", "London", 
    "Berlin", "Tokyo", "Sydney", "Mumbai", "Dubai"
]
marital_statuses = ["Single", "Married", "Divorced", "Widowed"]
genders = ["Male", "Female", "Other"]
degrees = ["Bachelor's", "Master's", "Ph.D.", "Diploma", "Certification"]
skills_pool = ["Python", "Java", "SQL", "Project Management", "Data Analysis", "Leadership", "Cloud Computing", "Customer Relations"]
work_shifts = ["Day", "Night", "Rotational"]
languages = ["English", "Spanish", "French", "German", "Mandarin", "Hindi"]
certifications = ["AWS Certified", "PMP", "Scrum Master", "Cisco Certified", "Google Cloud Certified"]
benefits_list = ["Health Insurance", "Dental Insurance", "401k Match", "Childcare Support", "Gym Membership"]
professional_memberships = ["IEEE", "ACM", "CIPD", "CFA"]

def generate_employee(emp_id):
    # Random age between 22 and 60
    age = random.randint(22, 60)
    
    # Experience in years (between 0 and 40 years, depending on age)
    experience = random.randint(0, min(40, age - 22))
    
    # Random salary based on band and experience; higher bands generally get higher salaries
    band = random.choice(bands)
    salary = random.randint(30000, 80000) + (experience * 1500) + (bands.index(band) * 10000)
    
    # Bonus typically a percentage of salary
    bonus = round(salary * random.uniform(0.05, 0.20), 2)
    
    # Random date of joining (DOJ) within the last 30 years
    doj = fake.date_between(start_date='-30y', end_date='today')
    
    # Random date of birth based on age
    dob = doj - timedelta(days=365 * age)
    
    # Random manager id (except for the first few employees who have no manager)
    manager_id = random.randint(1, emp_id - 1) if emp_id > 1 else None
    
    # Random fields for finance, work environment, and other details
    last_promotion_date = fake.date_between(start_date=doj, end_date='today') if random.random() > 0.5 else None
    office_floor = random.randint(1, 20)
    cubicle_number = f"C-{random.randint(100, 999)}"
    parking_spot = f"P-{random.randint(1, 500)}" if random.random() > 0.5 else None
    tax_id = fake.ssn()
    bank_account_number = fake.iban()
    insurance_coverage = random.choice(benefits_list)
    
    employee = {
        # Basic Information
        "emp_id": emp_id,
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": f"{fake.first_name().lower()}.{fake.last_name().lower()}@company.com",
        "phone_number": fake.phone_number(),
        "dob": dob.strftime('%Y-%m-%d'),
        "gender": random.choice(genders),
        "marital_status": random.choice(marital_statuses),
        
        # Job Details
        "designation": random.choice(designations),
        "department": random.choice(departments),
        "employee_band": band,
        "employee_type": random.choice(employee_types),
        "status": random.choice(statuses),
        "location": random.choice(locations),
        "doj": doj.strftime('%Y-%m-%d'),
        "work_shift": random.choice(work_shifts),
        
        # Compensation
        "salary": salary,
        "bonus": bonus,
        "benefits": random.sample(benefits_list, k=random.randint(1, 3)),
        "stock_options": random.randint(0, 500),
        "overtime_eligibility": random.choice([True, False]),
        "annual_leave_balance": random.randint(5, 30),
        "sick_leave_balance": random.randint(0, 10),
        
        # Performance & Experience
        "experience": experience,
        "performance_rating": round(random.uniform(1.0, 5.0), 1),
        "last_promotion_date": last_promotion_date.strftime('%Y-%m-%d') if last_promotion_date else None,
        "years_since_last_promotion": (datetime.today().year - last_promotion_date.year) if last_promotion_date else 0,
        "performance_goal_completion": round(random.uniform(70, 100), 2),
        "project_completion_rate": round(random.uniform(60, 100), 2),
        
        # Management & Reporting
        "manager_id": manager_id,
        "team_size": random.randint(1, 20),
        "direct_reports": random.randint(0, 10),
        "project_allocations": random.randint(1, 5),
        
        # Education & Skills
        "education": random.choice(degrees),
        "certifications": random.sample(certifications, k=random.randint(0, 3)),
        "skills": random.sample(skills_pool, k=random.randint(2, 5)),
        "languages_spoken": random.sample(languages, k=random.randint(1, 3)),
        "training_completed": random.choice([True, False]),
        "professional_memberships": random.sample(professional_memberships, k=random.randint(0, 2)),
        
        # Work Environment
        "office_floor": office_floor,
        "cubicle_number": cubicle_number,
        "parking_spot": parking_spot,
        "remote_work": random.choice([True, False]),
        "preferred_work_location": random.choice(locations),
        
        # Financial Information
        "tax_id": tax_id,
        "bank_account_number": bank_account_number,
        "payroll_type": random.choice(["Monthly", "Bi-Weekly"]),
        "insurance_coverage": insurance_coverage,
        "retirement_plan": random.choice(["401k", "Pension"]),
        "monthly_deductions": random.randint(100, 1000),
        
        # IT & Access
        "employee_id_card": f"ID-{emp_id:05d}",
        "computer_serial_number": fake.ean13(),
        "vpn_access": random.choice([True, False]),
        "email_quota": f"{random.randint(2, 100)}GB",
        "system_access_level": random.choice(["Admin", "User", "Guest"]),
        "last_system_login": fake.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
        "is_on_call": random.choice([True, False])
    }
    
    return employee

# Generate 30,000 employees
employees = [generate_employee(emp_id=i+1) for i in range(15000)]

# Write to JSON file
with open("employees_15000_with_50_fields.json", "w") as outfile:
    json.dump(employees, outfile, indent=4)

print("Employee data with 50 fields generated and saved to employees_30000_with_50_fields.json")
