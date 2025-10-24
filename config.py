display_mode = (1920,1080)
monitor_number = 0
pixels_per_deg = 36
foreground_color = (255, 255, 255)
background_color = (0, 0, 0)

prompt_for_eye = True
default_eye = 'RE'

data_monitoring = True
data_monitoring_folder = '/home/rjonnal/code/looky/testing'
data_monitoring_extensions = ['.unp']
auto_advance = True # automatically advance the script index when new data is detected

target_line_width = 5
target_radius = 1.0 #deg
target_step = 0.5
target_small_step = 0.125

target_type = 'ABC' # 'star' or 'bullseye' or 'ABC' for now
inset_type = 'checkerboard' # 'grating' or 'deadleaves' or 'checkerboard'

color_increment = 5
colors = [foreground_color,background_color]

origin_filename = 'origin.txt'
log_folder = 'logs'
data_folder = 'data'

text_color = (127,127,127)
text_font_size = 24
text_font = 'serif'

origin_color = (255,0,0)
origin_size_px = 50
origin_line_width = 2
origin_step_px = 5
origin_small_step_px = 1

inset_background_color = (127, 127, 127)

inset_width_deg = display_mode[0]/pixels_per_deg
inset_height_deg = display_mode[1]/pixels_per_deg/2.0
inset_x_deg = 0.0
inset_y_deg = inset_height_deg/2.0

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
grating_orientation = 'horizontal'

checkerboard_frequency = 5
checkerboard_n_cols = inset_width_deg
checkerboard_n_rows = inset_height_deg
checkerboard_bright = (255,255,255)
checkerboard_dark = (0,0,0)

# seconds to wait after moving the target before writing its location tot he log
logging_interval = 1

