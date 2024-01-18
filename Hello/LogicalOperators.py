# if applicant has high income AND good credit
    # Eligible for Loan
#And both should be true
#OR one should be true
has_high_income =input("Do you have high income ? (yes/no) :").lower() =='yes'

has_good_credit =input("do you have good credit ? (yes/no) :").lower()=='yes'

if has_good_credit and has_high_income :
    print("Eligible for loan")
else :
    print("Not eligible")

has_good_credit =True
has_criminal_Record=False
if has_good_credit and not has_criminal_Record :
    print("Eligible for loan")