import csv

# Read input file
with open('input.txt', 'r') as f:
    lines = f.readlines()
    demands = [int(x.strip()) for x in lines[0].split(':')[1].split(',')]
    capacities = [int(x.strip()) for x in lines[1].split(':')[1].split(',')]

# Compute matching allocation
results = []
for i, (demand, capacity) in enumerate(zip(demands, capacities)):
    allocation = min(demand, capacity)
    utilization = (allocation / capacity * 100) if capacity > 0 else 0
    results.append({
        'index': i + 1,
        'demand': demand,
        'capacity': capacity,
        'allocation': allocation,
        'utilization_percent': round(utilization, 2)
    })

# Export to CSV
with open('output.csv', 'w', newline='') as csvfile:
    fieldnames = ['index', 'demand', 'capacity', 'allocation', 'utilization_percent']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in results:
        writer.writerow(row)

print('Demand-capacity matching completed. Results exported to output.csv')
