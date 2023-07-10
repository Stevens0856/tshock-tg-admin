import unittest
from services.services import convert_raw_cmd_response_to_message


class TestConvertRawCmdResponseToMessage(unittest.TestCase):
    def test_help(self):
        response: list[str] = [
            'Commands (1/3):', '/user, /login, /logout, /password, /register, /accountinfo, /ban, /broadcast, ',
            '/displaylogs, /group, /itemban, /projban, /tileban, /region, /kick, /mute, ',
            '/overridessc, /savessc, /uploadssc, /tempgroup, /su, /sudo, /userinfo, /annoy, ',
            '/rocket, /firework, /checkupdates, /off, /off-nosave, /reload, ',
            'Type /help 2 for more.']
        lang: str = 'en'

        expected_message = '⬇️ Result:\n' \
                           'Commands (1/3):\n' \
                           '/user, /login, /logout, /password, /register, /accountinfo, /ban, /broadcast, \n' \
                           '/displaylogs, /group, /itemban, /projban, /tileban, /region, /kick, /mute, \n' \
                           '/overridessc, /savessc, /uploadssc, /tempgroup, /su, /sudo, /userinfo, /annoy, \n' \
                           '/rocket, /firework, /checkupdates, /off, /off-nosave, /reload, \n' \
                           'Type /help 2 for more.\n'

        actual_message = convert_raw_cmd_response_to_message(response, lang)

        self.assertEqual(actual_message, expected_message)

    def test_help_2(self):
        response: list[str] = ['Commands (2/3):',
                               '/serverpassword, /version, /whitelist, /give, /item, /butcher, /renamenpc, ',
                               '/maxspawns, /spawnboss, /spawnmob, /spawnrate, /clearangler, /home, /spawn, ',
                               '/tp, /tphere, /tpnpc, /tppos, /pos, /tpallow, /worldmode, /antibuild, /grow, ',
                               '/forcehalloween, /forcexmas, /worldevent, /hardmode, /protectspawn, /save, ',
                               'Type /help 3 for more.']
        lang: str = 'en'

        expected_message = '⬇️ Result:\n' \
                           'Commands (2/3):\n' \
                           '/serverpassword, /version, /whitelist, /give, /item, /butcher, /renamenpc, \n' \
                           '/maxspawns, /spawnboss, /spawnmob, /spawnrate, /clearangler, /home, /spawn, \n' \
                           '/tp, /tphere, /tpnpc, /tppos, /pos, /tpallow, /worldmode, /antibuild, /grow, \n' \
                           '/forcehalloween, /forcexmas, /worldevent, /hardmode, /protectspawn, /save, \n' \
                           'Type /help 3 for more.\n'

        actual_message = convert_raw_cmd_response_to_message(response, lang)

        self.assertEqual(actual_message, expected_message)

    def test_group_help(self):
        response: list[str] = ['Group Sub-Commands (1/3):',
                               'add <name> <permissions...> - Adds a new group.',
                               'addperm <group> <permissions...> - Adds permissions to a group.',
                               "color <group> <rrr,ggg,bbb> - Changes a group's chat color.",
                               "rename <group> <new name> - Changes a group's name.",
                               'Type /group help 2 for more sub-commands.']
        lang: str = 'en'

        expected_message = "⬇️ Result:\n" \
                           "Group Sub-Commands (1/3):\n" \
                           "add &lt;name&gt; &lt;permissions...&gt; - Adds a new group.\n" \
                           "addperm &lt;group&gt; &lt;permissions...&gt; - Adds permissions to a group.\n" \
                           "color &lt;group&gt; &lt;rrr,ggg,bbb&gt; - Changes a group's chat color.\n" \
                           "rename &lt;group&gt; &lt;new name&gt; - Changes a group's name.\n" \
                           "Type /group help 2 for more sub-commands.\n"

        actual_message = convert_raw_cmd_response_to_message(response, lang)

        self.assertEqual(actual_message, expected_message)


if __name__ == '__main__':
    unittest.main()
