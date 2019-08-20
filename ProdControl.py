import ProdPump
import ProdSensor
import ProdData
import ProdLED
import ProdScheduler
import Testing_more_graphs
import csv


class Control:

    def __init__(self, min_moisture, max_moisture, min_light, max_light,
                 water_time, override_time):
        self.Pump_Control = ProdPump.Pump_Control()
        self.Sensor_Control = ProdSensor.Sensor_Control()
        self.Data = ProdData.Data_Handling()
        self.LED = ProdLED.LED_Control()
        self.Graph = Testing_more_graphs.Graph_Plotter()

        self.InternalData = []
        self.graph_data = [min_moisture, max_moisture, min_light, max_light]

        self.min_moisture = min_moisture
        self.water_time = water_time
        self.override_time = override_time

        self.Schedule = ProdScheduler.Scheduler()

    def Checkup(self):
        """
        Collect Diagnostics and current state of other objects.
        Write diagnostic data to Database.
        """
        # [Sensor, Pump]
        #  Sensor -> (Moisture_Level, Tank_Level, Light_Level)
        #  Pump -> Pumping State

        data = []

        data.append((self.Sensor_Control.moisture_check(),
                     self.Sensor_Control.float_switch(),
                     self.Sensor_Control.light_check(),
                     self.Sensor_Control.manual_override()))

        data.append(self.Pump_Control.State)

        self.InternalData = data

    def UpdateSchedule(self):
        """
        Update the schedule based on what is already scheduled,
        state of other objects and collected Diagnostics
        """

        # Schedule Pump if not currently scheduled and moisture is too low
        if not self.Schedule.isScheduled(self.Pump_Control.start_pump,
                                         self.Pump_Control.stop_pump):

            if self.InternalData[0][3]:
                self.Schedule.add(self.Pump_Control.start_pump,
                                  None, (0, 0, 0))
                self.Schedule.add(self.Pump_Control.stop_pump,
                                  None, (0, 0, self.override_time))

            if self.InternalData[0][0] < self.min_moisture:
                self.Schedule.add(self.Pump_Control.start_pump,
                                  None, (0, 0, 0))
            elif (self.InternalData[0][0] > self.min_moisture
                    and self.InternalData[1]):
                self.Schedule.add(self.Pump_Control.stop_pump,
                                  None, (0, 0, self.water_time))

            else:
                pass

        # Schedule LED Update if not currently scheduled
        if not self.Schedule.isScheduled(self.LED.green_LED, self.LED.red_LED):
            if self.InternalData[0][1]:
                self.Schedule.add(self.LED.green_LED, None, (0, 0, 5))

            else:
                self.Schedule.add(self.LED.red_LED, None, (0, 0, 0.25))

        # Schedule Data write if not currently scheduled
        if not self.Schedule.isScheduled(self.Data.write_to_csv):
            self.Schedule.add(self.Data.write_to_csv,
                              self.InternalData, (0, 0, 0.5))

        # Schedule Graph to show if not currently scheduled
        if not self.Schedule.isScheduled(self.Graph.show_graph):
            self.Schedule.add(self.Graph.show_graph,
                              (self.InternalData[:3], self.graph_data),
                              (0, 0, 0.5))

    def ExecuteNextTask(self):
        """
        Encapsulated way to execute next task without
        needing to go through control
        to scheduler to execute.
        """

        task = self.Schedule.nextTask()

        if task is None:
            pass

        else:
            if task[1] is not None:
                task[0](task[1])
            else:
                task[0]()


if __name__ == "__main__":
    while True:
        x = input("Which config file do you want to use? (1, 2)\n>>> ")
        if x in ["1", "2"]:
            if x == "1":
                x = "./config_file.txt"
            else:
                x = "./config_file_2.txt"
            break
        else:
            print("Invalid input. Try again.\n\n")
    with open(x, "r") as ConfigFile:
        settings = list(csv.reader(ConfigFile, delimiter=","))[0]
        settings = tuple(map(lambda string: int(string), settings))
        MainController = Control(*settings)
    
    try:
        while True:
            MainController.Checkup()
            MainController.UpdateSchedule()
            MainController.ExecuteNextTask()
    except KeyboardInterrupt:
        pass