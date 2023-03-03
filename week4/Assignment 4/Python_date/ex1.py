from datetime import datetime, timedelta

qazir = datetime.now()
buryn = qazir - timedelta(days=5)

print(buryn.strftime("%Y-%m-%d"))
