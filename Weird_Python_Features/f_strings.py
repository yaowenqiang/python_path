from datetime import datetime
print(f"{(lambda x: x ** 2)(3)}")
print(f"Today is: {(today:=datetime.today()):%Y-%m-%d}, which is {today:%A}")
