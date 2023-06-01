def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    count = 0
    for first_pos, second_pos in permanence_period:
        if not isinstance(first_pos, int) or not isinstance(second_pos, int):
            return None
        if first_pos <= target_time <= second_pos:
            count += 1

    return count
