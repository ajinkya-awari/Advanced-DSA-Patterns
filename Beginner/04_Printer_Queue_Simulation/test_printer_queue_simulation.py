import pytest
from printer_queue_simulation import PrinterQueue

@pytest.fixture
def printer():
    return PrinterQueue()

def test_add_job(printer):
    """Verify jobs are added to the queue."""
    printer.add_job(1, "Resume.pdf", 2)
    assert printer.pending_count == 1
    assert printer.get_queue_snapshot()[0].job_id == 1

def test_fifo_processing(printer):
    """Verify First-In-First-Out behavior."""
    printer.add_job(1, "Doc1.pdf", 5)
    printer.add_job(2, "Doc2.pdf", 10)
    
    first_processed = printer.process_next_job()
    assert first_processed.job_id == 1
    assert printer.pending_count == 1
    
    second_processed = printer.process_next_job()
    assert second_processed.job_id == 2
    assert printer.pending_count == 0

def test_process_empty_queue(printer):
    """Verify exception handling for empty queue."""
    with pytest.raises(IndexError, match="Printer queue is empty"):
        printer.process_next_job()

def test_invalid_page_count(printer):
    """Verify data validation for job creation."""
    with pytest.raises(ValueError, match="greater than zero"):
        printer.add_job(1, "Bad.pdf", 0)

def test_cancel_job(printer):
    """Verify specific job cancellation."""
    printer.add_job(1, "Doc1.pdf", 1)
    printer.add_job(2, "Doc2.pdf", 1)
    
    assert printer.cancel_job(1) is True
    assert printer.pending_count == 1
    assert printer.get_queue_snapshot()[0].job_id == 2

def test_cancel_non_existent(printer):
    """Verify cancellation logic for missing IDs."""
    printer.add_job(1, "Doc1.pdf", 1)
    assert printer.cancel_job(99) is False
