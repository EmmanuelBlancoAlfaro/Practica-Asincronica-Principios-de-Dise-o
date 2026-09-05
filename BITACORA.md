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
No existe experimento no se llena nada
```

**Explicación: Al completar y explicar el porque estaban mal aplicados todos los principios en el archivo "DIAGNOSTICO.md" con sus evidencias y que puede suceder si no se corrige, se completo de manera existosa la etapa 0, colocando la etapa 0 en verde. **

**Sello: 013b3ae0d31c40f1**

## Etapa 1 — Dividir y conquistar, cohesión

**Predicción: Yo creo que se necesitarán 5 archivos más, porque al tener 6 funcionalidades en una sola clase, este se puede dividir en 5 clases diferentes. **

**Observación:**

```
No existe experimento
```

**Explicación: El rediseño eliminó la sobreacumulación de tareas al separar la clase ServicioRecetas en tres paquetes distintos. Se logró aislar el código aislando la lógica matemática en una función pura que no conoce de bases de datos ni redes(reglas.py:3), y se establecieron invariantes fuertes al usar tipos de datos inmutables con @dataclass(frozen=True) (modelos.py:5). **

**Sello:4fea7806ca5689e5 **

## Etapa 2 — Reducir el acoplamiento

**Predicción: Creo que pueden llegar a haber 3 lugares donde se llegue a cambiar el comportamiento del codigo si se cambia "vigencia_dias" a 1. **

**Observación:**

```
Configuración actual: {'farmauno_url': 'https://api.farmauno.cr/v3/rx', 'saludtotal_url': 'https://ws.saludtotal.cr/api/recetas', 'cruzverde_url': 'https://soap.cruzverde.cr/Recetas.asmx', 'vigencia_dias': 1, 'tarifa_diaria': 250, 'timeout': 1.5}

Al inspeccionar clinicasegura/legado.py, el diccionario CONFIG se utiliza en múltiples lugares (para definir URLs de conexión, establecer timeouts y calcular la fecha exacta de vencimiento sumando vigencia_dias). Esto demuestra que una sola línea modificada desde el exterior altera la regla de negocio del vencimiento en todo el servicio de forma invisible, comprobando el grave riesgo de acoplamiento que genera el estado global.
```

**Explicación: Se eliminó el acoplamiento común (estado global) inyectando la configuración a través del constructor de la clase (servicio.py:4). Además, se redujo el acoplamiento de estampado al definir una firma estrecha con tipos simples para la regla de negocio (reglas.py:3) y obligando al caso de uso a recibir un objeto de dominio inmutable en lugar de un diccionario crudo. **

**Sello: b075b8937cd0d6c5**

## Etapa 3 — Abstracción y reuso

**Predicción: Creo que se van a reducir a 0, ya que lo esperable sea que esto se reduja del todo. **

**Observación:**

```
  Se predijo que al rediseñar la arquitectura introduciendo modelos propios (Anti-Corruption Layer), el radio de impacto de estas llaves bajaría a cero en el dominio. Esto se comprobó con éxito: el nuevo diseño usa tipos estrictos en modelos.py, encapsulando los datos y evitando que las llaves mágicas del JSON externo se esparzan por los casos de uso
```

**Explicación: Se establecieron los puertos del dominio usando typing.Protocol (puertos.py:2), aislando los detalles técnicos de infraestructura del núcleo del negocio. Además, se aplicó el principio de reusar lo existente implementando validaciones con expresiones regulares y folios seguros con uuid en la capa de aplicación (borde.py:9), logrando que el método de emisión devuelva un objeto estructurado de tipo Despacho. **

**Sello:1472b7d93be3d92b **

## Etapa 4 — Flexibilidad, obsolescencia y portabilidad

**Predicción: Se va a romper todo, porque como se vio anteriormente si se agregaba una farmacia se tenia que modificar el codigo o el método emitir. **

**Observación:**

```
  La prueba falló al intentar procesar "FarmaViva". Esto demostró que, con el diseño viejo, es obligatorio modificar el código interno del orquestador (añadir un nuevo elif) cada vez que hay un nuevo proveedor, lo cual viola directamente el principio Abierto/Cerrado.
