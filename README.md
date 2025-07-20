# Lab 02 - Sistema de Tipos con ANTLR

Video de YouTube: https://youtu.be/COM341JzeGA

## Descripción

* **Gramática**: `SimpleLang.g4`, que define operaciones aritméticas y literales.
* **Visitor**: Implementado en `type_check_visitor.py` bajo el paquete `visitor/`.
* **Listener**: Implementado en `type_check_listener.py` bajo el paquete `listener/`.
* **Tipos**: Definidos en `custom_types.py` (`IntType`, `FloatType`, `StringType`, `BoolType`).
* **Casos de prueba**:
  * `program_test_pass.txt`, `program_test_no_pass.txt` (tests básicos).
  * `mod_test_pass.txt`, `mod_test_no_pass.txt` (tests de extensiones `%` y `^`).

## Levantar el entorno

1. Construye la imagen Docker y monta el directorio `program`:

   ```bash
   docker build --rm . -t lab2-image && docker run --rm -ti -v "$(pwd)/program":/program lab2-image
   ```
   
2. Accede al contenedor (ya estás dentro de `/program`).

## Generar Visitor y Listener

Dentro del contenedor, en la raíz `/program`, ejecuta:

```bash
# Crea los paquetes
mkdir visitor
mkdir listener

# Genera artefactos del Visitor (sin Listener)
antlr -Dlanguage=Python3 -visitor -o visitor/ SimpleLang.g4

# Genera artefactos del Listener (sin Visitor)
antlr -Dlanguage=Python3 -listener -o listener/ SimpleLang.g4
```

## Ejecutar pruebas

### Visitor

```bash
cd visitor/
python3 ../Driver.py ../mod_test_pass.txt    # debe imprimir "Type checking passed"
python3 ../Driver.py ../mod_test_no_pass.txt # debe fallar con un TypeError de  ^ o %
cd ..
```

### Listener

```bash
cd listener/
python3 ../DriverListener.py ../mod_test_pass.txt    # debe imprimir "Type checking passed" 
python3 ../DriverListener.py ../mod_test_no_pass.txt # debe listar todos los errores de tipo ^ o %
cd ..
```

## Estructura del proyecto

```
/program
├── SimpleLang.g4
├── custom_types.py
├── program_test_pass.txt
├── program_test_no_pass.txt
├── mod_test_pass.txt
├── mod_test_no_pass.txt
├── visitor/
└── listener/
```

## Resultados y análisis iniciales

**1. Ejecución de casos de prueba “pass” y “no_pass”**

- Visitor:
	- <img width="966" height="95" alt="Pasted image 20250720113635" src="https://github.com/user-attachments/assets/772d3c8f-0a7d-4999-ac13-c35f650940e5" />


- Listener:
	- <img width="1046" height="174" alt="Pasted image 20250720113653" src="https://github.com/user-attachments/assets/2a9a0003-c640-4b38-a3e0-4259bb933b12" />



**2. Análisis de por qué pasan o fallan los ejemplos actuales**

#### a) Ejemplos que **pasan** (`pass.txt`)

```text
5 + 3.0
10 * 2.5
4.5 + 2
```

- `5 + 3.0`:
    
    - **Izquierda:** `IntType`
        
    - **Derecha:** `FloatType`
        
    - **Regla:** `int + float → float`
        
    - **Resultado:** `FloatType` → _aceptado_.
        
- `10 * 2.5`:
    
    - **Izquierda:** `IntType`
        
    - **Derecha:** `FloatType`
        
    - **Regla:** `int * float → float`
        
    - **Resultado:** `FloatType` → _aceptado_.
        
- `4.5 + 2`:
    
    - **Izquierda:** `FloatType`
        
    - **Derecha:** `IntType`
        
    - **Regla:** `float + int → float`
        
    - **Resultado:** `FloatType` → _aceptado_.
        

#### b) Ejemplos que **falla**n (`no_pass.txt`)

```text
8 / "2.0"
(3 + 2) * "7"
9.0 - true
"hello" + 3
```

1. `8 / "2.0"`
    
    - **Izquierda:** `IntType`
        
    - **Derecha:** `StringType`
        
    - **Error:** “Unsupported operand types for * or /: int and string”
        
    - El Visitor detiene aquí la ejecución; el Listener lo registra y continúa.
        
