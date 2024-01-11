from db import database
from pydantic import BaseModel
from fastapi import APIRouter, HTTPException

router_actividad_diaria = APIRouter()

class updateActividadDiaria(BaseModel):
    descripcion: str
    hora_inicio: str
    hora_fin: str

@router_actividad_diaria.get("/actividad_diaria/", tags=["Actividad Diaria"])
async def obtenerActividadesDiarias():
    try:
        conn = database.getConnection()
        cursor = conn.cursor()

        query = ''' 
                    SELECT 
                        ad_secuencial, 
                        ad_descripcion, 
                        ad_hora_inicio, 
                        ad_hora_fin, 
                        ad_dia, 
                        ad_usuario,
                        ad_estado,
                        ad_fecha_bd
                    FROM 
                        actividad_diaria
                    ORDER BY
                        ad_usuario, ad_fecha_bd;
                '''
        cursor.execute(query)
        actividades_diarias = cursor.fetchall()

        conn.close()

        if actividades_diarias:
            lista_actividades_diarias = []
            for detalles_actividad_diaria in actividades_diarias:
                actividad_diaria = {
                    "ad_secuencial": detalles_actividad_diaria[0],
                    "ad_descripcion": detalles_actividad_diaria[1],
                    "ad_hora_inicio": detalles_actividad_diaria[2],
                    "ad_hora_fin": detalles_actividad_diaria[3],
                    "ad_dia": detalles_actividad_diaria[4],
                    "ad_usuario": detalles_actividad_diaria[5],
                    "ad_estado": detalles_actividad_diaria[6],
                    "ad_fecha_bd": detalles_actividad_diaria[7],
                }
                lista_actividades_diarias.append(actividad_diaria)
            return {
                "mensaje": "Has obtenido tu lista de actividades diarias", 
                "actividad_diaria": lista_actividades_diarias
                }
        else:
            return {
                "mensaje": "No hay actividades registradas"
                }

    except Exception as e:
        return {"error": 'Error al obtener la lista de actividades diarias', "exception": str(e)}
    
@router_actividad_diaria.get("/actividad_diaria_activa/", tags=["Actividad Diaria"])
async def obtenerActividadesDiariasActivas():
    try:
        conn = database.getConnection()
        cursor = conn.cursor()

        query = ''' 
                    SELECT 
                        ad_secuencial, 
                        ad_descripcion, 
                        ad_hora_inicio, 
                        ad_hora_fin, 
                        ad_dia, 
                        ad_usuario,
                        ad_estado,
                        ad_fecha_bd
                    FROM 
                        actividad_diaria
                    WHERE
                        ad_estado = 'A';
                '''
        cursor.execute(query)
        actividades_diarias = cursor.fetchall()

        conn.close()

        if actividades_diarias:
            lista_actividades_diarias = []
            for detalles_actividad_diaria in actividades_diarias:
                actividad_diaria = {
                    "ad_secuencial": detalles_actividad_diaria[0],
                    "ad_descripcion": detalles_actividad_diaria[1],
                    "ad_hora_inicio": detalles_actividad_diaria[2],
                    "ad_hora_fin": detalles_actividad_diaria[3],
                    "ad_dia": detalles_actividad_diaria[4],
                    "ad_usuario": detalles_actividad_diaria[5],
                    "ad_estado": detalles_actividad_diaria[6],
                    "ad_fecha_bd": detalles_actividad_diaria[7],
                }
                lista_actividades_diarias.append(actividad_diaria)
            return {
                "mensaje": "Has obtenido tu lista de actividades diarias activas", 
                "actividad_diaria": lista_actividades_diarias
                }
        else:
            return {
                "mensaje": "No hay actividades activas registradas"
                }
    except Exception as e:
        return {"error": 'Error al obtener la lista de actividades diarias activas', "exception": str(e)}

@router_actividad_diaria.get("/actividad_diaria_finalizada/", tags=["Actividad Diaria"])
async def obtenerActividadesDiariasFinalizadas():
    try:
        conn = database.getConnection()
        cursor = conn.cursor()

        query = ''' 
                    SELECT 
                        ad_secuencial, 
                        ad_descripcion, 
                        ad_hora_inicio, 
                        ad_hora_fin, 
                        ad_dia, 
                        ad_usuario,
                        ad_estado,
                        ad_fecha_bd
                    FROM 
                        actividad_diaria
                    WHERE
                        ad_estado = 'F';
                '''
        cursor.execute(query)
        actividades_diarias = cursor.fetchall()

        conn.close()

        if actividades_diarias:
            lista_actividades_diarias = []
            for detalles_actividad_diaria in actividades_diarias:
                actividad_diaria = {
                    "ad_secuencial": detalles_actividad_diaria[0],
                    "ad_descripcion": detalles_actividad_diaria[1],
                    "ad_hora_inicio": detalles_actividad_diaria[2],
                    "ad_hora_fin": detalles_actividad_diaria[3],
                    "ad_dia": detalles_actividad_diaria[4],
                    "ad_usuario": detalles_actividad_diaria[5],
                    "ad_estado": detalles_actividad_diaria[6],
                    "ad_fecha_bd": detalles_actividad_diaria[7],
                }
                lista_actividades_diarias.append(actividad_diaria)
            return {
                "mensaje": "Has obtenido tu lista de actividades diarias finalizadas", 
                "actividad_diaria": lista_actividades_diarias
                }
        else:
            return {
                "mensaje": "No hay actividades finalizadas registradas"
                }

    except Exception as e:
        return {"error": 'Error al obtener la lista de actividades diarias finalizadas', "exception": str(e)}

