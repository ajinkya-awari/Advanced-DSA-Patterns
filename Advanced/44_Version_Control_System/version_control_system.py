from typing import List, Dict, Optional, Set
import hashlib

class Commit:
    """Represents a snapshot in the VCS history."""
    def __init__(self, message: str, data: str, parents: List['Commit']):
        self.message = message
        self.data = data
        self.parents = parents
        self.commit_id = self._calculate_hash()

    def _calculate_hash(self) -> str:
        parent_ids = "".join([p.commit_id for p in self.parents])
        payload = f"{self.message}{self.data}{parent_ids}"
        return hashlib.sha256(payload.encode()).hexdigest()

class VersionControl:
    """
    Advanced VCS simulating Git-like branching and commit DAGs.
    """

    def __init__(self):
        self._commits: Dict[str, Commit] = {}
        self._branches: Dict[str, str] = {"main": ""} # branch_name -> commit_id

    def commit(self, branch_name: str, message: str, data: str) -> str:
        """Creates a new commit on the specified branch."""
        parent_id = self._branches.get(branch_name)
        parents = [self._commits[parent_id]] if parent_id else []
        
        new_commit = Commit(message, data, parents)
        self._commits[new_commit.commit_id] = new_commit
        self._branches[branch_name] = new_commit.commit_id
        return new_commit.commit_id

    def get_history(self, branch_name: str) -> List[str]:
        """Returns linear history messages of a branch."""
        commit_id = self._branches.get(branch_name)
        history = []
        while commit_id:
            c = self._commits[commit_id]
            history.append(c.message)
            commit_id = c.parents[0].commit_id if c.parents else None
        return history
