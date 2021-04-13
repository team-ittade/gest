# Notas tema 4

## `Reparto secundario - subreparto entre secciones relacionadas` [#21](/tema-4/ejercicios/#ejercicio-21-subreparto-entre-secciones-relacionadas)

1. Se plantea un sistema de ecuaciones para cada centro interrelacionado:
   - Coste primario centro + horas que le dedican otros **centros** = horas totales del centro - horas que se dedica a sí mismo
2. Esto calcula el "precio" de la hora de cada centro. Tenemos que repartir el coste de los **centros** en el resto de sectores (aprovisionamiento, producción, administración).
3. Tabla, donde las columnas sean los sectores (incluidos los **centros**) y las filas sean los repartos (reparto primario y **centros**).
    - En la casillas centro-x/centro-x se pone `(horas totales del centro - horas que se dedica a sí mismo) * precio por hora del centro` (**precio del taller \* la parte derecha de su ecuación**)

## `Valoración de productos en curso` [#24](/tema-4/ejercicios/#ejercicio-24-valoracion-de-productos-en-curso-produccion-equivalente)

De productos terminados nos dan:

- Existencias iniciales
- Iniciadas y terminadas
- Iniciadas y no terminadas

Para cada coste incurrido tenemos que calcular la producción equivalente:

- Existencias iniciales: (100% - porcentaje) \* coste
- Iniciales y terminadas: coste
- Iniciadas no terminadas: porcentaje \* coste

Procesamos los datos:

- Cada coste sumamos todas sus producciones equivalentes y se obtiene la **producción equivalente**.
- Dividiendo la producción equivalente entre los ^^costes de producción realizada^^ podemos calcular los **costes unitarios de producción realizada**.
- **Existencia final** se calcula como `costes unitarios de producción realizada * Unidades equivalentes de existencias finales`
    - Ej: si tenemos 500 unidades finales no terminadas que tienen un 90% de materias primas obtenemos un total de `90% * 500 = 450` unidades equivalentes de existencia final de materias primas.
- La **Producción terminada** nos lo dan. Es el número de unidades que se han terminado.
- El **coste de la producción terminada** se calcula como `existencias iniciales + sumatorio de los costes de la producción realizada - existencia final`

??? question "¿Por qué las fórmulas?"
    - **Existencias iniciales:** son las existencias que había inicialmente. Para poder hacer el producto hemos tenido que emplear un coste de `100%` - `porcentaje`.
    - **Iniciales y terminadas:** hemos empleado el `100%` del coste.
    - **Iniciales no terminadas:** hemos empleado el `porcentaje` del coste.
