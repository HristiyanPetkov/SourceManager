import nox


@nox.session(python=["3.10"])
def tests(session):
    session.install("-r", "requirements.txt")
    session.run("coverage", "run", "-m", "pytest", "tests/", external=True)
    session.run("coverage", "report", "-m", external=True)
