from scipy.io.wavfile import write
from scipy.io.wavfile import read
import numpy as np

#threshold should be the value of percentage of the average value of the spectral density

#threshhold should be between 0 and 1

def denoise(filename, threshold)

	rate, f = read(filename)

	f = f[:,0]        					   # Just taking the data of right speaker 
	dt = 1/len(f)
	t = np.arange(0, 1, dt)
	n = len(t)

	fhat = np.fft.fft(f,n)                 # Compute the FFT
	PSD = fhat * np.conj(fhat) / n         # Power spectrum (power per freq)


	data_avarage = np.average(PSD)
	indices = PSD > threshold*average      # Find all freqs with large power

	PSDclean = PSD * indices       		   # Zero out all others
	fhat = indices * fhat          		   # Zero out small Fourier coeffs. in Y
	ffilt = np.fft.ifft(fhat)      		   # Inverse FFT for filtered time signal

	write('new.wav', rate, np.asarray(ffilt, dtype=np.int16))

	print("New wav file created")


# denoise(##,##)
