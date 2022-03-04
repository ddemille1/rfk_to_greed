import pyray

class AudioService:

    def __init__ (self, music_path):
        self._music_path = music_path
        self._loop_music = True
        self._music = []

    def _start_audio_device(self):
        pyray.init_audio_device()
        self._music = pyray.load_music_stream(self._music_path)
        self._music.looping = self._loop_music
        pyray.play_music_stream(self._music)

    def _update_music(self):
        pyray.update_music_stream(self._music)

    def _close_audio_device(self):
        pyray.close_audio_device()
