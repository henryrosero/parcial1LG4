import pprint
import collections

primerCapitulo = '''
este es un texto el cual deben contar el numero
de palabras que tiene, deben tener en cuenta,
que algunas palabras se separa por un punto, y una
coma, tambien hay que tener en cuenta, que las palabras
escritas EN MAYUSCULAS y minusculas cuenta como una este. Texto
'''

conteo = {}
 
for palabra in primerCapitulo.upper().split():
     conteo.setdefault(palabra, 0)
     conteo[palabra] = conteo[palabra] + 1

conteoEnOrden = collections.Counter(conteo)

pprint.pprint(conteoEnOrden.most_common())

loremIpsum = 'Lorem ipsum dolor sit amet, eos vidisse invenire intellegebat ex, in has dolorem facilisi recusabo. Ad eum melius labores rationibus. Ea corpora maiestatis pri, ius simul exerci eu. Per virtute intellegam ex, sea id salutatus mediocritatem, duo at possit aliquip adipisci. An nec quod falli contentiones, falli partem adipiscing quo an. Unum salutandi cum no, affert delenit qualisque vis cu, cu velit scripta deterruisset pri.'


listaOraciones = loremIpsum.split('. ')

for oracion in listaOraciones:
    print(oracion, str(len(oracion.split(' '))))