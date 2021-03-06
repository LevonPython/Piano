import pyaudio
import wave
from datetime import datetime
# pip install pipwin
# pipwin install pyaudio

"""
pyaudio gives you more low-level control, it is possible to get and set parameters for your input and output devices,
and to check your CPU load and input or output latency.
"""

# rec_status = int(input("Do you want to record? Insert 1 or 0: "))
# print(f"rec_status: {rec_status}")

chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 2
fs = 44100  # Record at 44100 samples per second
seconds = 1
file_date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"records/record_{file_date}.wav"
print(filename)

p = pyaudio.PyAudio()  # Create an interface to PortAudio

stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                input=True)
frames = []  # Initialize array to store frames
seconds_count = 0
# while rec_status == 1:

print('Recording')
# data = stream.read(chunk)
# frames.append(data)
# rec_status = int(input("Continue recording? Insert 1 or 0: "))
# Store data in chunks for specified time (seconds)
for i in range(0, int(fs / chunk * seconds)):
    data = stream.read(chunk)
    frames.append(data)
seconds_count += 1

print(f"frames {frames}")

# Stop and close the stream
stream.stop_stream()
stream.close()
# Terminate the PortAudio interface
p.terminate()

print('Finished recording')

# Save the recorded data as a WAV file
wf = wave.open(filename, 'wb')
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(sample_format))
wf.setframerate(fs)
wf.writeframes(b''.join(frames))
wf.close()
print(f"{seconds_count} seconds recorded")
