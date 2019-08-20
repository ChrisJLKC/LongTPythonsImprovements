from datetime import datetime, timedelta


class Scheduler:

    def __init__(self):
        self.Schedule = []

    def add(self, func, param, time):
        """
        Schedule a Method
        """
        # Time => (Hours, Minutes, Seconds)
        Delta = timedelta(hours=time[0], minutes=time[1], seconds=time[2])
        self.Schedule.append((func, param, datetime.now() + Delta))
        self.Schedule.sort(key=lambda x: x[2])

    def nextTask(self):
        """
        Return next scheduled task and remove it from schedule.
        """
        if len(self.Schedule) == 0:
            return None
        elif datetime.now() >= self.Schedule[0][2]:
            task = self.Schedule[0][0]
            param = self.Schedule[0][1]
            self.Schedule.pop(0)
            return (task, param)
        else:
            return None

    def isScheduled(self, *tasks):
        """
        Checks if a task is currently scheduled.
        It is meant to help control to schedule tasks
        """
        taskScheduled = [Event[0] for Event in self.Schedule]
        return any([(task in taskScheduled) for task in tasks])