```

**Explicación: Se rediseñó el orquestador del servicio (servicio.py:13) para eliminar los condicionales rígidos por nombre de cadena, integrando un registro dinámico (registro.py:3). Asimismo, se aseguró la portabilidad y configuración por entorno en arranque.py y se documentó formalmente el ciclo de vida y riesgo de las dependencias externas en el archivo DEPENDENCIAS.md. **

**Sello: fc3f9032c796e601**

## Etapa 5 — Testabilidad

**Predicción: Al intentar emitir una receta con el servicio heredado, la ejecución fallará o requerirá un entorno real completo (red y base de datos), porque el código esta incompleto teniendo llamadas de forma incorrecta, haciendo que sucedan varios errores. **

**Observación:**

```
  Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    s = ServicioRecetas()
  File "D:\TEC\Cuarto Semestre\Diseño\Practica-Asincronica-Principios-de-Diseño\clinicasegura\legado.py", line 50, in __init__
    self.db = sqlite3.connect(os.path.join("/tmp", "clinicasegura.db"))
              ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    sqlite3.OperationalError: unable to open database file

    Al correr el experimento aparece este error, ya que al intentar conectarse a la base de datos, la ruta es ed linux y al estar usando windows es imposible lograr esto.
```

**Explicación: Se rediseñó el servicio para garantizar la testabilidad. Se implementó la carpeta mis_pruebas/ con pruebas personalizadas para validar escenarios de controlabilidad y observabilidad, incluyendo relojes fijos, manejo de errores por red y validación en el borde. **

**Sello: 1caab80d9be316d6 **

## Etapa 6 — Diseño defensivo

**Predicción: La diferencia entre la primera y la segunda es la bandera -O que es para optimizar, por lo que supongo que la primera no servira o durara mucho en correr y la segunda será mas rapida y funcionará perfectamente. **

**Observación: **

```
No se puede probar el experimento, porque la ruta que aparece necesita linux y tengo windows, por lo que no puedo conocer el resultado. 
```

**Explicación: Se estableció una frontera de confianza estricta utilizando Pydantic con las configuraciones extra="forbid" y frozen=True, garantizando que los datos externos no confiables se pasen a tipos válidos del dominio (mediante la función a_receta) y no sufran mutaciones posteriores. Se implementó una política de fallos explícita, si la pasarela de la farmacia falla, el error no se silencia con bloques except vacíos ni se devuelve None, en su lugar, se propaga una excepción de dominio (FarmaciaNoDisponible) que incluye contexto crítico, y se registra el evento para mantener la trazabilidad. **

**Sello: 7706f39affe17bc5**

## Cierre — Los principios en conflicto

Nombre dos principios que se estorbaron entre sí en SU rediseño, y con qué
criterio resolvió el conflicto. Cite el archivo donde se ve la decisión.

**Conflicto 1: Defensa en la frontera vs. Paranoia interna (Principio 11):
Existe una tensión directa entre proteger el sistema de datos externos maliciosos o erróneos y caer en código redundante. La directriz exige validar estrictamente en el borde (frontera de confianza) mediante esquemas como Pydantic, pero advierte que verificar lo mismo en el interior del código es código paranoico, ya que duplica validaciones, confunde al lector sobre dónde recae la responsabilidad y viola la limpieza del dominio.**

**Conflicto 2: Testabilidad y Desacoplamiento vs. Simplicidad de uso (Principios 9 y 10):
Para lograr la testabilidad absoluta y eliminar el estado global, se obliga a pasar explícitamente todas las dependencias por el constructor (reloj, folios, pasarelas, bitácora). Esto entra en conflicto con la "comodidad" inicial del código legacy (donde bastaba con llamar ServicioRecetas()), obligando a aceptar un mayor volumen de código de configuración (boilerplate de inyección) a cambio de ganar controlabilidad, observabilidad y aislamiento en las pruebas. **
