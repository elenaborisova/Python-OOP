import unittest

from exam_19dec.project.factory.paint_factory import PaintFactory


class PaintFactoryTests(unittest.TestCase):
    def test_init_shouldInitializeValues(self):
        paint_factory = PaintFactory('test', 100)

        self.assertEqual('test', paint_factory.name)
        self.assertEqual(100, paint_factory.capacity)
        self.assertEqual({}, paint_factory.ingredients)
        self.assertEqual(['white', 'yellow', 'blue', 'green', 'red'], paint_factory.valid_ingredients)

    def test_productsProperty_shouldReturnIngredients(self):
        paint_factory = PaintFactory('test', 100)
        paint_factory.add_ingredient('white', 50)
        paint_factory.add_ingredient('yellow', 20)

        self.assertEqual({'white': 50, 'yellow': 20}, paint_factory.products)

    def test_addIngredient_whenIsValidAndEnoughCapacity_shouldAddIt(self):
        paint_factory = PaintFactory('test', 100)

        paint_factory.add_ingredient('white', 50)

        self.assertEqual({'white': 50}, paint_factory.ingredients)

    def test_addIngredient_whenNotValid_shouldRaise(self):
        paint_factory = PaintFactory('test', 100)

        with self.assertRaises(TypeError) as context:
            paint_factory.add_ingredient('pink', 50)

        self.assertIsNotNone(context.exception)

    def test_addIngredient_whenNotEnoughCapacity_shouldRaise(self):
        paint_factory = PaintFactory('test', 100)

        with self.assertRaises(ValueError) as context:
            paint_factory.add_ingredient('white', 150)

        self.assertIsNotNone(context.exception)

    def test_removeIngredient_whenValid_shouldReduceQuantity(self):
        paint_factory = PaintFactory('test', 100)
        paint_factory.add_ingredient('white', 50)

        paint_factory.remove_ingredient('white', 25)

        self.assertEqual({'white': 25}, paint_factory.ingredients)

    def test_removeIngredient_whenNotInIngredients_shouldRaise(self):
        paint_factory = PaintFactory('test', 100)

        with self.assertRaises(KeyError) as context:
            paint_factory.remove_ingredient('white', 150)

        self.assertIsNotNone(context.exception)

    def test_removeIngredient_whenQuantityMoreThanAvailable(self):
        paint_factory = PaintFactory('test', 100)
        paint_factory.add_ingredient('white', 50)

        with self.assertRaises(ValueError) as context:
            paint_factory.remove_ingredient('white', 60)

        self.assertIsNotNone(context.exception)

