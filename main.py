def flatten_and_sort(array):
    arr = []
    for item in array:
        arr.append(item)
    return sorted(arr)

print(flatten_and_sort([2, 3, 1, 9, 5, 23, 16, 8]))

class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price
        
    def repair(self):
        if self.condition == 'trashed':
            self.condition = 'repaired'
        else:
            print('Repair not needed.')
            
class AnakinsPod(Podracer):
    def boost(self):
        self.max_speed *= 2

class SebulbasPod(Podracer):
    def flame_jet(self):
        self.condition = 'trashed'



podracer1 = Podracer(max_speed=500, condition='perfect', price=10000)

anakins_pod = AnakinsPod(max_speed=2, condition='perfect', price=20000)
print(anakins_pod.max_speed)

anakins_pod.boost()
print(anakins_pod.max_speed)


sebulbas_pod = SebulbasPod(max_speed=700, condition='perfect', price=25000)

sebulbas_pod.flame_jet()
print(sebulbas_pod.condition)

sebulbas_pod.repair()
print(sebulbas_pod.condition)