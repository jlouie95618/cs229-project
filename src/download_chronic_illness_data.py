from subprocess import call

hospital_url = 'http://www.dartmouthatlas.org/downloads/tables/DAP_hospital_data_%s.xls'
hrr_url = 'http://www.dartmouthatlas.org/downloads/tables/DAP_hrr_data_%s.xls'
state_url = 'http://www.dartmouthatlas.org/downloads/tables/DAP_state_data_%s.xls'

for i in xrange(2010, 2014): # upper bound exclusive
    target_url = hospital_url % str(i)
    call(['wget', target_url])
    target_url = hrr_url % str(i)
    call(['wget', target_url])
    target_url = state_url % str(i)
    call(['wget', target_url])