@router_actividad_diaria.get("/actividad_diaria/{ad_usuario}", tags=["Actividad Diaria"])
async def obtenerActividadesDiariasPorUsuario(ad_usuario: str):
    try:
        conn = database.getConnection()
        cursor = conn.cursor()

        query = ''' 
                    SELECT 
                        ad_secuencial, 
                        ad_descripcion, 
                        ad_hora_inicio, 
                        ad_hora_fin, 
                        ad_dia, 
                        ad_usuario,
                        ad_estado,
                        ad_fecha_bd
                    FROM 
                        actividad_diaria
                    WHERE   
                        ad_usuario=%s
                    ORDER BY
                        ad_fecha_bd, 
                        CASE
                            WHEN ad_dia = 'L' THEN 1
                            WHEN ad_dia = 'M' THEN 2
                            WHEN ad_dia = 'MI' THEN 3
                            WHEN ad_dia = 'J' THEN 4
                            WHEN ad_dia = 'V' THEN 5
                            WHEN ad_dia = 'S' THEN 6
                            WHEN ad_dia = 'D' THEN 7
                        END;
                '''
        cursor.execute(query, (ad_usuario,))
        actividades_diarias = cursor.fetchall()

        conn.close()

        if actividades_diarias:
            lista_actividades_diarias = []
            for detalles_actividad_diaria in actividades_diarias:
                actividad_diaria = {
                    "ad_secuencial": detalles_actividad_diaria[0],
                    "ad_descripcion": detalles_actividad_diaria[1],
                    "ad_hora_inicio": detalles_actividad_diaria[2],
                    "ad_hora_fin": detalles_actividad_diaria[3],
                    "ad_dia": detalles_actividad_diaria[4],
                    "ad_usuario": detalles_actividad_diaria[5],
                    "ad_estado": detalles_actividad_diaria[6],
                    "ad_fecha_bd": detalles_actividad_diaria[7],
                }
                lista_actividades_diarias.append(actividad_diaria)
            return {
                "mensaje": "Has obtenido tu lista de actividades diarias", 
                "actividades_diarias": lista_actividades_diarias
                }
        else:
            return {
                "mensaje": "El usuario indicado no tiene actividades registradas"
                }

    except Exception as e:
        return {"error": 'Error al obtener la lista de actividades diarias', "exception": str(e)}
    
@router_actividad_diaria.post("/actividad_diaria/insert/", tags=["Actividad Diaria"])
async def crearActividadDiaria(ad_descripcion: str, ad_hora_inicio: str, ad_hora_fin: str, ad_dia: str, ad_usuario: str):
    try:
        conn = database.getConnection()
        cursor = conn.cursor()

        query = ''' 
                    INSERT INTO  actividad_diaria ( 
                        ad_descripcion, 
                        ad_hora_inicio, 
                        ad_hora_fin, 
                        ad_dia, 
                        ad_usuario,
                        ad_estado,
                        ad_fecha_bd
                    ) VALUES (
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        'A',
                        now()
                    ) RETURNING 
                        ad_secuencial,
                        ad_descripcion, 
                        ad_hora_inicio, 
                        ad_hora_fin, 
                        ad_dia, 
                        ad_usuario,
                        ad_estado,
                        ad_fecha_bd
                '''
        cursor.execute(query, (ad_descripcion, ad_hora_inicio, ad_hora_fin, ad_dia, ad_usuario))
        detalles_actividad_diaria = cursor.fetchone()

        conn.commit()
        conn.close()

        if detalles_actividad_diaria:
            actividad_diaria = {
                "ad_secuencial": detalles_actividad_diaria[0],
                "ad_descripcion": detalles_actividad_diaria[1],
                "ad_hora_inicio": detalles_actividad_diaria[2],
                "ad_hora_fin": detalles_actividad_diaria[3],
                "ad_dia": detalles_actividad_diaria[4],
                "ad_usuario": detalles_actividad_diaria[5],
                "ad_estado": detalles_actividad_diaria[6],
                "ad_fecha_bd": detalles_actividad_diaria[7],
            }
            return{
                    "mensaje": "Actividad registrada correctamente", "actividad_diaria": actividad_diaria
            }
        else:
            return {
                "mensaje": "Error al obtener los detalles de la actividad creada"
                }

    except Exception as e:
        return {"error": 'Error al crear la actividad', "exception": str(e)}

