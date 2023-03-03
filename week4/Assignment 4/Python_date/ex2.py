from datetime import datetime, timedelta

bugin = datetime.now()
keshe = bugin - timedelta(days = 1)
erten = bugin + timedelta(days = 1)

print(keshe)
print(bugin)
print(erten)