import codewars_test as test
from solution import is_today
from datetime import datetime

@test.describe("Example")
def test_group():
    @test.it("test case")
    def test_case():
        test.assert_equals(is_today(datetime(2020, 10, 1, 1, 1, 1, 1)), False)
        test.assert_equals(is_today(datetime(2080, 10, 1, 1, 1, 1, 1)), False)
        test.assert_equals(is_today(datetime.today()), True)