from datetime import datetime, timezone, timedelta
tz=timezone(timedelta(hours=7))
runtime=datetime.now(tz=tz)
print(runtime.strftime("%c"))