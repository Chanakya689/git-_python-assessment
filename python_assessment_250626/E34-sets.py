
trial = [1, 2, 3, 4, 5]
paid = [4, 5, 6, 7, 8]

trial_set = set(trial)
paid_set = set(paid)
print(trial_set,paid_set)

upgraded = trial_set & paid_set          # Intersection
leads = trial_set - paid_set             # Difference
unique_status = trial_set ^ paid_set     # Symmetric Difference

print("Upgraded (Both):", upgraded)
print("Leads (Trial only):", leads)
print("Unique Status (Not):",unique_status)
