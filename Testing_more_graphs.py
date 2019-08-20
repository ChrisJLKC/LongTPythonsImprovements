from datetime import datetime
from matplotlib import pyplot
'''
Colour list
Core Blue:   #9BD5E3
Core Purple: #805c8c
Orange:      #EB845C
Yellow:      #FCC66E
Green:       #8FCB22
Dark Blue:   #565D95
Dark Purple: #695267
'''


class Graph_Plotter:

    def __init__(self):
        pyplot.ion()
        self.x_time = []
        self.y_moisture, self.y_light, self.y_pump_status = [], [], []
        self.y_min_moisture, self.y_max_moisture = [], []
        self.y_min_light, self.y_max_light = [], []
        self.figure = pyplot.figure()
        mng = pyplot.get_current_fig_manager()
        mng.resize(*mng.window.maxsize())

        # Set the list of colours - Easier to understand
        self.Core_Blue = "#9BD5E3"
        self.Core_Purple = "#805c8c"
        self.Orange = "#EB845C"
        self.Yellow = "#FCC66E"
        self.Green = "#8FCB22"
        self.Dark_Blue = "#565D95"
        self.Dark_Purple = "#695267"
        self.Other_Blue = "#61b5ca"
        self.Other_Yellow = "#e3c390"
        self.Other_Dark_Purple = "#2f387c"

    def show_graph(self, input_data):
        sensordata = (input_data[0][0][0], input_data[0][0][2],
                      input_data[0][0][1])
        self.data_to_plot = [datetime.now(), *sensordata, input_data[0][1]]

        self.x_time.append(datetime.now())

        self.y_moisture.append(self.data_to_plot[1])

        self.y_min_moisture.append(input_data[1][0])
        self.y_max_moisture.append(input_data[1][1])
        self.y_min_light.append(input_data[1][2])
        self.y_max_light.append(input_data[1][3])

        self.y_light.append(self.data_to_plot[2])

        self.y_pump_status.append(self.data_to_plot[4] * 550)

        axMoisture = pyplot.subplot(211)  # nrows, ncols, index

        pyplot.plot(self.x_time, self.y_min_moisture,
                    color=self.Other_Dark_Purple)

        pyplot.plot(self.x_time, self.y_max_moisture,
                    color=self.Other_Dark_Purple)

        pyplot.plot(self.x_time, self.y_moisture,
                    color=self.Dark_Blue, linewidth=1)

        pyplot.plot(self.x_time, self.y_pump_status, marker="o",
                    color=self.Core_Purple,
                    linestyle="dashed", markersize=2)

        pyplot.title("Moisture", fontsize=16, fontweight=0,
                     color=self.Dark_Purple, loc='left')
        axMoisture.patch.set_facecolor(self.Core_Blue)

        # Makes the labels invisible
        pyplot.setp(axMoisture.get_xticklabels(), visible=False)

        axLight = pyplot.subplot(212)  # nrows, ncols, index

        pyplot.plot(self.x_time, self.y_min_light,
                    color=self.Other_Yellow)

        pyplot.plot(self.x_time, self.y_max_light,
                    color=self.Other_Yellow)

        pyplot.plot(self.x_time, self.y_light,
                    color=self.Yellow)

        pyplot.title("Light", fontsize=16, fontweight=0,
                     color=self.Dark_Purple, loc='left')

        # Sets BG for window
        self.figure.patch.set_facecolor(self.Other_Blue)

        axLight.patch.set_facecolor(self.Core_Purple)
        self.figure.canvas.draw()
