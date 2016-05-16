from subprocess import call

county_url = 'http://www.dartmouthatlas.org/downloads/tables/PC_County_rates_%s.xls'
hsa_url = 'http://www.dartmouthatlas.org/downloads/tables/PC_HSA_rates_%s.xls'
hrr_url = 'http://www.dartmouthatlas.org/downloads/tables/PC_HRR_rates_%s.xls'
state_url = 'http://www.dartmouthatlas.org/downloads/tables/PC_State_rates_%s.xls'

for i in xrange(2008, 2014): # upper bound exclusive
    target_url = county_url % str(i)
    call(['wget', target_url])
    target_url = hsa_url % str(i)
    call(['wget', target_url])
    target_url = hrr_url % str(i)
    call(['wget', target_url])
    target_url = state_url % str(i)
    call(['wget', target_url])
