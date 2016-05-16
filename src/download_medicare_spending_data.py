from subprocess import call

county_url = 'http://www.dartmouthatlas.org/downloads/tables/pa_reimb_county_%s.xls'
hsa_url = 'http://www.dartmouthatlas.org/downloads/tables/pa_reimb_hsa_%s.xls'
hrr_url = 'http://www.dartmouthatlas.org/downloads/tables/pa_reimb_hrr_%s.xls'
state_url = 'http://www.dartmouthatlas.org/downloads/tables/pa_reimb_state_%s.xls'
for i in xrange(2003, 2013):
    print str(i)
    target_url = county_url % str(i)
    call(['wget', target_url])
    target_url = hsa_url % str(i)
    call(['wget', target_url])
    target_url = hrr_url % str(i)
    call(['wget', target_url])
    target_url = state_url % str(i)
    call(['wget', target_url])
