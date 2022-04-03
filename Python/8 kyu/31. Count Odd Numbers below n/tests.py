import codewars_test as test

try:
    from solution import oddCount as odd_count
except ImportError:
    from solution import odd_count

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(odd_count(15),7)
        test.assert_equals(odd_count(15023),7511)