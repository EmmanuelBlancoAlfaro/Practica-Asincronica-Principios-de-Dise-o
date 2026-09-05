# Bitácora de la práctica

Estudiante:
Carné:

> Cómo se llena cada entrada, en este orden y sin saltarse pasos:
>
> 1. **Predicción** — escríbala ANTES de correr nada. Qué cree que va a
>    pasar y por qué. Equivocarse aquí y entender después vale más que
>    acertar; no vuelva a corregirla.
> 2. **Observación** — corra el experimento de la etapa y pegue la salida.
> 3. **Explicación** — por qué pasó lo que pasó, en sus palabras, citando
>    **su** archivo y **su** línea (`servicio.py:24`).
> 4. **Sello** — corra `python herramientas/marcador.py` al cerrar la
>    etapa y pegue el sello que imprime.

## Etapa 0 — Diagnóstico

**Predicción:**
Yo creo que esta violando todos los principios
**Observación:**

```
MARCADOR DE LA PRÁCTICA · Principios de diseño
Emmanuel Blanco Alfaro carné 2025077600
Etapa 0 Diagnóstico [verde] verde
4 pruebas en verde · 0 por resolver
corrida #2 registrada
SELLO: 013b3ae0d31c40f1
```

**Explicación: Al completar y explicar el porque estaban mal aplicados todos los principios en el archivo "DIAGNOSTICO.md" con sus evidencias y que puede suceder si no se corrige, se completo de manera existosa la etapa 0, colocando la etapa 0 en verde. **

**Sello: 013b3ae0d31c40f1**

## Etapa 1 — Dividir y conquistar, cohesión

**Predicción: Yo creo que se necesitarán 5 archivos más, porque al tener 6 funcionalidades en una sola clase, este se puede dividir en 5 clases diferentes. **

**Observación:**

```
MARCADOR DE LA PRÁCTICA · Principios de diseño
Emmanuel Blanco Alfaro carné 2025077600
Etapa 1  Dividir y conquistar · cohesión [verde] verde
7 pruebas en verde · 0 por resolver
corrida #3 registrada
SELLO: 4fea7806ca5689e5
```

**Explicación: El rediseño eliminó la sobreacumulación de tareas al separar la clase ServicioRecetas en tres paquetes distintos. Se logró aislar el código aislando la lógica matemática en una función pura que no conoce de bases de datos ni redes(reglas.py:3), y se establecieron invariantes fuertes al usar tipos de datos inmutables con @dataclass(frozen=True) (modelos.py:5). **

**Sello:4fea7806ca5689e5 **

## Etapa 2 — Reducir el acoplamiento

**Predicción: Creo que pueden llegar a haber 3 lugares donde se llegue a cambiar el comportamiento del codigo si se cambia "vigencia_dias" a 1. **

**Observación:**

```
MARCADOR DE LA PRÁCTICA · Principios de diseño
  Emmanuel Blanco Alfaro   carné 2025077600
  Etapa 2  Acoplamiento [verde] verde
  5 pruebas en verde · 0 por resolver
  corrida #8 registrada
  SELLO: b075b8937cd0d6c5
```

**Explicación: Se eliminó el acoplamiento común (estado global) inyectando la configuración a través del constructor de la clase (servicio.py:4). Además, se redujo el acoplamiento de estampado al definir una firma estrecha con tipos simples para la regla de negocio (reglas.py:3) y obligando al caso de uso a recibir un objeto de dominio inmutable en lugar de un diccionario crudo. **

**Sello: b075b8937cd0d6c5**

## Etapa 3 — Abstracción y reuso

**Predicción: Creo que se van a reducir a 0, ya que lo esperable sea que esto se reduja del todo. **

**Observación:**

```
  MARCADOR DE LA PRÁCTICA · Principios de diseño
  Emmanuel Blanco Alfaro   carné 2025077600
  Etapa 3  Abstracción y reuso [verde] verde
  7 pruebas en verde · 0 por resolver
  corrida #9 registrada
  SELLO: 3f36e107f1c04ca0
```

**Explicación: Se establecieron los puertos del dominio usando typing.Protocol (puertos.py:2), aislando los detalles técnicos de infraestructura del núcleo del negocio. Además, se aplicó el principio de reusar lo existente implementando validaciones con expresiones regulares y folios seguros con uuid en la capa de aplicación (borde.py:9), logrando que el método de emisión devuelva un objeto estructurado de tipo Despacho. **

**Sello:3f36e107f1c04ca0 **

## Etapa 4 — Flexibilidad, obsolescencia y portabilidad

**Predicción: Se va a romper todo, porque como se vio anteriormente si se agregaba una farmacia se tenia que modificar el codigo o el método emitir. **

**Observación:**

```
  MARCADOR DE LA PRÁCTICA · Principios de diseño
  Emmanuel Blanco Alfaro   carné 2025077600
  Etapa 4  Flexibilidad · obsolescencia · portabilidad [verde] verde
  7 pruebas en verde · 0 por resolver
  corrida #10 registrada
  SELLO: fc3f9032c796e601
```

**Explicación:**

**Sello:**

## Etapa 5 — Testabilidad

**Predicción:**

**Observación:**

```
```

**Explicación:**

**Sello:**

## Etapa 6 — Diseño defensivo

**Predicción:**

**Observación:**

```
```

**Explicación:**

**Sello:**

## Cierre — Los principios en conflicto

Nombre dos principios que se estorbaron entre sí en SU rediseño, y con qué
criterio resolvió el conflicto. Cite el archivo donde se ve la decisión.

**Conflicto 1:**

**Conflicto 2:**
