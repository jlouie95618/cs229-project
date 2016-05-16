from subprocess import call

county_url = 'http://www.dartmouthatlas.org/downloads/tables/post_discharge_events_county_%s.xls'
hospital_url = 'http://www.dartmouthatlas.org/downloads/tables/post_discharge_events_hospital_%s.xls'
hrr_url = 'http://www.dartmouthatlas.org/downloads/tables/post_discharge_events_hrr_%s.xls'
state_url = 'http://www.dartmouthatlas.org/downloads/tables/post_discharge_events_state_%s.xls'

for i in xrange(10, 14): # upper bound exclusive
    target_url = hospital_url % str(i)
    call(['wget', target_url])
    target_url = hrr_url % str(i)
    call(['wget', target_url])
    target_url = state_url % str(i)
    call(['wget', target_url])
    target_url = county_url % str(i)
    call(['wget', target_url])