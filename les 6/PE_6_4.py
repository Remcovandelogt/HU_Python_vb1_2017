studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]
def gemiddelde_per_student():
    print(sum(studentencijfers[0])/3)
    print(sum(studentencijfers[1])/3)
    print(sum(studentencijfers[2])/3)
    print(sum(studentencijfers[3])/3)
gemiddelde_per_student()

def gemiddelde_van_alle_studenten():
   cijfersopgeteld=sum(sum(studentencijfers[0]),sum(studentencijfers[1]),sum(studentencijfers[2]),sum(studentencijfers[3]))
   print(cijfersopgeteld)
gemiddelde_van_alle_studenten()