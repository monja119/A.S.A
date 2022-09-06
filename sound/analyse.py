# octave = Intervalle parfait de huit degrés de l'échelle diatonique (par ex., de do à do).

from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404,request

import math
import matplotlib.pyplot as plt
import librosa
import librosa.display
from  fractions import  Fraction
import io

from django.template.loader import get_template,render_to_string

class Analyse:
    def __init__(self,file_path,name):
        self.notes = []
        try :
            # analyse du fichier :
            # analyse du son:
            onde, frequence = librosa.load(file_path)  # frequence en Hz = echantillon
            tempo= librosa.beat.beat_track(y=onde, sr=frequence)[0] #inverse de frequence
            tempo_min = int(tempo)/60
            longeur_onde = onde.shape[0]

            temps_de_battement = librosa.frames_to_time(onde, sr=frequence)
            amplitude = librosa.magphase(onde, power=1)[0]   * math.pow(10,3)



            #___________________ AFFICHAGE
            val_x = []
            val_y = []
            for x in range(longeur_onde):
                y = amplitude[x]
                val_y.append(y)  # 404 onde de reference
                val_x.append(x)

            plt.figure(facecolor='gray')
            plt.title(f"Spectogramme de {name}", fontweight='bold')
            plt.xlabel(' Wage', fontweight='bold')
            plt.ylabel(' Frequency (Hz) ', fontweight='bold')
            plt.plot(val_x,val_y)
            plt.legend([name])
            fig = plt.gcf()
            fig.set_size_inches(10.5, 10.5)
            fig.savefig('sound/static/plots/{}.png'.format(name), size=(10,10), dpi=100)


            # __________________ HARMONIE DU SON

            boublons = []
            tons = [0]
            mesure = 0

            # traduction de note en mathematiques
            self.notes = []
            cles= ['do','re','mi','fa','so','la','si','do']
             # note de Do
            cle = cles.index('do')+1

            solfa = [('La3',440 * cle),
                     ('li',466 * cle),
                     ('Si',493 * cle),
                     ('Do',523 * cle),
                     ('Di',554 * cle),
                     ('Ré',587 * cle),
                     ('Ri',622 * cle),
                     ('Mi',659 * cle),
                     ('Fa',698 * cle),
                     ('Fi',739 * cle),
                     ("sol",783 * cle),
                     ('zi',830 * cle),
                     ("La4",880 * cle)]


            # adjustemnt de gammma, octave et l'intervalle de temps
            notes = []
            position = 0
            for x in range(1,longeur_onde):
                # recuperation de la mesure

                ton = x % (frequence//4)
                if ton == 0:
                    position +=1


                # ajout au note
                val_y[x] = int(val_y[x])
                for s in range(len(solfa)):
                    if val_y[x] in solfa[s]:
                        self.notes.append({
                            'note' : solfa[s][0],
                            'position' :position
                        })
            for n in range(len(notes)):
                print(notes[n]['note'])
        except FileNotFoundError :
            print(f" Fichier non introuvable : {file_path}")

