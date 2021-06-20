function [fSSA,fSSP] = funSpectralData(S,freqsampledouble)

%%FFT of the input image
fS = fft(single(S),freqsampledouble);
fSS = fftshift(fS);

%Amplitude Spectrum
fSSA = abs(fSS);

%%Phase spectrum
fSSP = angle(fSS);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
