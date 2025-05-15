from scipy.signal import butter, filtfilt
# import IPython.display as ipd
import soundfile as sf
import numpy as np
import librosa
import matplotlib.pyplot as plt

def butter_filter(data, sr, cutoff, btype='low', order=5):
    nyq = 0.5 * sr
    normal_cutoff = np.array(cutoff) / nyq if isinstance(cutoff, (list, tuple)) else cutoff / nyq
    b, a = butter(order, normal_cutoff, btype=btype, analog=False)
    return filtfilt(b, a, data)

file_path = "data/catsound.wav"
y, sr = librosa.load(file_path, sr=None)
# y = y[:sr]

duration_sec = len(y) / sr
print(f"Duration: {duration_sec:.2f} seconds")

# Use 0.5s from a valid time (e.g., start at 0.5s)
start_time = 0.5
end_time = start_time + 0.5

# Convert to sample index and clip within bounds
start_sample = int(start_time * sr)
end_sample = int(min(len(y), end_time * sr))

segment = y[start_sample:end_sample]

# Check if segment has sufficient data
if len(segment) == 0:
    raise ValueError("Segment is empty. Choose a valid start time and ensure the signal is long enough.")

# Plot spectrum
N = len(segment)
fft_vals = np.fft.rfft(segment)
frequencies = np.fft.rfftfreq(N, d=1/sr)
magnitude = np.abs(fft_vals)

plt.figure(figsize=(10, 4))
plt.plot(frequencies, magnitude)
plt.title("Original Spectrum (0.5s segment)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid(True)
plt.tight_layout()
plt.show()

# Listen to original segment
# ipd.Audio(segment, rate=sr)
# Low-pass filter (below 1000 Hz)
low = butter_filter(segment, sr, cutoff=1000, btype='low')

# High-pass filter (above 1000 Hz)
high = butter_filter(segment, sr, cutoff=1000, btype='high')

# Band-stop filter (remove 500–2000 Hz)
bandstop = butter_filter(segment, sr, cutoff=[500, 2000], btype='bandstop')

sf.write("lowpass_filtered.wav", low, sr)
sf.write("highpass_filtered.wav", high, sr)
sf.write("bandstop_filtered.wav", bandstop, sr)

print("Filtered audio files saved:")
print("- lowpass_filtered.wav")
print("- highpass_filtered.wav")
print("- bandstop_filtered.wav")