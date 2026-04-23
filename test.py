#!/usr/bin/env python
#from database import db_create,
import database as db 
import pipeline as pipe

raw_pbp = pipe.extract_pbp()
raw_ch = pipe.extract_charting()
raw_pt = pipe.extract_participation()
raw_sched = pipe.extract_schedules()

#print('pbp schema: ', raw_pbp.schema)
#print('charting schema ',raw_ch.schema)
#print('participation schema ', raw_pt.schema, "\n\n")

res = pipe.transform_play(raw_pbp, raw_ch, raw_pt)
#qa_df = res.fetch(10)
#print(qa_df)


#play_data = pipe.transform_play(raw_pbp, raw_ch, raw_pt)



#pipe.transform_play(raw_pbp, raw_ch, raw_pt)

#print(play_table_data.describe()

    