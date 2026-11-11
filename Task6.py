def total_sum(lst):
   total = 0
   for x in lst:
       total = x + total
   return total

print(total_sum([1, 2, 3, 4])) # The output should be 10


#the error was that total=0 was being ran inside the the loop so the running total goes back to 0 on every pass. to fix this issue I moved the total = 0 outside of the loop so that it only runs once and keeps a running total