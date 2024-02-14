print("Documentación Global de Git, control de versiones.")

"""

git --help
    --Muestra la ayuda de git

ls
    --Muestra los ficheros

cd <Tabulador>  
    --Muestra los diferentes directorios
cd ..
    --Nos retorna a un directorio anterior
cd "C:\Users\X_HernandJ03\OneDrive - Primary Products Ingredients Americas LLC\Desktop\Documents\Git"
    --Path de trabajo actual

pwd
    --Muestra la dirección <PATH> donde me encuentro

mkdir <Nombre>
    --Comando para crear un directorio

0]
git init
    --Se indica que es el repositorio de control de versiones
    --Ahora estamos en la rama <Master>    
    
1]
git config --global user.name "jes-1304"
git config --global user.email "jes_1304@hotmail.com"
    --Congiguración GLOBAL, son necesarios los dos valores para iniciar.     

2]
git branch -m <Nombre>
    --Podemos cambiar el nombre de la rama <Master> a el <Nombre> a elegir
git granch -D <name>
    -- Elimina una rama por completo    

3]
git status
    --Podemos conocer el status de nuestro proyecto

4]
notepad <name>.<py>
    --Crea un archivo notepad de tipo Python
echo > <name>.<extensión>
    --Crea un archivo sin pedir que se guarde, mejor opción.
    --Ahora sólo debe abrir el archivo desde las opciones del editor para que pase de solo lectura a escritura.        

del <name>.<extensión>
    --Borra el archivo indicado    

5]
git add <Archivo>
    --Incluye el archivo en el proyecto -control de versiones-    
git add .
    --Incluye todos los archivos en el proyecto.

6]
git status
    --Nos muestra el resultado antes de una fotografía(commit)    
    
7]
git commit -m "COMENTARIO(S): Control de versiones"    
    --Nos resguarda todo lo que hemos guardado con "add ." etc.

8]
git log
    --Muestra el historial de los commit (Cambios Guardados) + su "Hash" con el que se almaceno    
    --Como podemos hacer una foto grafía

git log --graph
    --Nos muestra el detalle en una rama
git log --graph --pretty=oneline
    --Nos muestra el detall en una sola linea
git log --graph --decorate --all -oneline
    --Nos muestra una linea + el Hash por versión

9]
git config --global alias.<name> "Comando"
git config --global alias.pretty "log --graph --pretty=oneline"
git pretty
    --Nos mostrara mediante un alias el resultado del comando "log --graph --pretty=oneline"

10]
git checkout <Nombre de Arvhivo>
    --Nos retornara los valores a el último punto guardado (commit)
git reset
    --Nos mostrara que hay archivos con modificaciones por lo que puedes usar el anterior comando.
git checkout HEAD
    --Nos permite posicionarnos en ese momento como la cabecera
git checkout <Nombre Rama>
    --Nos permite cambiarnos a la rama especificada inclusive donde hicimos el reset --hard

11]
git merge main "Fucionarse"
    --Nos permite fucionar archivos/cambios/etc.
    --Incluso sirve para validar comparativos de codigo entre diferentes personas.

12]
git stash
    --Nos permite guardar temporalmente un cambio sin hacer un commit
git stash list
    --Nos permite ver un listado de cambios pendientes por guardar (Commit)
git stash pop
    --Nos permite retornar el punto donde dejamos el trabajo pendiente    
git stash drop
    --Nos permite retornar a un punto antes del guardado de formsa temporal
        
"""
