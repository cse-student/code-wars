import codewars_test as test
from solution import get_age

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(get_age("2 years old"), 2)
        test.assert_equals(get_age("4 years old"), 4)
        test.assert_equals(get_age("5 years old"), 5)
        test.assert_equals(get_age("7 years old"), 7)