2. `(3 + 2) * "7"`
    
    - Primero se evalúa `(3 + 2) → IntType`.
        
    - Luego `IntType * StringType`.
        
    - **Error:** “Unsupported operand types for * or /: int and string”
        
    - Se reporta de nuevo (por eso aparecen dos entradas iguales en el Listener, una por cada operación `MulDiv`).
        
3. `9.0 - true`
    
    - **Izquierda:** `FloatType`
        
    - **Derecha:** `BoolType`
        
    - **Error:** “Unsupported operand types for + or -: float and bool”
        
4. `"hello" + 3`
    
    - **Izquierda:** `StringType`
        
    - **Derecha:** `IntType`
        
    - **Error:** “Unsupported operand types for + or -: string and int”
        
Con esta verificación y análisis, se puede ver que:

- El **Visitor** arroja el primer error y detiene la comprobación.
    
- El **Listener** acumula todos los conflictos de tipo en `listener.errors`, permitiendo un reporte completo.

---

## Resultado y análisis después de las modificaciones

### Pruebas con el **Visitor**

Nos movemos a la carpeta `visitor/` y ejecutamos los tests para las nuevas operaciones (`mod_test_pass.txt` y `mod_test_no_pass.txt`):

<img width="947" height="87" alt="Pasted image 20250720125128" src="https://github.com/user-attachments/assets/b05c2df9-f3ce-487d-8bc6-5f886d73b558" />

```bash
root@...:/program/visitor# python3 ../Driver.py ../mod_test_pass.txt
Type checking passed

root@...:/program/visitor# python3 ../Driver.py ../mod_test_no_pass.txt
Type checking error: Unsupported operand types for %: float and float
```

* **`mod_test_pass.txt`** contiene estas líneas válidas:

  ```text
  7 % 3
  2 ^ 5
  4.0 ^ 2
  ```

  1. **`7 % 3`**

     * Ambos operandos son `IntType`.
     * La regla de módulo (`%`) sólo acepta enteros y produce `IntType`.
     * → *aceptado*.

  2. **`2 ^ 5`**

     * Ambos operandos son `IntType`.
     * La regla de potencia (`^`) acepta cualquier combinación numérica y devuelve `IntType` cuando ambos son enteros.
     * → *aceptado*.

  3. **`4.0 ^ 2`**

     * Izquierda `FloatType`, derecha `IntType`.
     * `^` entre numéricos da `FloatType` si alguno es float.
     * → *aceptado*.

* **`mod_test_no_pass.txt`** contiene:

  ```text
  5.0 % 2.0
  true ^ false
  "abc" ^ 2
  ```

  El **Visitor** detiene la comprobación en la **primera** línea incorrecta:

  * **`5.0 % 2.0`**

    * FloatType `%` FloatType.
    * Módulo sólo permite `IntType % IntType`.
    * → `TypeError: Unsupported operand types for %: float and float`.

---

### Pruebas con el **Listener**

Desde `listener/`, ejecutamos los mismos ficheros:

<img width="995" height="157" alt="Pasted image 20250720125145" src="https://github.com/user-attachments/assets/ea7cbe0a-dd41-4c63-903e-689a50e25b2a" />

```bash
root@...:/program/listener# python3 ../DriverListener.py ../mod_test_pass.txt
Type checking passed

root@...:/program/listener# python3 ../DriverListener.py ../mod_test_no_pass.txt
Type checking error: Unsupported operand types for %: float and float
Type checking error: Unsupported operand types for ^: bool and bool
Type checking error: Unsupported operand types for ^: string and int
```

* En **`mod_test_pass.txt`** el Listener no encuentra conflictos y muestra *“Type checking passed”*.
* En **`mod_test_no_pass.txt`** acumula **todos** los errores:

  1. **`5.0 % 2.0`** → `%` sólo IntType  → *error*
  2. **`true ^ false`** → `^` sólo numéricos    → *error*
  3. **`"abc" ^ 2`** → `^` sólo numéricos       → *error*

Al completar estas pruebas, confirmamos que:

* **Visitor** reporta el primer conflicto y detiene la ejecución.
* **Listener** recopila y muestra cada conflicto de tipo en el orden en que aparecen en el AST.


