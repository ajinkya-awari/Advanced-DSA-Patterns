from typing import Dict, List, Optional, Union
import hashlib

class FSNode:
    """Base node for File System (Tree)."""
    def __init__(self, name: str, is_directory: bool = False):
        self.name: str = name
        self.is_directory: bool = is_directory
        self.children: Dict[str, 'FSNode'] = {}
        self.content: str = ""
        self.hash: Optional[str] = None

class FileSystem:
    """
    Enterprise-grade File System Simulation using Tree structures and Hashing.
    """

    def __init__(self):
        self._root = FSNode("/", is_directory=True)

    def _resolve_path(self, path: str) -> Optional[FSNode]:
        """Navigates the tree to find a node by path."""
        if path == "/": return self._root
        
        parts = path.strip("/").split("/")
        current = self._root
        for part in parts:
            if part not in current.children:
                return None
            current = current.children[part]
        return current

    def mkdir(self, path: str) -> bool:
        """Creates a directory at the given path."""
        parts = path.strip("/").split("/")
        current = self._root
        for part in parts:
            if part not in current.children:
                current.children[part] = FSNode(part, is_directory=True)
            current = current.children[part]
        return True

    def write_file(self, path: str, content: str) -> None:
        """Writes content to a file, generating a hash for integrity."""
        parts = path.strip("/").split("/")
        dir_path = "/".join(parts[:-1])
        file_name = parts[-1]
        
        parent = self._resolve_path("/" + dir_path)
        if not parent or not parent.is_directory:
            raise FileNotFoundError(f"Parent directory not found for {path}")
            
        file_node = FSNode(file_name, is_directory=False)
        file_node.content = content
        file_node.hash = hashlib.md5(content.encode()).hexdigest()
        parent.children[file_name] = file_node

    def read_file(self, path: str) -> str:
        """Reads file content."""
        node = self._resolve_path(path)
        if not node or node.is_directory:
            raise FileNotFoundError(f"File not found: {path}")
        return node.content

    def list_dir(self, path: str) -> List[str]:
        """Lists directory contents."""
        node = self._resolve_path(path)
        if not node or not node.is_directory:
            raise NotADirectoryError(f"Directory not found: {path}")
        return sorted(node.children.keys())

    def get_file_hash(self, path: str) -> Optional[str]:
        node = self._resolve_path(path)
        return node.hash if node else None
