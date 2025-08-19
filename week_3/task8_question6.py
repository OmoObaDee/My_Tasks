#     .......Task6
# The Federal Government of Nigeria has set the minimum age for admission into federal tertiary institutions at 16 years old for the 2025/2026 academic session, according to the Minister of Education, Dr. Tunji Alausa. This policy, announced at the 2025 JAMB policy meeting, replaces the previous 18-year minimum age requirement. 
# For the 2025/2026 academic session, the University of Lagos (UNILAG) requires candidates to have a minimum UTME score of 200 to be eligible for the Post-UTME screening. The Post-UTME itself is an online screening exercise. UNILAG does not release specific departmental cut-off marks before the screening. The departmental cut-off marks are determined after the Post-UTME, based on merit and the performance of candidates in both UTME and the Post-UTME. 

#><><><><> Breakdown of the Admission Process:
#  1. UTME:
# Candidates must score 200 or above in the UTME and choose UNILAG as their first choice. 
#  2. O'Level Requirements:
#Candidates must also have five (5) credit passes at one sitting in relevant O'Level subjects, including English Language and Mathematics. 
#   3. Post-UTME:
#Eligible candidates participate in the university's online Post-UTME screening. 
#  4. Departmental Cut-off Marks:
#  After the Post-UTME, the university determines departmental cut-off marks based on merit and overall performance
#(This can range from 200 to 320). 
#5. Final Admission:
#Candidates who meet the departmental cut-off marks are offered admission. 
#Write a program to account for all of the conditions above, Such that when a user imputes all their required details, they are told if they will be legible for admission or not.

#.... SOLUTION  .....


# print("*** OOU Admission Eligibility Checker (2025/2026) ***")
print("<><>"*30)
# Collecting user name
name = input("Enter your  Full name: ")
# Age requirement
age = int(input("Enter your age: "))
# UTME requirement
utme_score = int(input("Enter your UTME score: "))
first_choice = input("Did you choose OOU as your first choice? (Yes/No): ").title()
# O'Level requirement
olevel_credits = int(input("How many credit passes did you have in one sitting ? "))
english_pass = input("Did you pass English Language? (Yes/No): ").title()
math_pass = input("Did you pass Mathematics? (Yes/No): ").title()
# Post-UTME screening
post_utme_score = int(input("Enter your Post-UTME score (0-100): "))
# Step 5: Departmental cut-off (asking user)
dept_cutoff_marks = int(input("Enter your Departmental cut-off mark (200 - 320): "))

# Conditions for considering the user admission: must be at least 16 years old as at the time of application.
meets_age = age >= 16

# must be >= 200 and UNILAG as first choice
meets_utme_cutoff = (utme_score >= 200) and (first_choice == "Yes")
# must be 5 credits including English & Math
meets_olevel_subjects = (olevel_credits >= 5) and (english_pass == "Yes") and (math_pass == "Yes")

# total score for admission = UTME + Post-UTME
total_score = utme_score + post_utme_score
meets_cutoff = total_score >= dept_cutoff_marks

# Final decision
eligibility = meets_age and meets_utme_cutoff and meets_olevel_subjects and meets_cutoff
# mapping true and false to statement for final result
result = {
    True: f"Congratulations {name}, you have been offered Provisional admission to the course of your choice",
    False: f"Sorry, no admission yet"
}
print("*"*80)
print("\n=== Admission Status ===")
print(f"Status: {result[eligibility]}")
print("*"*80)











