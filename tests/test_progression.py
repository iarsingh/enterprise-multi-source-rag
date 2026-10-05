from ragapp.progression import enterprise_rag

def test_enterprise_rag_rbac():
    sources = [{"id": "runbook", "text": "oom kill", "roles": ["sre", "admin"]}]
    hidden = enterprise_rag("oom", sources, role="reader")
    shown = enterprise_rag("oom", sources, role="sre")
    assert hidden["visible"] == 0
    assert shown["visible"] == 1

