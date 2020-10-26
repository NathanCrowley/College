'''Student Name: Nathan Crowley
Student Number: 118429092'''
from Year2_semester2.Operating_Systems_Sem2.Assignement3.memory import *
def Next_Fit():
    x = 0
    num_Process = len(free_memory)-1
    while x <= num_Process:
        next_process = free_memory[x]  # Process1: Size 62 KB.
        node = main_memory.first.next  # node holding Block0(Number of Pages 2. BlockState 0 .Block Size 8KB. *REMAINING 8KB*)->>>>
        while node.next:
            if node.element.state == 0 and node.element.Bsize >= next_process.sizeKB:
                node.element.state = 1
                node.element.remainKB -= next_process.sizeKB
                node.element.status = "Holding PROCESS {}: Size {}KB".format(next_process.id,next_process.sizeKB)
                node.element.remainKB -= next_process.sizeKB
                break
            node = node.next
        x += 1
    print(main_memory)

Next_Fit()