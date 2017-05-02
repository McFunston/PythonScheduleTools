from enum import Enum
class ScheduleType(Enum):
    ToDo
    Done
    Mixed

class ExcelSchedule():
    Type = ScheduleType()
    