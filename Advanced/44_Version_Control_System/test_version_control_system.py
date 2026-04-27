import pytest
from version_control_system import VersionControl

def test_vcs_commit_history():
    vcs = VersionControl()
    vcs.commit("main", "Initial commit", "data v1")
    vcs.commit("main", "Feature A", "data v2")
    
    history = vcs.get_history("main")
    assert history == ["Feature A", "Initial commit"]

def test_vcs_branching():
    vcs = VersionControl()
    vcs.commit("main", "Base", "root")
    
    # Branch off
    vcs._branches["dev"] = vcs._branches["main"]
    vcs.commit("dev", "Dev Work", "dev data")
    
    assert "Dev Work" in vcs.get_history("dev")
    assert "Dev Work" not in vcs.get_history("main")
