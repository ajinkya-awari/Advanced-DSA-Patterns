import pytest
from task_scheduler import TaskScheduler

def test_scheduling_logic():
    scheduler = TaskScheduler(cooldown=2)
    scheduler.add_task("TaskA", 10)
    scheduler.add_task("TaskB", 5)
    
    assert scheduler.execute_next() == "TaskA"
    assert scheduler.execute_next() == "TaskB"
    # Both in cooldown. Time is 2. TaskA available at 0+2+1=3.
    assert scheduler.execute_next() is None # Time becomes 3
    assert scheduler.execute_next() == "TaskA"
