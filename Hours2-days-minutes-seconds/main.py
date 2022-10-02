print("Indtast antallet af timer du vil have konverteret til dage, minutter og sekunder: ")

hours = float(input())

seconds = round((float(hours) * 60 * 60), 6)

minutes = round((float(hours) * 60), 6)

days = round((float(hours) / 24), 6)

print("Super! Det er "+str(days)+" dag(e), " +
      str(minutes)+" minutter og "+str(seconds)+" sekunder :)")
