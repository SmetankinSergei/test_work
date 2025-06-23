def appearance(intervals: dict[str, list[int]]) -> int:
    lesson_start, lesson_end = intervals["lesson"]
    timeline = []

    for item in ["pupil", "tutor"]:
        for index in range(0, len(intervals[item]), 2):
            in_time = intervals[item][index]
            out_time = intervals[item][index + 1]

            if out_time <= lesson_start or in_time >= lesson_end:
                continue
            in_time = max(in_time, lesson_start)
            out_time = min(out_time, lesson_end)

            timeline.append((in_time, item, +1))
            timeline.append((out_time, item, -1))

    timeline.sort()

    current_pupil = 0
    current_tutor = 0
    last_time = None
    total_time = 0

    for time, who, delta in timeline:
        if current_pupil > 0 and current_tutor > 0 and last_time is not None:
            total_time += time - last_time

        if who == "pupil":
            current_pupil += delta
        elif who == "tutor":
            current_tutor += delta

        last_time = time

    return total_time


tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
                   'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
                   'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
     },
    {'intervals': {'lesson': [1594702800, 1594706400],
                   'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564,
                             1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096,
                             1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500,
                             1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
                   'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
     'answer': 3577
     },
    {'intervals': {'lesson': [1594692000, 1594695600],
                   'pupil': [1594692033, 1594696347],
                   'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     'answer': 3565
     },
]

if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['intervals'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
