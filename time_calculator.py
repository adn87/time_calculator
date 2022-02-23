def add_time(start, duration, dayOfTheWeek=None):
    time, dur = start.split()
    dur_start = dur

    shr, smin = time.split(':')
    dhr, dmin = duration.split(':')

    newMin = int(smin) + int(dmin)
    newHr = int(shr) + int(dhr)

    timeLater = 0
    daysLater = 0

    WEEK = [
        "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday"
    ]

    if newMin > 59:
        newMin -= 60
        newHr += 1

    newShr = newHr

    while newHr > 12:
        newHr -= 12

    while newShr > 11:
        newShr -= 12
        dur = "PM" if dur == "AM" else "AM"
        timeLater += 1

    if timeLater % 2 != 0:
        if dur_start == "PM":
            timeLater += 1
        else:
            timeLater -= 1

    daysLater = timeLater / 2

    newT = f"{newHr}:{str(newMin).zfill(2)} {dur}"

    if dayOfTheWeek:
        dayIndex = WEEK.index(dayOfTheWeek.title())
        newDay = int((dayIndex + daysLater) % 7)
        newT += f", {WEEK[newDay]}"

    if daysLater == 1:
        newT += " (next day)"

    if daysLater > 1:
        newT += f" ({int(daysLater)} days later)"

    return newT