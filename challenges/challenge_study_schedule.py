def study_schedule(permanence_period, target_time):
    if not permanence_period or target_time is None:
        return None

    count = 0
    for tupla in permanence_period:
        first_pos, second_pos = tupla

        if None in (first_pos, second_pos):
            return None

        if isinstance(first_pos, int) and isinstance(second_pos, int):
            if first_pos <= target_time <= second_pos:
                count += 1
        else:
            return None

    return count
