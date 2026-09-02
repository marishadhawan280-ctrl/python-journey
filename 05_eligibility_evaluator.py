print("You have entered to ~Applicant Evaluation System~")
#Collect user inputs
gpa=float(input("Enter your current Gpa (0.0-10.0)"))
coding_score=int(input("Enter you current Coding Score/Tech stack(1-100)"))
has_preq=input("Do you have any prequisite knowledge? (yes/no)").strip().lower()=="yes"
has_flags=input("Do you have any penalty/flags? (yes/no)").strip().lower()=="yes"

# Composite evaluation score
composite_score = (gpa * 10 * 0.4) + (coding_score * 0.6)

print(f"\nCalculated Composite Score: {composite_score:.2f}")

# Multi-condition decision engine
if has_flags or not has_preq:
    print("Decision: Ineligible. Prerequisite incomplete or disciplinary flag active.")
elif gpa >= 8.5 and coding_score >= 80:
    print("Decision: Fast-Track Selection Granted!")
elif (gpa >= 7.5 or coding_score >= 85) and not has_flags:
    print("Decision: Selected for Technical Interview Round.")
else:
    print("Decision: Application deferred for standard pool review.")
