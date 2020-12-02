""""
    class TestCase:
    def __init__(self):
        self.steps[]
    def add_step(self,step):
    step = input("enter step: ")
    steps.add_step()
    print("steps")
"""


class TestCase:
    def __init__(self):
        self.steps = []

    def add_step(self, step: str):
        self.steps.append(step)
        print("Step added to a test case.")


if __name__ == '__main__':
    test_case = TestCase()
    test_case.add_step("A")
