sq = [x**2 for x in range(1, 11)]
print(sq)

days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
weekday_dict = {day: index + 1 for index, day in enumerate(days)}
print(weekday_dict)

tags = ["Django", "FastAPI", "Numpy", "PYTHON", "Pandas", "FASTAPI", "Python", "random"]
tag_set = {tag.lower() for tag in tags}
print(tag_set)


