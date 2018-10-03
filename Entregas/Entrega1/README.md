# Big Data - Entrega 1
La entrega consiste en la implementación de un proyecto (Java o Python a elección) y un informe respondiendo a todas las consignas presentes en este enunciado. 
La fecha límite de entrega es el 23 de octubre de 2018.  La calificación obtenida en este TP será tenida en cuenta en la nota final de la materia.

Implementar jobs (procesos map y reduce) que permitan hacer las operaciones básicas entre conjuntos para utilizarlos en la resolución de un problema más complejo.
- Unión 
- Intersección 
- Diferencia 
- Igualdad 
- Complemento 
- Cardinalidad 
 -Pertenencia 


#### Unión
```python
map 
write <value, null> # deberia ser (map)<number, stub> ->(comb)  ->(redc)<number> asi llegan todos al mismo reducer?
reduce 
write <value, null>

#Funcion del mapper: Elimina la distinción por grupo, 
#Funcion del reducer:
#Ventajas de un combiner: En este caso no serviría de nada ya que no hace falta combinar/reducir los datos en ningun momento.
```

#### Intersección
```python
map 
write <valor, 1>
reduce 
if list.length = 2 
	write<value, null>
```

#### Diferencia A-B
```python
map 
write < value, “A”> o write <value, “B”>

reduce

if (list.length < 2 && list.get(0) == “A”)
	write <value, null>
```


#### Complemento
```python

U - a 
map 
write <value, “U”> o <value, “A”>

reduce
if (list.length < 2 && list.get(0) == “U”)
	write <value, null>
```


#### Cardinalidad
```python
map 
write <unique, 1>

combiners(?)

reduce
	write <acum, null>
```


#### Pertenencia
```python
map 
write <value, 1>

reduce
write <value, list.length == 2> # esto imprime todos los numeros, no solo los de B
```


#### Igualdad
```python
entrada es la salida del job anterior <pertenencia>
Map
if (es false)
write <hay_false, 1>

reduce 
	write <”NO”, null>

alternativa 
map 
	write <value, 1>

reduce
	if (list.length < 2) write <NO, null>
```


#### Ejercicio 8
```python
map 
write <value, “A”> o <value, “B”> o <value, “C”>

reduce 
if (list.length == 1) write <value, null>
```


#### 9
```python
cardinalidad
acumulacion igual

pertenencia
map <value, X> o <value, E>
reduce
if list length == 2 <value, true> sino <value, false>

```


