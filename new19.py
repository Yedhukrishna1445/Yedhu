import smtplib
s=smtp.SMTP("smtp.gmail.com",587)
s.starttls()
login("arathilyedhu@gmail.com","amma6565")
msg="Hi"
s.sendmail("arathilyedhu@gmail.com","ykreddy8055@gmail.com","Hi")
print("Sent")
s.quit()