@router_actividad_diaria.put("/actividad_diaria/update/{ad_secuencial}", tags=["Actividad Diaria"])
async def actualizarActividadDiaria(ad_secuencial: int, ad: updateActividadDiaria):
    try:
        conn = database.getConnection()
        cursor = conn.cursor()

        query = ''' 
                    UPDATE actividad_diaria 
                    SET 
                        ad_descripcion = %s, 
                        ad_hora_inicio = %s, 
                        ad_hora_fin = %s
                    WHERE
                        ad_secuencial = %s
                '''
        cursor.execute(query, (ad.descripcion, ad.hora_inicio, ad.hora_fin, ad_secuencial))
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Actividad no existente")

        query = ''' 
                    SELECT 
                        ad_secuencial, 
                        ad_descripcion, 
                        ad_hora_inicio, 
                        ad_hora_fin, 
                        ad_dia, 
                        ad_usuario,
                        ad_estado,
                        ad_fecha_bd
                    FROM 
                        actividad_diaria
                    WHERE   
                        ad_secuencial=%s
                '''
        cursor.execute(query, (ad_secuencial,))
        detalles_actividad_diaria = cursor.fetchone()

        conn.commit()
        conn.close()

        if detalles_actividad_diaria:
            actividad_diaria = {
                "ad_secuencial": detalles_actividad_diaria[0],
                "ad_descripcion": detalles_actividad_diaria[1],
                "ad_hora_inicio": detalles_actividad_diaria[2],
                "ad_hora_fin": detalles_actividad_diaria[3],
                "ad_dia": detalles_actividad_diaria[4],
                "ad_usuario": detalles_actividad_diaria[5],
                "ad_estado": detalles_actividad_diaria[6],
                "ad_fecha_bd": detalles_actividad_diaria[7],
            }
            return{
                    "mensaje": "Actividad actualizada correctamente", "actividad_diaria": actividad_diaria
            }
        else:
            return {
                "mensaje": "Error al obtener los detalles de la actividad creada"
                }

    except Exception as e:
        return {"error": 'Error al actualizar la actividad', "exception": str(e)}

@router_actividad_diaria.delete("/actividad_diaria/delete/{ad_secuencial}", tags=["Actividad Diaria"])
async def actualizarActividadDiaria(ad_secuencial: int):
    try:
        conn = database.getConnection()
        cursor = conn.cursor()

        query = ''' 
                    SELECT 
                        ad_secuencial, 
                        ad_descripcion, 
                        ad_hora_inicio, 
                        ad_hora_fin, 
                        ad_dia, 
                        ad_usuario,
                        ad_estado,
                        ad_fecha_bd
                    FROM 
                        actividad_diaria
                    WHERE   
                        ad_secuencial=%s
                '''
        cursor.execute(query, (ad_secuencial,))
        actividad_diaria = cursor.fetchone()

        if not actividad_diaria:
            return HTTPException(status_code=404, detail="Intentas borrar una actividad no existente")

        

        query = ''' 
                    DELETE FROM 
                        actividad_diaria 
                    WHERE
                        ad_secuencial = %s
                    RETURNING 
                        ad_secuencial,
                        ad_descripcion, 
                        ad_hora_inicio, 
                        ad_hora_fin, 
                        ad_dia, 
                        ad_usuario,
                        ad_estado,
                        ad_fecha_bd
                '''
        cursor.execute(query, (ad_secuencial,))
            
        detalles_actividad_diaria = cursor.fetchone()

        conn.commit()
        conn.close()

        if detalles_actividad_diaria:
            actividad_diaria = {
                "ad_secuencial": detalles_actividad_diaria[0],
                "ad_descripcion": detalles_actividad_diaria[1],
                "ad_hora_inicio": detalles_actividad_diaria[2],
                "ad_hora_fin": detalles_actividad_diaria[3],
                "ad_dia": detalles_actividad_diaria[4],
                "ad_usuario": detalles_actividad_diaria[5],
                "ad_estado": detalles_actividad_diaria[6],
                "ad_fecha_bd": detalles_actividad_diaria[7],
            }
            return{
                    "mensaje": "Actividad eliminada correctamente", "actividad_diaria": actividad_diaria
            }
        else:
            return {
                "mensaje": "Error al obtener los detalles de la actividad eliminada. Actividad no eliminada."
                }
        
    except Exception as e:
        return {"error": 'Error al eliminar la actividad', "exception": str(e)}    
