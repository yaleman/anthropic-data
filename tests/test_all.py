from anthropic_data import Memories, Conversations, Users, Projects


def test_projects():
    projects = Projects.load("tests/data/projects.json")
    assert len(projects.root) == 1
    assert projects.root[0].name == "How to use Claude"


def test_users():
    users = Users.load("tests/data/users.json")
    assert len(users.root) == 1
    assert users.root[0].full_name == "test_user_1"
    assert users.root[0].email_address == "test_user_1@example.com"


def test_memories():
    memories = Memories.load("tests/data/memories.json")
    assert len(memories.root) == 1
    assert str(memories.root[0].account_uuid) == "a55a05c0-c560-4854-b7b3-f939c32e2078"
    assert "This is some nonsense" in memories.root[0].conversations_memory

    assert memories.root[0].try_find_user("tests/data/users.json") is not None


def test_conversations():
    conversations = Conversations.load("tests/data/conversations.json")
    assert len(conversations.root) > 0
