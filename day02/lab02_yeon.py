## Fill in the following methods for the class 'Clock'
class Clock:
    def __init__(self, hour, minutes):
        self.minutes = minutes
        self.hour = hour

    ## Print the time
    def __str__(self):
        return f"The time is {self.hour}:{self.minutes}."

    ## Add time
    ## Don't return anything
    def __add__(self, minutes):
        self.minutes += minutes
        if self.minutes >= 60:
            self.minutes -= 60
            self.hour += 1
        self.minutes = "%02d" % (self.minutes)


    ## Subtract time
    ## Don't return anything
    def __sub__(self, minutes):
        self.minutes -= minutes
        if self.minutes < 0:
            self.minutes +=60
            self.hour -= 1
        self.minutes = "%02d" % (self.minutes)


    ## Are two times equal?
    def __eq__(self, other):
        return self.hour == other.hour and self.minutes == other.minutes

    ## Are two times not equal?
    def __ne__(self, other):
        return self.hour != other.hour or self.minutes != other.minutes


#instantiate  clocks
clock1 = Clock(10, 15)
clock2 = Clock(1, 45)
print(clock1)

clock1 + 45
print(clock1)
clock2 - 15
print(clock2)

print(clock1 == clock2)
print(clock1 != clock2)
