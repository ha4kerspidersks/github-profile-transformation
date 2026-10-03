import math

# We want to find begin offsets (b_iam, b_data, b_cloud, b_dev, b_sec)
# Orbits:
# IAM: rx=180, ry=90, ang=-15, dur=32
# DATA_AI: rx=195, ry=100, ang=42, dur=38
# CLOUD: rx=185, ry=80, ang=12, dur=34
# DEV: rx=200, ry=95, ang=-52, dur=42
# SEC: rx=135, ry=65, ang=70, dur=22

cx, cy = 262, 290

orbits = [
    ('iam', 180, 90, -15, 32),
    ('data_ai', 195, 100, 42, 38),
    ('cloud', 185, 80, 12, 34),
    ('dev', 200, 95, -52, 42),
    ('sec', 135, 65, 70, 22)
]

def get_pos(rx, ry, angle_deg, dur, begin, t):
    rad = math.radians(angle_deg)
    u = ((t - begin) % dur) / dur
    theta = 2 * math.pi * u
    x0 = rx * math.cos(theta)
    y0 = ry * math.sin(theta)
    x = cx + x0 * math.cos(rad) - y0 * math.sin(rad)
    y = cy + x0 * math.sin(rad) + y0 * math.cos(rad)
    return x, y

# IAM fixed at begin = 0.0
# We want:
# IAM at t=0: right (~440, 240)
# DATA_AI: bottom-left
# CLOUD: top-left
# DEV: top-right
# SEC: bottom-right / inner perimeter

# Grid search best offsets:
best_score = -1
best_begins = None

import itertools

for u_data in [0.2, 0.25, 0.3, 0.35]:
    for u_cloud in [0.4, 0.45, 0.5, 0.55]:
        for u_dev in [0.65, 0.7, 0.75, 0.8]:
            for u_sec in [0.85, 0.9, 0.95, 0.1]:
                b_iam = 0.0
                b_data = -u_data * 38
                b_cloud = -u_cloud * 34
                b_dev = -u_dev * 42
                b_sec = -u_sec * 22
                
                # evaluate min distance over t=0..60s in steps of 2s
                min_dist_overall = 999
                for t in range(0, 60, 2):
                    positions = [
                        get_pos(180, 90, -15, 32, b_iam, t),
                        get_pos(195, 100, 42, 38, b_data, t),
                        get_pos(185, 80, 12, 34, b_cloud, t),
                        get_pos(200, 95, -52, 42, b_dev, t),
                        get_pos(135, 65, 70, 22, b_sec, t)
                    ]
                    for i in range(len(positions)):
                        for j in range(i+1, len(positions)):
                            d = math.hypot(positions[i][0] - positions[j][0], positions[i][1] - positions[j][1])
                            if d < min_dist_overall:
                                min_dist_overall = d
                
                if min_dist_overall > best_score:
                    best_score = min_dist_overall
                    best_begins = (b_iam, b_data, b_cloud, b_dev, b_sec)

print(f"Best min distance between any 2 groups across 60s: {best_score:.1f}px")
print(f"Best begins: IAM={best_begins[0]:.1f}, DATA_AI={best_begins[1]:.1f}, CLOUD={best_begins[2]:.1f}, DEV={best_begins[3]:.1f}, SEC={best_begins[4]:.1f}")
