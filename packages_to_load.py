def which_packages_to_load(truck_space: int, packages: list, reserve: int = 30):
    target_space = truck_space - reserve
    if target_space >= 0 and len(packages) > 1:
        best_order = []
        packages.sort()
        left_index = 0
        right_index = len(packages) - 1
        while left_index < right_index:
            current_packages = [packages[left_index], packages[right_index]]
            if sum(current_packages) == target_space:
                return current_packages
            elif sum(current_packages) < target_space:
                if sum(current_packages) > sum(best_order):
                    best_order = current_packages
                left_index += 1
            else:
                right_index -= 1
        return best_order
    return []
