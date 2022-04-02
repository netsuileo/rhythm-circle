from datetime import datetime, timedelta
from time import sleep
import simpleaudio as sa


hh = sa.WaveObject.from_wave_file('drumkit/CY2525.WAV')
clap = sa.WaveObject.from_wave_file('drumkit/CP.WAV')


RHYTHM = {
    'name': 'rhythm',
    'bpm': 300,
    'rhythm': [
        [clap, clap],
        [clap, None, clap],
        [None, clap, None, clap],
        [clap, clap],
    ]
}
PART_DURATION = 60 / (RHYTHM['bpm'] / len(RHYTHM['rhythm']))


def sleep_until(wake_time):
    while wake_time > datetime.now():
        sleep(0.01)

def main():
    start_time = datetime.now()
    while True:
        for part in RHYTHM['rhythm']:
            end_time = start_time + timedelta(seconds=PART_DURATION)
            note_duration = PART_DURATION / len(part)
            times = [
                start_time + timedelta(seconds=note_duration*note_index)
                for note_index in range(len(part))
            ]

            for note, playtime in zip(part, times):
                if note:
                    sleep_until(playtime)
                    note.play()
            start_time = end_time

if __name__ == '__main__':
    main()
