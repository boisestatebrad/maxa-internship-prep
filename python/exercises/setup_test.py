class SetupTest:
    def __init__(self, name: str = "Brad"):
        self.name = name    # This trailing space will be auto-removed

    def greet(self) -> str:
        return f"Hello, {self.name}! Your development environment is working!"

def test_greeting():
    # This tests our SetupTest class
    tester = SetupTest()
    assert tester.greet() == "Hello, Brad! Your development environment is working!"

if __name__ == "__main__":
    test = SetupTest()
    print(test.greet())
