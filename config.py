display_mode = (1280,720)
monitor_number = 0
pixels_per_deg = 72
background_color = (0, 0, 0)

default_eye = 'RE'

data_monitoring = True
data_monitoring_folder = '/home/rjonnal/code/looky/testing'
data_monitoring_extensions = ['.unp']
auto_advance = True # automatically advance the script index when new data is detected

target_color = (31, 31, 31)
target_line_width = 5
target_radius = 1.0 #deg
target_step = 0.5
target_small_step = 0.125

target_type = 'ABC' # 'star' or 'bullseye' or 'ABC' for now
inset_type = 'checkerboard' # 'grating' or 'deadleaves' or 'checkerboard'

colors = [(127,0,0),
          (0,127,0),
          (127,0,0),
          (255,0,127)]


origin_filename = 'origin.txt'
log_folder = 'logs'
data_folder = 'data'

text_color = (127,191,127)
text_font_size = 32
text_font = 'freemono'

origin_color = (255,0,0)
origin_size_px = 50
origin_line_width = 2
origin_step_px = 5
origin_small_step_px = 1

inset_background_color = (127, 127, 127)

inset_width_deg = 18.0
inset_height_deg = 6.0
inset_x_deg = 0.0
inset_y_deg = 3.0

deadleaves_rad_mean_deg = 0.25
deadleaves_rad_std_deg = 0.2
deadleaves_n_ellipses = int(inset_width_deg*inset_height_deg/deadleaves_rad_mean_deg**2)
deadleaves_alpha = 0.5
deadleaves_gray_range = 255
deadleaves_gray_mean = 127
# The full cycle frequency is half the update frequency.
# In other words, if you want the full cycle to run at 7.5 Hz,
# write 15 Hz here.
deadleaves_frequency = 6
deadleaves_seed = 1234

grating_frequency = 30
grating_interval_deg = 1
grating_cycles_per_second = 5
grating_orientation = 'vertical'

checkerboard_frequency = 5
checkerboard_n_cols = 18
checkerboard_n_rows = 6
checkerboard_bright = (255,255,255)
checkerboard_dark = (0,0,0)

# seconds to wait after moving the target before writing its location tot he log
logging_interval = 1

