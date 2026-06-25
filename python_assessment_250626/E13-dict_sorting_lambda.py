employees = [{"name": "A", "salary": 50}, {"name": "B", "salary": 70}, {"name": "C", "salary": 60}] 

#Expected Output: [{'name': 'B', 'salary': 70}, {'name': 'C', 'salary': 60}, {'name': 'A', 'salary': 50}]


res=[]

res = sorted(employees,key = lambda x:x["salary"],reverse=True)
print(res)


           