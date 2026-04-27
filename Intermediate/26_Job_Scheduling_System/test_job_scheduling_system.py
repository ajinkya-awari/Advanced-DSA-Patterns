import pytest
from job_scheduling_system import JobScheduler, Job

@pytest.fixture
def scheduler():
    return JobScheduler()

def test_priority_order(scheduler):
    """Verify that jobs are returned in descending order of priority."""
    scheduler.schedule_job("J1", priority=10, task_name="Low")
    scheduler.schedule_job("J2", priority=100, task_name="Critical")
    scheduler.schedule_job("J3", priority=50, task_name="Mid")
    
    assert scheduler.get_next_job().job_id == "J2"
    assert scheduler.get_next_job().job_id == "J3"
    assert scheduler.get_next_job().job_id == "J1"

def test_fifo_tie_break(scheduler):
    """Verify FIFO behavior for identical priorities."""
    scheduler.schedule_job("First", priority=10, task_name="T1")
    scheduler.schedule_job("Second", priority=10, task_name="T2")
    
    assert scheduler.get_next_job().job_id == "First"
    assert scheduler.get_next_job().job_id == "Second"

def test_lazy_cancellation(scheduler):
    """Verify that cancelled jobs are skipped during extraction."""
    scheduler.schedule_job("J1", 10, "Task 1")
    scheduler.schedule_job("J2", 20, "Task 2")
    
    scheduler.cancel_job("J2")
    assert scheduler.pending_count == 1
    
    # J2 should be skipped, returning J1
    next_job = scheduler.get_next_job()
    assert next_job.job_id == "J1"
    assert scheduler.get_next_job() is None

def test_peek_behavior(scheduler):
    """Verify peek returns top element without mutation."""
    scheduler.schedule_job("J1", 50, "Task")
    assert scheduler.peek_next_job().job_id == "J1"
    assert scheduler.pending_count == 1
    assert scheduler.get_next_job().job_id == "J1"

def test_duplicate_prevention(scheduler):
    """Ensure Job IDs remain unique."""
    scheduler.schedule_job("UNIQUE", 10, "Task")
    with pytest.raises(ValueError, match="already in the queue"):
        scheduler.schedule_job("UNIQUE", 20, "Task")

def test_empty_scheduler(scheduler):
    """Verify robustness with no jobs."""
    assert scheduler.get_next_job() is None
    assert scheduler.peek_next_job() is None
    assert scheduler.pending_count == 0
