import freqbands
import waterfall
 

SignalInfo='SDR.wav'
Fcentre=137.5
Fsample=2.05
filename = 'satellite_db.json'
bands = freqbands.getbands(SignalInfo, filename)
print(bands)
chunksize = int(1024 * 2 * 2 * 2 * 2 * 2 * 2 * 2)
waterfall.plot_waterfall(SignalInfo, chunksize, 30)
