# Chat Application (Message Queue)

### Architectural Overview
The **Chat Application** is implemented using a **Message Broker** pattern centered around a **FIFO Message Queue** to simulate asynchronous communication.

**Core Design Decisions:**
1.  **Centralized Broker:** Decouples senders and recipients by using a global dispatch queue for all incoming traffic.
2.  **Private User Inboxes:** Each participant maintains a local queue, ensuring that messages are buffered and retrievable only by the intended recipient.
3.  **FIFO Guarantee:** Utilizes `collections.deque` for both global and local queues to maintain strict chronological order of delivery.
4.  **O(1) Throughput:** All message enqueuing and dequeuing operations occur in constant time, allowing the system to scale efficiently with message volume.

### Complexity Analysis
- **Enqueue Message:** $O(1)$
- **Process/Dispatch:** $O(N)$ where $N$ is the number of pending messages.
- **Fetch Inbox:** $O(M)$ where $M$ is the number of messages in the user's inbox.
- **Space:** $O(Total\_Messages)$
