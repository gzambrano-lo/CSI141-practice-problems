# '''4. Use nested for loops to create a simple multiplication table for numbers 1 through 5. 
# Format your output so that each row corresponds to multiplying by a specific number.''' 

for row in range(1, 6): 
    for col in range(1, 6):
        print(row * col, end='\t')
    print()    
