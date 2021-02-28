import unittest
from exam_16aug.project.hardware.hardware import Hardware, UnsuccessfulInstallException
from exam_16aug.project.hardware.heavy_hardware import HeavyHardware
from exam_16aug.project.hardware.power_hardware import PowerHardware
from exam_16aug.project.software.express_software import ExpressSoftware


class HardwareTests(unittest.TestCase):
    def test_hardwareInit_whenInit_shouldRaise(self):
        with self.assertRaises(TypeError) as context:
            Hardware('test', 'Heavy', 100, 100)

        self.assertIsNotNone(context.exception)

    def test_hardwareHeavyInit_shouldAssignAttributes(self):
        heavy_hardware = HeavyHardware('test', 100, 100)

        self.assertEqual('test', heavy_hardware.name)
        self.assertEqual('Heavy', heavy_hardware.type)
        self.assertEqual(200, heavy_hardware.capacity)
        self.assertEqual(75, heavy_hardware.memory)
        self.assertListEqual([], heavy_hardware.software_components)

    def test_hardwarePowerInit_shouldAssignAttributes(self):
        power_hardware = PowerHardware('test', 100, 100)

        self.assertEqual('test', power_hardware.name)
        self.assertEqual('Power', power_hardware.type)
        self.assertEqual(25, power_hardware.capacity)
        self.assertEqual(175, power_hardware.memory)
        self.assertListEqual([], power_hardware.software_components)

    def test_hardwareInstall_whenEnoughCapacityAndMemory_shouldAppendSoftwareToComponents(self):
        software = ExpressSoftware('test software', 100, 20)
        heavy_hardware = HeavyHardware('test', 100, 100)

        heavy_hardware.install(software)

        self.assertListEqual([software], heavy_hardware.software_components)

    def test_hardwareInstall_whenNotEnoughCapacityOrMemory_shouldRaise(self):
        software = ExpressSoftware('test software', 100, 100)
        heavy_hardware = HeavyHardware('test', 100, 100)

        with self.assertRaises(UnsuccessfulInstallException) as context:
            heavy_hardware.install(software)

        self.assertIsNotNone(context.exception)
        self.assertEqual(str(context.exception), 'Software cannot be installed')

    def test_hardwareUninstall_whenValidSoftware_shouldRemoveFromComponents(self):
        software = ExpressSoftware('test software', 100, 20)
        heavy_hardware = HeavyHardware('test', 100, 100)
        heavy_hardware.install(software)

        heavy_hardware.uninstall(software)

        self.assertListEqual([], heavy_hardware.software_components)

    def test_hardwareUninstall_whenInvalidSoftware_shouldRaise(self):
        software = ExpressSoftware('test software', 100, 20)
        heavy_hardware = HeavyHardware('test', 100, 100)

        heavy_hardware.uninstall(software)

        self.assertEqual([], heavy_hardware.software_components)


if __name__ == '__main__':
    unittest.main()
