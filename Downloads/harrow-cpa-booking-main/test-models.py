from models import *
from application import db
from datetime import datetime
# print(Bookings.query.all())
print(datetime.strptime('14-12-2023', '%d-%m-%Y'))
rows = Bookings.query.filter_by(time_slot="Before school (7:00 to 7:30)", rid="A101", date=datetime.strptime('14-12-2023', '%d-%m-%Y')).first()
print(rows)
print(Bookings.query.all()[-1].date)
# Bookings.query.delete()
# db.session.commit()