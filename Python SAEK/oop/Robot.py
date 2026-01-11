class Robot:
    def __init__(self, steps, length, distance=0, usage=0):
        self.steps = steps
        self.length = length
        self.distance = distance
        self.usage = usage

    def Print(self):
        print("Ποσό βημάτων: ", self.steps)
        print("Μήκος ενός βήματος: ", self.length)
        print("Απόσταση σε μέτρα: ", self.distance)
        print("Κατανάλωση ενέργειας σε Joules: ", self.usage)

    def calculate_distance(self):
        self.distance = self.steps * self.length / 100

    def calculate_usage(self):
        self.usage = self.distance * 10

robot1_steps = int(input('Δώσε βήματα πρώτου ρομπότ :'))
robot1_length = float(input('Δώσε απόσταση που διήνυσε το πρώτο ρομπότ :'))
robot2_steps = int(input('Δώσε βήματα δεύτερου ρομπότ :'))
robot2_length = float(input('Δώσε απόσταση που διήνυσε του δεύτερου ρομπότ :'))

Robo100 = Robot(robot1_steps, robot1_length)
Robo101 = Robot(robot2_steps, robot2_length)

Robo100.calculate_distance()
Robo100.calculate_usage()
Robo101.calculate_distance()
Robo101.calculate_usage()

Robo100.Print()
Robo101.Print()

if Robo100.distance < Robo101.distance:
    print('Το ρομπότ 100 κινήθηκε σε μικρότερη απόσταση ')
else:
    print('Το ρομπότ 101 κινήθηκε σε μικρότερη απόσταση ')
