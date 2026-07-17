"""
This file contains the elements and wait timeouts of the PC application
"""

# Wait timeouts (seconds)
WAIT_TIMEOUT_2 = 2
WAIT_TIMEOUT_5 = 5
WAIT_TIMEOUT_10 = 10
WAIT_TIMEOUT_15 = 15
WAIT_TIMEOUT_20 = 20

# Login
username_xpath = "//input[@placeholder='Enter username']"
password_xpath = "//input[@placeholder='Enter password']"
login_button_xpath = "//button[text()='Login']"

# Navigation
software_update_link_text = "Software Update"

# Software update wizard
next_button_xpath = "//button[text()='Next']"
image_file_id = "imageFile"
file_preview_id = "filePreview"
file_name_id = "fileName"
next_step1_id = "nextStep1"
device_select_panel_id = "deviceSelectPanelDevices"
select_all_devices_id = "selectAllDevices"
device_count_id = "deviceCount"
next_step2_id = "nextStep2"
scheduler_panel_id = "schedulerPanel"
job_name_id = "jobName"
run_now_id = "runNow"
job_summary_id = "jobSummary"
start_job_id = "startJob"
jobs_tab_id = "tab-jobs"
jobs_table_body_id = "jobsTableBody"