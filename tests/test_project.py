from models.project import Project


def test_project_creation():
    project = Project(
        "CLI Tool",
        "Project Management App",
        "2026-07-01"
    )

    assert project.title == "CLI Tool"