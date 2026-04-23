import pipeline as pipe

raw_pbp = pipe.extract_pbp()
raw_chart = pipe.extract_charting()
raw_part = pipe.extract_participation()
raw_sched = pipe.extract_schedules()

play_plan = pipe.transform_play(raw_pbp, raw_chart, raw_part)
sit_plan = pipe.transform_situation(raw_pbp, raw_chart)
sched_plan = pipe.transform_schedule(raw_sched)

print(play_plan.fetch(5).glimpse())
print(sit_plan.fetch(5).glimpse())
print(sched_plan.fetch(5).glimpse())

