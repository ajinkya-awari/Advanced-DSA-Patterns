# Parking Lot Management (Stack)

### Architectural Overview
The **Parking Lot Management System** uses a **Stack (LIFO)** to simulate a single-entry parking corridor.

**Core Design Decisions:**
1.  **LIFO Constraint:** Vehicles closest to the exit (parked last) are retrieved first in $O(1)$ time.
2.  **Obstruction Simulation:** Retrieving a vehicle buried in the stack requires popping others into a temporary buffer, simulating the physical movement of cars in a narrow lane.
3.  **Order Preservation:** After retrieving a target vehicle, all obstructing cars are returned to the stack, maintaining their original relative order.
4.  **Capacity Enforcement:** Strictly manages the number of vehicles to prevent overflow in a finite-space environment.

### Complexity Analysis
- **Park Vehicle:** $O(1)$
- **Retrieve Vehicle:** $O(N)$ (due to possible movement of obstructing vehicles)
- **Space:** $O(N)$ (buffer stack for retrieval)
