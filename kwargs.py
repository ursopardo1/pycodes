"""
**kwargs
Funciona semelhantemente ao *args, mas salva os valores extras em dicionário {}


ordem correta de declaração:

- Parâmetros obrigatórios;
- *args;
- Parâmetros default;
- **kwargs

"""


def cores_favoritas(**kwargs):
    return (kwargs)


dict = cores_favoritas(vanderson='rosa', jeff='anil', georgia='gótica')

print(dict.get('vanderson'))
print(dict.items())

del dict['jeff']
print(dict)
