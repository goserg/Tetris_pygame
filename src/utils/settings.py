# game
name = "Tetris"
version = "0.3-dev-alpha"
fps_cap = 60
speed = 48  # 1 - maximum
auto_shift = 6
delayed_auto_shift = 16
flat = True
grid = False

# window
win_h = 500
win_w = 400
game_h = 500
game_w = 300

scale = 1.5
cell_size = 20

# colors
grid_color = (50, 50, 50)
standard_color = {"Background": (0, 0, 0),
                  "TypeI": (0, 240, 240),
                  "TypeJ": (0, 0, 240),
                  "TypeL": (240, 160, 0),
                  "TypeO": (240, 240, 0),
                  "TypeS": (0, 240, 0),
                  "TypeT": (160, 0, 240),
                  "TypeZ": (240, 0, 0),
                  "Shade": (20, 20, 20),
                  "Border": (100, 100, 100),
                  "Grid": (50, 50, 50)}

palette_1 = {"Background": (0, 0, 0),
             "TypeI": (248, 118, 109),
             "TypeJ": (196, 154, 0),
             "TypeL": (83, 180, 0),
             "TypeO": (0, 192, 148),
             "TypeS": (0, 182, 235),
             "TypeT": (165, 138, 255),
             "TypeZ": (251, 97, 215),
             "Shade": (20, 20, 20),
             "Border": (150, 150, 150),
             "Grid": (20, 20, 20)}

palette_2 = {"Background": (0, 0, 0),
             "TypeI": (58, 137, 201),
             "TypeJ": (153, 199, 236),
             "TypeL": (230, 245, 254),
             "TypeO": (255, 250, 210),
             "TypeS": (255, 227, 170),
             "TypeT": (245, 162, 117),
             "TypeZ": (210, 77, 62),
             "Shade": (20, 20, 20),
             "Border": (150, 150, 150),
             "Grid": (20, 20, 20)}

palette_3 = {"Background": (0, 0, 0),
             "TypeI": (102, 194, 165),
             "TypeJ": (252, 141, 98),
             "TypeL": (141, 160, 203),
             "TypeO": (231, 138, 195),
             "TypeS": (166, 216, 84),
             "TypeT": (255, 217, 47),
             "TypeZ": (229, 196, 148),
             "Shade": (20, 20, 20),
             "Border": (179, 179, 179),
             "Grid": (0, 0, 0)}

palette_4 = {"Background": (0, 0, 0),
             "TypeI": (27, 158, 119),
             "TypeJ": (217, 95, 2),
             "TypeL": (117, 112, 179),
             "TypeO": (231, 41, 138),
             "TypeS": (102, 166, 30),
             "TypeT": (230, 171, 2),
             "TypeZ": (166, 118, 29),
             "Shade": (20, 20, 20),
             "Border": (102, 102, 102),
             "Grid": (20, 20, 20)}

colors = palette_3
