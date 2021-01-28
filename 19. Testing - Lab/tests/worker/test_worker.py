import unittest
from test_worker_01.worker import Worker


class WorkerTests(unittest.TestCase):
    def test_workerInit_whenCorrectNameSalaryAndEnergy_shouldBeInitialized(self):
        name = 'Worker name'
        salary = 123
        energy = 5
        worker = Worker(name, salary, energy)

        self.assertEqual(name, worker.name)
        self.assertEqual(salary, worker.salary)
        self.assertEqual(energy, worker.energy)
        self.assertEqual(0, worker.money)

    def test_workerRest_shouldIncrementEnergy(self):
        name = 'Worker name'
        salary = 123
        energy = 5
        worker = Worker(name, salary, energy)

        worker.rest()
        self.assertEqual(energy + 1, worker.energy)

    def test_workerWork_whenEnergyIsNegativeOrZero_shouldRaiseException(self):
        name = 'Worker name'
        salary = 123
        energy = 0
        worker = Worker(name, salary, energy)

        with self.assertRaises(Exception) as context:
            worker.work()

        self.assertIsNotNone(context.exception)

        # self.assertRaises(Exception, worker.work())

    def test_workerWork_shouldIncreaseMoneyBySalary(self):
        name = 'Worker name'
        salary = 123
        energy = 5
        worker = Worker(name, salary, energy)

        worker.work()
        self.assertEqual(salary, worker.money)
        worker.work()
        self.assertEqual(salary * 2, worker.money)

    def test_workerWork_shouldDecreaseEnergy(self):
        name = 'Worker name'
        salary = 123
        energy = 5
        worker = Worker(name, salary, energy)

        worker.work()
        self.assertEqual(energy - 1, worker.energy)

    def test_workerGetInfo_shouldReturnCorrectString(self):
        name = 'Worker name'
        salary = 123
        energy = 5
        worker = Worker(name, salary, energy)

        expected = f'{name} has saved 0 money.'
        actual = worker.get_info()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()