import csv

def emailsender(names, titles, email, occasion):
    print("Hello,", titles, names, ",")
    print("Happy", occasion)
    print("Cheers")
    print("To:", email)



with open('emails', 'r') as csvfile:
    emailreader = csv.reader(csvfile, delimiter=',')
    for row in emailreader:
        emailsender(names=row[0], titles=row[1], email=row[2], occasion=row[3])



