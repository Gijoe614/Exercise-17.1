class Time(object):
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def time_to_sec(self):
        hr = self.hour * 60 * 60
        mt = self.minute * 60
        sec = self.second + hr + mt
        print 'The time being converted is ' + '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)
        print '\n'
        return 'The time converted into seconds is %d seconds ' % sec


time = Time()
time.hour = 9
time.minute = 20
time.second = 55

print time.time_to_sec()

# Answer to question:
# I would invoke int_to_time with the time_to_sec method.

