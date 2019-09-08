from django.shortcuts import render
from django.http import HttpResponse
from .models import plot_img
import webrtcvad
import pyaudio
import wave
import os, sys
import librosa
import numpy as np
import matplotlib.pyplot as plt
import librosa.display
import tensorflow as tf
import time
# Create your views here.
def home(request):
    output=[
        {
        'input_file':"No Choosen File",
        }
    ]
    context={
            'output':output
        }

    return render(request,'index.html',context)

def predict(request):
    file=request.POST.get('audioSave')
    if file==None or len(file)==0:
        return HttpResponse("Sorry Give some input")
        print(file)
    else:

         with tf.gfile.FastGFile("retrained_graph.pb", 'rb') as f:

             graph_def = tf.GraphDef()
             graph_def.ParseFromString(f.read())
             tf.import_graph_def(graph_def, name='')

         with tf.Session() as sess:


            # Feed the image_data as input to the graph and get first prediction
             softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
             print('hold on!')
             time.sleep(1)
             # frames = []
             # frameCount = 0
             # while frameCount < 5:
             #     data = stream.read(CHUNK)
             #     if vad.is_speech(data, RATE):
             #         frameCount+=1;
             #     else:
             #         frameCount = 0;


             #   # print frameCount
             # print("recording...")
             # for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
             #    data = stream.read(CHUNK)
             #    frames.append(data)
             # print("finished recording")
             # waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
             # waveFile.setnchannels(CHANNELS)
             # waveFile.setsampwidth(audio.get_sample_size(FORMAT))
             # waveFile.setframerate(RATE)
             # waveFile.writeframes(b''.join(frames))
             # waveFile.close()
             # os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
             audio_path = file #file.wav
             image_path = 'tmp.png'
             try:


                y, sr = librosa.load(audio_path)
                try:

                    l = librosa.get_duration(y=y, sr=sr)
                    if(l >= 4.5 and l <= 10):
                        S = librosa.feature.melspectrogram(y, sr=sr, n_mels=128)
                        log_S = librosa.core.amplitude_to_db(S, ref=np.max)
                        fig = plt.figure(figsize=(12,4))
                        ax = plt.Axes(fig, [0., 0., 1., 1.])
                        ax.set_axis_off()
                        fig.add_axes(ax)
                        librosa.display.specshow(log_S, sr=sr, x_axis='time', y_axis='mel')
                        plt.savefig(image_path)
                        plt.close()
                    elif(l > 10 and l <15):
                        y1 = y[:int(len(y)*0.75)]
                        S = librosa.feature.melspectrogram(y1, sr=sr, n_mels=128)
                        log_S = librosa.core.amplitude_to_db(S, ref=np.max)
                        fig = plt.figure(figsize=(12,4))
                        ax = plt.Axes(fig, [0., 0., 1., 1.])
                        ax.set_axis_off()
                        fig.add_axes(ax)
                        librosa.display.specshow(log_S, sr=sr, x_axis='time', y_axis='mel')
                        plt.savefig(image_path)
                        plt.close()
                except Exception as e:
                    print(e)
             except Exception as e:
                print(e)
            # Read in the image_data
             image_data = tf.gfile.FastGFile(image_path, 'rb').read()
            # Loads label file, strips off carriage return
             label_lines = [line.rstrip() for line
                               in tf.gfile.GFile("retrained_labels.txt")]
             predictions = sess.run(softmax_tensor, \
                     {'DecodeJpeg/contents:0': image_data})
            # Sort to show labels of first prediction in order of confidence
             top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
             print('%s (score = %.5f)' % (label_lines[top_k[0]], predictions[0][top_k[0]]))

             plt.bar(label_lines,predictions[0])
             plotfile = 'plot.png'
             # img_data=plot_img(image=plotfile)
             # img_data.save()
             # #plt.savefig(plotfile)
             # # plt.show()
             # #img_data=plot_img(image=data)
             # #img_data.save()
             # plot_img_data=plot_img.objects.all()
             out = str(label_lines[top_k[0]])#predictions[0]
             print(np.array(predictions[0])*100,label_lines)
             final_data=dict(zip(label_lines,(np.array(predictions[0])*100)))
             
             print(final_data)
             bar_data=[]
             bar_data.append(final_data)
             output=[
              {'output_file':out,
                'input_file':file,}
             ] 
             context={
             'output':output,
             'bar_data':bar_data,

             }
    return render(request,'index.html',context)



