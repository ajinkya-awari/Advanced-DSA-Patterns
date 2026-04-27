# Music Playlist (Circular Linked List)

### Architectural Overview
The **Music Playlist** is implemented using a **Singly Circular Linked List** to model a looping playback system.

**Core Design Decisions:**
1.  **Circular Linkage:** The `tail.next` always points to `head`, enabling an infinite loop of playback in $O(1)$ transition time.
2.  **Tail Pointer Optimization:** Maintains a `tail` reference to allow $O(1)$ song additions at the end of the list.
3.  **State Persistence:** The `_current` pointer tracks the active song, facilitating seamless navigation across different playback sessions.
4.  **Robust Deletion:** Correctly repairs circular links when head, tail, or middle nodes are removed.

### Complexity Analysis
- **Add Song:** $O(1)$
- **Next Song:** $O(1)$
- **Remove Song:** $O(N)$ (requires linear search)
- **Space:** $O(N)$
