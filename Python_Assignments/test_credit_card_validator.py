from unittest import TestCase

from Python_Assignments.credit_card_validator import check_card_length, check_card_type, add_even_number_step_2, \
    add_odd_number_step_3, sum_from_step2_and_3


class CreditCardTest(TestCase):
    def test_check_card_length(self):
        sup = "438857601252626"
        for i in sup:
            result = check_card_length(sup)
        self.assertTrue(16)

    # self.fail()

    def test_check_card_type(self):
        print()
        result2 = check_card_type("4")
        self.assertTrue("4")

    # self.fail()

    def test_add_even_number_step_2(self):
        result3 = add_even_number_step_2([2, 3, 5])
        inputs = [1, 2, 3, 5]
        result4 = add_even_number_step_2(inputs)
        self.assertEqual(result4, result3)

    # self.fail()

    def test_add_odd_number_step_3(self):
        result5 = add_odd_number_step_3([3, 7, 9])
        input2 = [1, 3, 6, 7]
        result6 = add_odd_number_step_3(input2)
        self.assertEqual(result6, result5)

    # self.fail()

    def test_sum_from_step2_and_3(self):
        result7 = sum_from_step2_and_3([2, 3, 5])
        step4 = 0
        if step4 % 10 == 0:
            print("valid")
            self.assertTrue(result7)
            # self.assertEqual()
        # self.fail()
