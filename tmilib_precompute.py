#!/usr/bin/env python
# md5: 9e1792e10e7372ce813df59698c71705
# coding: utf-8

from tmilib import *

tmi_overrides['basedir'] = '/home/gkovacs/tmi-data/local_2016-03-27_19:25:47-07:00'


'''
print 'get_mturkid_to_time_last_active'
get_mturkid_to_time_last_active()
print 'get_username_to_mturk_id'
get_username_to_mturk_id()
print 'get_mturkid_to_history_pages'
get_mturkid_to_history_pages()
print 'get_mturkid_to_history_visits'
get_mturkid_to_history_visits()
print 'get_domains_list'
get_domains_list()
'''


'''
if random.random() > 0.5:
  print 'history_pages_for_all_users_randomized'
  compute_history_pages_for_all_users_randomized()
else:
  print 'history_visits_for_all_users_randomized'
  compute_history_visits_for_all_users_randomized()
'''

#print 'history_ordered_visits_for_all_users_randomized'
#compute_history_ordered_visits_for_all_users_randomized()

task_list = [
  compute_hist_timesorted_lines_for_all_users_randomized,
  compute_log_timesorted_lines_for_all_users_randomized,
  compute_mlog_timesorted_lines_for_all_users_randomized,
  compute_history_valid_hids_for_all_users_randomized,
  compute_history_pages_for_all_users_randomized,
  compute_history_visits_for_all_users_randomized,
  compute_mlog_active_times_for_all_users_randomized,
  compute_tab_focus_times_for_all_users_randomized,
  compute_log_with_mlog_active_times_for_all_users_randomized,
]

for fn in shuffled(task_list):
  fn()

task_list = [
  precompute_domains_list,
  precompute_username_to_mturk_id,
]

for fn in shuffled(task_list):
  fn()


#print 'compute_tab_focus_times_for_all_users'
#compute_tab_focus_times_for_all_users()

