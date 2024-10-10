import unittest
from emulator import Emulator, clear, console

class TestEmulator(unittest.TestCase):

    def setUp(self):
        self.emulator = Emulator()

    def tearDown(self):
        clear()

    def test_help_command(self):
        self.emulator.read_command("help")
        self.assertIn("List of commands:", console.text_list)

    def test_about_command(self):
        self.emulator.read_command("about")
        self.assertIn("This Shell Emulator has been created by Soup-o-Stat", console.text_list)

    def test_clear_command(self):
        console.text_list.append("Test message")
        self.emulator.read_command("clear")
        self.assertEqual(console.text_list, [])

    def test_ls_command(self):
        self.emulator.read_command("ls")
        self.assertNotEqual(len(console.text_list), 0)

    def test_cd_command(self):
        start_dir = 'C:/Users/3bepu/OneDrive/Документы'
        self.emulator.read_command(f"cd {start_dir}")
        self.assertIn(f"Changed to {start_dir}", console.text_list)

    def test_uniq_command_invalid_params(self):
        self.emulator.read_command("uniq")
        self.assertIn("Error! Invalid number of parameters", console.text_list)

    def test_tree_command_no_option(self):
        self.emulator.read_command("tree")
        self.assertIn("Error! No options", console.text_list)

    def test_error_command(self):
        self.emulator.read_command("main furry228 cpp")
        self.assertIn("Command main furry228 cpp does not exist. Type 'help' for command list", console.text_list)

if __name__ == "__main__":
    unittest.main()
