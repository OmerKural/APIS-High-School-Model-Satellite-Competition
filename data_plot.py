# Made by Ömer Kural

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.image as mpimg
import pandas as pd

# PLOT SETTINGS
fig, plots = plt.subplots(3, 4)
fig.canvas.set_window_title('3424 Ground Station')
plt.tight_layout()

sattelite_status = 0

def animate(i):
    # DEFINE THE DATAFRAME
    df = pd.read_csv('sat_data.csv')
    #SATTELITE LOGO
    im = mpimg.imread(r'logo.jpg')
    plots[0, 0].clear()
    plots[0, 0].imshow(im)
    plots[0, 0].axis('off')
    #SATTELITE INFO
    if list(df['sattelite_status'])[-1] == 1:
        sattelite_status = 'WAITING'
    elif list(df['sattelite_status'])[-1] == 2:
        sattelite_status = 'RISING'
    elif list(df['sattelite_status'])[-1] == 3:
        sattelite_status = 'LANDING'
    elif list(df['sattelite_status'])[-1] == 4:
        sattelite_status = 'RESCUE'
    plots[0, 1].clear()
    plots[0, 1].text(
            -0.5, 
            0.3,
            f"""
            TEAM NO: 3424
            PACKAGE NO: {list(df['package_no'])[-1]}
            REAL_TIME: {list(df['real_time'])[-1]}
            SATTELITE STATUS: {sattelite_status}
            """, 
            bbox=dict(
                    boxstyle="round",
                    ec=(1., 0.4, 0.5),
                    fc=(1., 0.8, 0.8),
                )   
            )
    plots[0, 1].axis('off')
    # HEIGHT
    plots[0, 2].clear()
    plots[0, 2].plot(xgen_time(df['height']), df['height'], 'b')
    plots[0, 2].set_title("Height (m)")
    plots[0, 2].set_xlabel('time (seconds)')
    # PRESSURE
    plots[0, 3].clear()
    plots[0, 3].plot(xgen_time(df['pressure']), df['pressure'], 'b')
    plots[0, 3].set_title("Pressure (Pa)")
    plots[0, 3].set_xlabel('time (seconds)')
    # TEMPERATURE
    plots[1, 0].clear()
    plots[1, 0].plot(xgen_time(df['temperature']), df['temperature'], 'b')
    plots[1, 0].set_title("Temperature (°C)")
    plots[1, 0].set_xlabel('time (seconds)')
    # BATTERY VOLTAGE
    plots[1, 1].clear()
    plots[1, 1].plot(xgen_time(df['battery_voltage']), df['battery_voltage'], 'b')
    plots[1, 1].set_title("Battery Voltage (V)")
    plots[1, 1].set_xlabel('time (seconds)')
    # GYRO PITCH
    plots[1, 2].clear()
    plots[1, 2].plot(xgen_time(df['gyro_pitch']), df['gyro_pitch'], 'b')
    plots[1, 2].set_title("Pitch (degree)")
    plots[1, 2].set_xlabel('time (seconds)')
    # GYRO ROLL
    plots[1, 3].clear()
    plots[1, 3].plot(xgen_time(df['gyro_roll']), df['gyro_roll'], 'b')
    plots[1, 3].set_title("Roll (degree)")
    plots[1, 3].set_xlabel('time (seconds)')
    # GYRO YAW
    plots[2, 0].clear()
    plots[2, 0].plot(xgen_time(df['gyro_yaw']), df['gyro_yaw'], 'b')
    plots[2, 0].set_title("Yaw (degree)")
    plots[2, 0].set_xlabel('time (seconds)')
    # GPS LONGITUDE
    plots[2, 1].clear()
    plots[2, 1].plot(xgen_time(df['gps_longitude']), df['gps_longitude'], 'b')
    plots[2, 1].set_title("Longitude (degree)")
    plots[2, 1].set_xlabel('time (seconds)')
    # GPS LATITUDE
    plots[2, 2].clear()
    plots[2, 2].plot(xgen_time(df['gps_latitude']), df['gps_latitude'], 'b')
    plots[2, 2].set_title("Latitude (degree)")
    plots[2, 2].set_xlabel('time (seconds)')
    # GPS HEIGHT
    plots[2, 3].clear()
    plots[2, 3].plot(xgen_time(df['gps_height']), df['gps_height'], 'b')
    plots[2, 3].set_title("GPS Height (m)")
    plots[2, 3].set_xlabel('time (seconds)')



def xgen_time(array):
    l=[i+1 for i in range(len(array))]
    return l

ani=animation.FuncAnimation(fig, animate, interval= 1000)
plt.show()