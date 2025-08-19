#  >>>>>>>>>>> Task2
#Comment the code below appropriately, and using doctring, explain what the code is doing.
#  Adapt the code to the case below.

#  Federal Government Scholarship Key Eligibility Requirements:
# Citizenship:
# This task is to determine who is eligible based on criterial set below
  # 1. Applicant must be a citizen of Nigeria. 
  # 2. Enrollment: Must be a registered, full-time undergraduate student in a recognized Nigerian university. 
  # 3. Other Scholarships outside Nigeria: Applicants cannot be currently receiving any other scholarship from an entity in the Oil and Gas industry, whether national or international. 
  # 4. Academic Qualification: For undergraduate courses, applicants usually need five distinctions (As and Bs) in relevant subjects in their WAEC/WASSCE (May/June) exams, including English and Mathematics.

# Taking inmformation Details of the applicant/student.>>>>>>>

name = input("Enter your full name Starting the Last-Name: ")
citizenship = input("Are you a citizen of Nigeria? (yes/no): ").strip().lower()
enrollment = input("Are you a full-time undergraduate in a Nigerian university? (yes/no): ").strip().lower()
other_scholarship = input("Are you a beneficial of any Oil and Gas scholarship? (yes/no): ").strip().lower()
waec_distinctions = int(input("Enter the number of WAEC distinctions you have here please (A/B grades) : "))
english_pass = input("Is your English Lang result is with at least a B grade? (yes/no): ").strip().lower()
math_pass = input("Is your Mathematics with at least a B grade? (yes/no): ").strip().lower()
age = input ( " Are you above 18 years Old? (yes/no):").strip().lower()
score = int(input("Enter your test score: "))
# condition of selection
eligibility = (
    citizenship == "yes" 
    and enrollment == "yes" 
    and other_scholarship == "no"
    and waec_distinctions >= 5
    and english_pass == "yes" 
    and math_pass == "yes"
)
print(" The outcome of your Eligibility Status:")
print("<>"*20)
print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility} \n{other_scholarship} \n{citizenship} \n{enrollment} \n{waec_distinctions} \n{english_pass} \n{math_pass }")
print("<>"*20)
print(eligibility)
