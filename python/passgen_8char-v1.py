import random
import string
from datetime import date

today = date.today()

print(today)

win_admin_passwd = ''.join(random.choice(string.ascii_uppercase + string.ascii_uppercase + string.punctuation + string.punctuation + string.ascii_lowercase + string.ascii_lowercase + string.digits + string.digits) for _ in range(8))
#print('<Windows> - nx-admin'": " + win_admin_passwd)

win_analyst_passwd = ''.join(random.choice(string.ascii_uppercase + string.ascii_uppercase + string.punctuation + string.punctuation + string.ascii_lowercase + string.ascii_lowercase + string.digits + string.digits) for _ in range(8))
#print('<Windows> - nx-user'": " + win_user_passwd)

nx_admin_passwd =  ''.join(random.choice(string.ascii_uppercase + string.ascii_uppercase + string.punctuation + string.punctuation + string.ascii_lowercase + string.ascii_lowercase + string.digits + string.digits) for _ in range(8))
#print('<Nuix> - engines'": " + nx_admin_passwd)

nx_engines_passwd =  ''.join(random.choice(string.ascii_uppercase + string.ascii_uppercase + string.punctuation + string.punctuation + string.ascii_lowercase + string.ascii_lowercase + string.digits + string.digits) for _ in range(8))
#print('<Nuix> - engines'": " + nx_engines_passwd)

nx_reviewer_passwd =  ''.join(random.choice(string.ascii_uppercase + string.ascii_uppercase + string.punctuation + string.punctuation + string.ascii_lowercase + string.ascii_lowercase + string.digits + string.digits) for _ in range(8))
#print('<Nuix> - reviewer'": " + nx_reviewer_passwd)

win_admin_creds = ('Windows', 'Admin', win_admin_passwd )

win_analyst_creds = ("<Windows Username>: nx-analyst" + "   " + "Password: " + win_analyst_passwd)

nx_admin_creds = ("<Nuix Username>: nx-admin" + "   " + "Password: " + nx_admin_passwd)

nx_engines_creds = ("<Nuix Username>: engines" + "   " + "Password: " + nx_engines_passwd)

nx_reviewer_creds = ("<Nuix Username>: reviewer" + "   " + "Password: " + nx_reviewer_passwd)

#f = open("creds.txt", "a")
#f.write(win_admin_creds)
#f.write(win_analyst_creds)
#f.write(nx_admin_creds)
#f.close()

print(win_admin_creds)
print(win_analyst_creds)
print(nx_admin_creds)
print(nx_engines_creds)
print(nx_reviewer_creds)
