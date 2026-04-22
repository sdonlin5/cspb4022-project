#!/usr/bin/env python
#from database import db_create,
import database as db 
import pipeline as pipe



raw_pbp = pipe.extract_pbp()
raw_pt = pipe.extract_participation()
raw_ch = pipe.extract_charting()
raw_sched = pipe.extract_schedules()



print(raw_pbp.describe(), '\n'*2)

print(raw_pt.describe(), '\n'*2)
print(raw_ch.describe(), '\n'*2)
print(raw_sched.describe(), '\n'*2)






    