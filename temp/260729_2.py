def ordered_difference_sets(set1, set2):
    set1_diff = set1.difference(set2)
    set2_diff = set2.difference(set1)
    if len(set1_diff) <= len(set2_diff):
        return set1_diff, set2_diff
    else:
        return set2_diff, set1_diff

# 예시 실행
result = ordered_difference_sets({1, 2, 3, 4}, {3, 4, 5, 6})
print("결과:", result)  # 출력: ({1, 2}, {5, 6})

result = ordered_difference_sets({1, 2, 3, 4}, {1, 2, 3})
print("결과:", result)  # 출력: (set(), {4})
