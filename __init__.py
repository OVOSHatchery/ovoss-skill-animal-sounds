from os.path import isfile

from ovos_workshop.skills import OVOSSkill
from ovos_workshop.decorators import intent_handler


class AnimalSounds(OVOSSkill):

    def sound_file_path(self, animal):
        if animal[-1] == 's':
            animal = animal[:-1]
        path = f"{self.root_dir}/sounds/{animal}.wav"
        self.log.info(path)
        return path if isfile(path) else None

    @intent_handler('sounds.animal.intent')
    def handle_sounds_animal(self, message):
        animal = message.data.get('animal')
        sound_file = self.sound_file_path(animal)
        if sound_file:
            self.play_audio(sound_file)
        else:
            self.speak_dialog('not.sure', data={'animal': animal})
