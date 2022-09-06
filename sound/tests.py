from django.test import TestCase

# Create your tests here.
//affichage de note
                if (counter == 0){
                    write('<tr>')
                }
                else if (counter == 11){
                    write('<td><center> | </center> </td>');
                    write('</tr>');

                }
                else if (i == notes.length && counter != 11){
                    write('</tr>');
                }

                if(counter == 3) {

                    write('<td><center> | </center> </td>');
                }
                var ton = i%4;
                write('<td><center>'+notes[i]['note']+'</center> </td>');
                   write('<td><center> : </center> </td>');

                }
